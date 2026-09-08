### Get the list from the database
```php
public function index(Request $request){
    try{
        $location = Location::orderBy('name','asc')->whereNotIn('id', [1])->get();
        return view('admin.booking.index', compact('location'));
    }catch (Exception $e) {
        Log::error($e->getMessage(), $e->getTrace());
    }
}
```


### With laravel ajax
```php
use DataTables;
use App\DataTables\ExportDataTable;

public function customerList(Request $request)
    {
        //\DB::enableQueryLog();
        try{
            if ($request->ajax()) {
                $customer_data= User::select('users.id','users.first_name', 'users.last_name','users.email','users.phone',
                                            'bookings.booking_hour','advance_bookings.used_days','advance_bookings.end_date',
                                            'advance_bookings.remaining_days','advance_bookings.days', 'advance_bookings.updated_at'
                    )
                ->leftjoin('bookings','bookings.user_id','users.id')
                ->leftjoin('advance_bookings', 'advance_bookings.user_id', 'users.id')
                ->leftjoin('payment_histories', 'payment_histories.booking_id', '=', 'bookings.id')
                ->where('bookings.is_advanced', '1')
                ->where(
                        function ($q) {
                            $q->where('payment_histories.status', 'COMPLETED')
                                ->orWhere('bookings.payment_status', 'exsting_user')
                                ->orWhere('bookings.payment_status', 'cash')
                                // ->orWhere('customers.is_import', '1')
                                ->orWhere('bookings.is_advanced', '1');
                     
                        }
                    )
                ->get();
                
                return Datatables::of($customer_data)->addIndexColumn()
                    ->addColumn(
                        'first_name', function ($row) {
                            $first_name = '';
                            if($row->first_name == "") {
                                $first_name .= '--';
                            }else{
                                $first_name .= $row->first_name.' '.$row->last_name;
                            }
                            return $first_name;
                        }
                    )
                ->addColumn(
                    'email', function ($row) {
                        $email = '';
                        if($row->email == "") {
                            $email .= '--';
                        }else{
                            $email .= $row->email;
                        }
                        return $email;
                    }
                )
                ->addColumn(
                    'end_date', function ($row) {
                        $end_date = '';
                        if($row->end_date == "") {
                            $end_date .= '--';
                        }else{
                            $end_date .= date('m-d-Y', strtotime($row->end_date));
                        
                        }
                        return $end_date;
                    }
                )
                ->addColumn(
                    'action', function ($row) {
                            $editPath=url('customer/'.$row->id);
                            $btn = '
                        <a onclick="customer_delete('.$row->id.');"
                        class="btn btn-danger btn-sm rounded-0" type="button" data-toggle="modal"
                        data-placement="top" title="Delete"><i class="fa fa-trash"></i></a>
                        <a  href="javascript:void(0)" 
                        id="show-user" 
                        data-url="'.$editPath.'" 
                        class="btn btn-primary btn-sm rounded-0 float-right"><i class="fas fa-eye"></i></a>';
                        
                            return $btn;
                    }
                )
                ->rawColumns(['action'])->make(true);
            }
            // return view('admin/customer/list');
            return view('admin/customer/list');
        }catch (Exception $e) {
            Log::error($e->getMessage(), $e->getTrace());
        }
    }
```


### Blade file
```php
@if($getTransctionByLocation->count() > 0)
    @foreach ($getTransctionByLocation as $transaction)
    <tr>
        <td>{{$transaction['first_name']}} {{$transaction['last_name']}}</td>
        <td>$&nbsp;{{number_format((float)$transaction['amount'], 2, '.', '')}}</td>
        <td>{{$transaction['created_at']->format('m/d/Y')}} / {{$transaction['created_at']->format('h:m A')}}</td>
        <td>{{ \Carbon\Carbon::parse($startDate)->format('m/d/Y') }}</td>
    </tr>
    @endforeach
    @else
    <tr>
        <td colspan="4" style="text-align:center">No data found</td>
    </tr>
@endif
```
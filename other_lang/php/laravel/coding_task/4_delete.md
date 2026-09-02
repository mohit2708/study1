### Route file
```php
Route::get('/customer/destroy/{id}', [App\Http\Controllers\Admin\CustomerController::class, 'destroy'])->name('customer.destroy');
```


### in controller
```php
public function destroy($id){
	try{  
		Customer::where('id', $id)->delete();	
		$user = User::where('id', $id)->firstorfail()->delete();
		return redirect('customer/list')->with('success', 'Customer deleted successfully!');
	}catch (Exception $e) {
		Log::error($e->getMessage(), $e->getTrace());
	}
}

```

### Delete with bootstrap model
```php
# in blade file

<a onclick="confirm_delete('.$row->id.');" class="delete btn btn-link" title="Delete" data-toggle="modal" style="color: #F44336;"><i class="fa fa-trash"></i></a>

<a onclick="customer_delete({{$customer->id}})" class="btn btn-danger btn-sm rounded-0" type="button" data-toggle="modal" data-placement="top" title="Delete"><i class="fa fa-trash"></i></a>

<div id="delete_confirm" class="modal fade" role="dialog">
	<div class="modal-dialog">
		<div class="modal-content">         
				<div class="modal-header">						
					<h4 class="modal-title">Delete Item</h4>
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
				</div>
				<div class="modal-body">					
					<p>Are you sure you want to delete this item?</p>					
				</div>
				<div class="modal-footer">
					<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancel">
					<span id="delete_butt_id"></span>
				</div>			
		</div>
	</div>
</div>

<script>
function confirm_delete(id){
	var url="{{url('equipment/delete/')}}";
	var a='<a href="'+url+'/'+id+'" class="btn btn-primary">Confirm</a>';
	$("#delete_butt_id").html(a);
	$("#delete_confirm").modal();
}
</script>
```

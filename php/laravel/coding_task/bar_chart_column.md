### Bar chart column
```php
@extends('admin.app') @section('content')
<section class="content-header">
    <div class="container-fluid">
        <div class="row mb-2">
            <div class="col-sm-6">
                <h1>Sales Report</h1>
            </div>
            <div class="col-sm-6">
                <ol class="breadcrumb float-sm-right">
                    <li class="breadcrumb-item"><a href="{{url('/admin/home')}}">Home</a></li>
                    <li class="breadcrumb-item">Sales Report</li>
                </ol>
            </div>
        </div>
    </div>
</section>

<section class="content">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header border-0">
                        <div class="d-flex justify-content-between">
                            <h3 class="card-title">Online Store Visitors</h3>
                            <a href="javascript:void(0);">View Report</a>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="d-flex">
                            <p class="d-flex flex-column">
                                <span class="text-bold text-lg">820</span>
                                <span>Visitors Over Time</span>
                            </p>
                            <p class="ml-auto d-flex flex-column text-right">
                                <span class="text-success"> <i class="fas fa-arrow-up"></i> 12.5% </span>
                                <span class="text-muted">Since last week</span>
                            </p>
                        </div>

                        <div class="position-relative mb-4">
                            <canvas id="visitors-chart" height="320"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="card">
                    <div class="card-header">
                        <button id="dailyBtn" onclick="updateChart('daily', this)" class="btn btn-secondary">Daily</button>
                        <button id="weeklyBtn" onclick="updateChart('weekly', this)" class="btn btn-secondary">Weekly</button>
                        <button id="monthlyBtn" onclick="updateChart('monthly', this)" class="btn btn-secondary">Monthly</button>
                        <button id="yearlyBtn" onclick="updateChart('yearly', this)" class="btn btn-secondary">Yearly</button>
                        <select id="locationDropdown" onchange="updateChart()">
                            @isset($locationList)
                            <option value="all">All Locations</option>
                            @foreach($locationList as $loc)
                            <option value="{{ $loc->id }}">{{ $loc->name }}</option>
                            @endforeach
                            @endisset
                            
                            <!-- <option value="1">Location 1</option>
                            <option value="2">Location 2</option>
                            <option value="3">Location 3</option> -->
                            <!-- Add more locations as needed -->
                        </select>
                    </div>
                    <div class="card-body">
                        <div class="position-relative mb-4">
                            <canvas id="myChart" width="400" height="200"></canvas>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-12">
                <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">Break even calculations</h3>
                    </div>
                    <div class="card-body">
                        <table id="sales_report_table" class="table table-bordered table-hover">
                            <thead>
                                <tr>
                                    <th>Full name</th>
                                    <th>Location</th>
                                    <th>Amount</th>
                                    <th>Payment Type</th>
                                    <th >Date</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Krishna</td>
                                    <td>DD</td>
                                    <td>$ 200</td>
                                    <td>Cash</td>
                                    <td>07/15/2024</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

@endsection @section('script')
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="{{ asset('admin/js/admin.js') }}"></script>
<script>
/*
* Data table script
*/
$(function () {
    $("#sales_report_table").DataTable({
        columnDefs: [
            {
                orderable: false,
                targets: [3, 4],
            },
        ],
        paging: true,
        lengthChange: false,
        searching: false,
        ordering: true,
        info: true,
        autoWidth: false,
        responsive: true,
    });
});
/*
* Bar chart column script
*/
    const chartData = {
        daily: {
            all: { labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], data: [29, 45, 16, 25, 11, 20, 19] },
            Atrium: { labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], data: [12, 19, 50, 5, 2, 3, 4] },
            loc2: { labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], data: [7, 11, 5, 8, 3, 7, 6] },
            loc3: { labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], data: [10, 15, 8, 12, 6, 10, 9] },
        },
        weekly: {
            all: { labels: ["Week 1", "Week 2", "Week 3", "Week 4"], data: [150, 180, 210, 240] },
            Atrium: { labels: ["Week 1", "Week 2", "Week 3", "Week 4"], data: [50, 60, 70, 80] },
            loc2: { labels: ["Week 1", "Week 2", "Week 3", "Week 4"], data: [45, 55, 65, 75] },
            loc3: { labels: ["Week 1", "Week 2", "Week 3", "Week 4"], data: [55, 65, 75, 85] },
        },
        monthly: {
            all: { labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], data: [600, 900, 1200, 1500, 1800, 1900, 1700, 1600, 1500, 1700, 2800, 3200] },
            Atrium: { labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], data: [200, 300, 400, 500, 600, 1900, 1700, 1600, 1500, 1700, 2800, 3200] },
            loc2: { labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], data: [180, 280, 380, 480, 580, 1900, 1700, 1600, 1500, 1700, 2800, 3200] },
            loc3: { labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], data: [220, 320, 420, 520, 620, 1900, 1700, 1600, 1500, 1700, 2800, 3200] },
        },
        yearly: {
            all: { labels: ["2020", "2021", "2022", "2023", "2024"], data: [7200, 7500, 7800, 8100, 5000] },
            Atrium: { labels: ["2020", "2021", "2022", "2023", "2024"], data: [2400, 2500, 2600, 2700, 6000] },
            loc2: { labels: ["2020", "2021", "2022", "2023", "2024"], data: [2300, 2400, 2500, 2600, 7000] },
            loc3: { labels: ["2020", "2021", "2022", "2023", "2024"], data: [2100, 2300, 2500, 2800, 9000] },
        },
    };

    let myChart;
    let currentPeriod = "daily";

    function createChart(data, labels) {
        const ctx = document.getElementById("myChart").getContext("2d");
        if (myChart) {
            myChart.destroy();
        }
        myChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Sales Report",
                        data: data,
                        backgroundColor: "rgba(75, 192, 192, 0.2)",
                        borderColor: "rgba(75, 192, 192, 1)",
                        borderWidth: 1,
                    },
                ],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    }

    function updateChart(period, button) {
        if (period) {
            currentPeriod = period;
            setActiveButton(button);
        } else {
            period = currentPeriod;
        }
        const location = document.getElementById("locationDropdown").value;
        const beach_loc = $('#locationDropdown').val();

        const data = chartData[period][location].data;
        const labels = chartData[period][location].labels;

        // var CSRF_TOKEN = $('meta[name="csrf-token"]').attr("content");
        // $.ajax({
        //     type: 'POST',
        //     url: "/sales-report-data",
        //     data: {
        //         period: period,
        //         location: location,
        //         beach_loc :beach_loc,
        //         // data: data,
        //         // labels: labels,
        //         _token: CSRF_TOKEN
        //     },
        //     success: function(response) {
        //         console.log(response);
        //         const data = response.data;
        //         const labels = response.labels;
        //         createChart(data, labels);
        //     },
        //     error: function(xhr, status, error) {
        //         console.error('Error setting session dates');
        //     }
        // });
        createChart(data, labels);

        
    }

    function setActiveButton(button) {
        const buttons = document.querySelectorAll("button.btn-secondary, button.btn-success");
        buttons.forEach((btn) => {
            btn.classList.remove("btn-success");
            btn.classList.add("btn-secondary");
        });
        button.classList.remove("btn-secondary");
        button.classList.add("btn-success");
    }

    // Initialize with daily data for all locations
    document.addEventListener("DOMContentLoaded", () => {
        document.getElementById("locationDropdown").value = "all";
        const dailyBtn = document.getElementById("dailyBtn");
        dailyBtn.classList.add("btn-success");
        updateChart("daily", dailyBtn);
    });
</script>
@stop

```
```php
public function getSalesReportData(Request $request){
        $period = $request->input('period', 'daily');
        $beach_loc = $request->input('beach_loc', 'all'); // Default to 'all' if not provided


        $total=BookingTransaction::select(DB::raw('SUM(amount) as total')) ->when($beach_loc!='all',function($query)use($beach_loc){
                return $query->where('beach_location',$beach_loc);
                });

        switch ($period) {
            case 'daily':
                $date = Carbon::now()->subDays(6);
               $total=$total->addSelect(DB::raw('DAYNAME(created_at) as period'))
               ->where('created_at', '>=', $date)
                        ->groupBy(DB::raw('DAYNAME(created_at)'))
                        ->orderBy(DB::raw('DATE(created_at)'), 'ASC');
               
                break;
            case 'weekly':
                $date = Carbon::now()->subWeeks(3)->startOfWeek();
                $total= $total
                    ->addSelect(DB::raw('YEARWEEK(created_at, 1) as period'))
                    ->where('created_at', '>=', $date)
                    ->groupBy(DB::raw('YEARWEEK(created_at, 1)'))
                    ->orderBy(DB::raw('YEARWEEK(created_at, 1)'), 'ASC');
                break;
            case 'monthly':
                $date = Carbon::now()->subMonths(11)->startOfMonth();
                    $total = $total
                        ->addSelect(DB::raw('MONTHNAME(created_at) as period'))
                        ->where('created_at', '>=', $date)
                        ->groupBy(DB::raw('YEAR(created_at)'), DB::raw('MONTHNAME(created_at)'))
                        ->orderBy(DB::raw('YEAR(created_at)'), 'desc')
                        ->orderBy(DB::raw('MONTH(created_at)'), 'desc');
                break;
            case 'yearly':
                $date = Carbon::now()->subYears(5)->startOfYear();
                    $total = $total
                        ->addSelect(DB::raw('YEAR(created_at) as period'))
                        ->where('created_at', '>=', $date)
                        ->groupBy(DB::raw('YEAR(created_at)'))
                        ->orderBy(DB::raw('YEAR(created_at)'), 'desc');
                break;
          
        }
       
        $total=$total->get()->keyBy('period')->toArray();
       
        $data=['labels' => [], 'data' => []];
        switch ($period) {
            case 'daily':
                for ($i = 6; $i >= 0; $i--) {
                    $day= Carbon::now()->subDays($i)->dayName;
                    $data['labels'][]=Carbon::now()->subDays($i)->format('D');
                    
                    if(isset($total[$day]))
                    $data['data'][]=$total[$day]['total'];
                    else
                    $data['data'][]=0;
                }
                break;
            case 'weekly':
                for ($i = 3; $i >=0; $i--) {
                    $week = Carbon::now()->subWeeks($i)->startOfWeek()->isoFormat('GGGGWW');
                    $data['labels'][]="Week ".$i+1;
                    if(isset($total[$week]))
                    $data['data'][]=$total[$week]['total'];
                    else
                    $data['data'][]=0;
                }
                break;
            case 'monthly':
                for ($i = 11; $i >=0; $i--) {
                    $month = Carbon::now()->subMonths($i)->startOfMonth()->format('F');
                    $data['labels'][]=Carbon::now()->subMonths($i)->startOfMonth()->format('M');
                    if(isset($total[$month]))
                    $data['data'][]=$total[$month]['total'];
                    else
                    $data['data'][]=0;
                }
                break;
            case 'yearly':
                for ($i = 4; $i >=0; $i--) {
                    $year = Carbon::now()->subYears($i)->startOfYear()->year;
                    $data['labels'][]=$year;
                    if(isset($total[$year]))
                    $data['data'][]=$total[$year]['total'];
                    else
                    $data['data'][]=0;
                }
                break;
        }
       
        
        return response()->json($data);

    }
```
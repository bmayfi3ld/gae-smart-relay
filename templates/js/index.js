google.load('visualization', '1', { packages : ['controls'] } );

function drawChart(arrayIN) {
		
	// create data
	var dataArr = [];
	for(var i = 0; i < arrayIN[0].length-1; i++) 
	{
		dataArr[i] = new google.visualization.DataTable();
	}
	
	// convert back to date
	for(var i = 1; i < arrayIN.length; i++) 
	{
		arrayIN[i][0] = new Date(arrayIN[i][0])       
	}

	// add date to all graphs
	for(var i = 0; i < arrayIN[0].length-1; i++) 
	{
		dataArr[i].addColumn('datetime', 'Time');
	}

	// create individual graph legends and add data
	for(var i = 0; i < arrayIN[0].length-1; i++) 
	{
		dataArr[i].addColumn('number', arrayIN[0][i+1]);
		
		for(var j = 1; j < arrayIN.length; j++) 
		{
			dataArr[i].addRow([arrayIN[j][0],arrayIN[j][i+1]])
		}
	}
	
	// add all charts arrayIN[0].length-1
	for(var i = 0; i < arrayIN[0].length-1; i++) {
		
		var dash_container = document.getElementById('dashboard' + i),
		myDashboard = new google.visualization.Dashboard(dash_container);
	
		var myDateSlider = new google.visualization.ControlWrapper({
			'controlType': 'ChartRangeFilter',
			'containerId': 'control' + i,
			'options': {
				'filterColumnLabel': 'Time'
			}
		});
		
		var chart = new google.visualization.ChartWrapper({
			'chartType': 'LineChart',
			'containerId': 'chart' + i,
		});
		
		myDashboard.bind(myDateSlider, chart)
		
		//var chart = new google.charts.Line(document.getElementById('chart' + i));
		myDashboard.draw(dataArr[i]);
	}
}
	
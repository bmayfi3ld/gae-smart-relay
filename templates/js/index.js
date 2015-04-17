google.load('visualization', '1.1', {packages: ['line']});
google.load("visualization", "1", {packages:["gauge"]});


function drawChart(arrayIN) {

	var dataArr = [];
	// create all graphs
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
  // add all charts
	for(var i = 0; i < arrayIN[0].length-1; i++) {
		var options = {
			chart: {
				 title: arrayIN[0][i+1]
			},      
			//width: 100,
			//width: document.getElementById('chart' + i).offsetWidth,
			height: 350,
			legend: {position: 'none'},                    
		}
		var chart = new google.charts.Line(document.getElementById('chart' + i));
		chart.draw(dataArr[i], options);
	}
}
	
function drawGauge(uptime) {
        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          ['', 5],
        ]);

        var options = {
          redFrom: 0, redTo: 10,
          yellowFrom:10, yellowTo: 25,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('gauge'));

        chart.draw(data, options);
      }
	
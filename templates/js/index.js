google.load('visualization', '1.1', {packages: ['line']});


function drawChart(arrayIN) {

	var dataArr = [];
	// create all graphs
	for(var i = 0; i < arrayIN[0].length-1; i++) 
	{
		dataArr[i] = new google.visualization.DataTable();
	}

	// add date to all graphs
	for(var i = 0; i < arrayIN[0].length-1; i++) {
		dataArr[i].addColumn('number', 'Time');
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
			width: 100,
			//width: document.getElementById('chart' + i).offsetWidth,
			height: 500,
			curveType: 'function',
			legend: {position: 'none'},                    
		}
		var chart = new google.charts.Line(document.getElementById('chart' + i));
		chart.draw(dataArr[i], options);
	}
}
	
	
google.load("visualization", "1", {packages:["gauge"]});
	
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
	
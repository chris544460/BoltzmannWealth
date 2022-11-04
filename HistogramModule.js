// const HistogramModule = function(bins, canvas_width, canvas_height){
//     // Create a canvas element
//     const canvas = document.createElement('canvas');
//     Object.assign(canvas,{
//         width: canvas_width,
//         height: canvas_height,
//         style : "border:1px dotted",
//     });
//     // Appemd it to #elements
//     const elements = document.getElementById('elements');
//     elements.appendChild(canvas);

//     // Create a 2D context
//     const ctx = canvas.getContext('2d');

//     // Prep the chart properties and series
//     const datasets = [{
//         label: 'Data',
//         fillColor: "rgba(151,187,205,0.5)",
//         strokeColor: "rgba(151,187,205,0.8)",
//         highlightFill: "rgba(151,187,205,0.75)",
//         highlightStroke: "rgba(151,187,205,1)",
//         data: []
//     }];

//     // Add a zero value for each bin
//     for(var i in bins)
//         datasets[0].data.push(0)

//     const data = {
//         labels: bins,
//         datasets: datasets
//     }

//     const options = {
//         scaleBeginAtZero : true
//     };

//     // Create the chart
//     const chart = new Chart(ctx, {type: 'bar', data: data, options: options});

//     this.render = function(data){
//         datasets[0].data = data;
//         chart.update();
//     };

//     this.reset = function(){
//         chart.destroy();
//         chart = new Chart(context, {type: 'bar', data: data, options: options});
//     };
// }

const HistogramModule = function(bins, canvas_width, canvas_height) {
    // Create the canvas object:
    const canvas = document.createElement("canvas");
    Object.assign(canvas, {
    width: canvas_width,
    height: canvas_height,
    style: "border:1px dotted",
    });
    // Append it to #elements:
    const elements = document.getElementById("elements");
    elements.appendChild(canvas);

    // Create the context and the drawing controller:
    const context = canvas.getContext("2d");
    // Prep the chart properties and series:
    const datasets = [{
        label: "Data",
        fillColor: "rgba(151,187,205,0.5)",
        strokeColor: "rgba(151,187,205,0.8)",
        highlightFill: "rgba(151,187,205,0.75)",
        highlightStroke: "rgba(151,187,205,1)",
        data: []
    }];
    // Add a zero value for each bin
    for (var i in bins)
    datasets[0].data.push(0);
    const data = {
        labels: bins,
        datasets: datasets
    };
    const options = {
        scaleBeginsAtZero: true
    };
    // Create the chart object
    var chart = new Chart(context, {type: 'bar', data: data, options: options});

    
    this.render = function(data) {
        datasets[0].data = data;
        chart.update();
      };
    
      this.reset = function() {
        chart.destroy();
        chart = new Chart(context, {type: 'bar', data: data, options: options});
    }
}


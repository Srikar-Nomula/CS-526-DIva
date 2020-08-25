//================================================
// Function to generate the value for the chart
// Inputs : None
// Outputs: None
// Call the chart instance and pass the parameters
// for the function to plot
//================================================
function guagedata(){
     name_d = GetSelectedText();  // get the selected value from dropdown.
     key_value = guage_data[ name_d ];
     generateChart(key_value)
}

//================================================
// Function to generate the value for the chart
// Fucntion name: generateChart
// Inputs : selected key value, String
// Outputs: None
// Create the chart instance and plot the rating for
// the selected district
//================================================
function generateChart(key_value){
    // create chart
    var guage_chart = am4core.create("guagechart", am4charts.GaugeChart);
    guage_chart.innerRadius = -50;
    guage_chart.width=am4core.percent(100);
    guage_chart.height=am4core.percent(80);

    var axis = guage_chart.xAxes.push(new am4charts.ValueAxis());
    axis.min = 0;
    axis.max = 10;
    axis.strictMinMax = true;

    var colorSet = new am4core.ColorSet();

    // Define three ranges or bands in the guage chart
    var range0 = axis.axisRanges.create();
    range0.value = 0;
    range0.endValue = 5;
    range0.axisFill.fillOpacity = 1;
    range0.axisFill.fill = colorSet.getIndex(0);
    range0.axisFill.fill = am4core.color("green");

    var range1 = axis.axisRanges.create();
    range1.value = 5;
    range1.endValue = 8;
    range1.axisFill.fillOpacity = 1;
    range1.axisFill.fill = am4core.color("orange");

    var range2 = axis.axisRanges.create();
    range2.value = 8;
    range2.endValue = 10;
    range2.axisFill.fillOpacity = 1;
    range2.axisFill.fill = colorSet.getIndex(4);
    range2.axisFill.fill = am4core.color("red");

    // Update the guage chart with the new value
    var hand = guage_chart.hands.push(new am4charts.ClockHand());
    hand.showValue(key_value, am4core.ease.cubicOut);

}

//================================================
// Function to get the value for the chart
// Inputs : None
// Outputs: name of selected value
// Get the required parameters from the application
//================================================
function GetSelectedText(){
    var e = document.getElementById("District");
    var name_d = e.options[e.selectedIndex].text;
    return name_d;
}

// Get the data from the specified URL
fetch('http://127.0.0.1:5000/Safety_Rating')
    .then(res => res.json())
    .then(data => { guage_data = data})
    .then((out) => {
        generateChart(guage_data.Central);
    }).catch(err => console.error(err));
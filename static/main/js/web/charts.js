
function chartConfig(args="normal", right=false, rightColor='grey', sole=false, chartType="bar") {
    if (sole == true) {
        let config = {
        plugins: { legend: {
            display: false
        }},
        indexAxis: chartType == "horizontalBar" ? "y" : "x",
        scales: {
            x: { display: false },
            left: {
            ticks: {
                beginAtZero: true,
                callback: function(value, index, values) {
                if (args == "pct") return Math.round(value * 100) + '%';
                else return value
                },},
            position: 'left',
            display: false,
            }
        } }
        return config
    } 

    let config = {
        plugins: { legend: { labels: {
        display: sole == true ? 
        fontColor: "rgb(255, 255, 255)",
        font: { size: 14, } 
        } } 
        },
        plugins: [{
        afterDraw: chart => {
            if (chart.tooltip?._active?.length) {
                let x = chart.tooltip._active[0].element.x;
                let yAxis = chart.scales.y;
                let ctx = chart.ctx;
                ctx.save();
                ctx.beginPath();
                ctx.moveTo(x, yAxis.top);
                ctx.lineTo(x, yAxis.bottom);
                ctx.lineWidth = 1;
                ctx.strokeStyle = '#ff0000';
                ctx.stroke();
                ctx.restore();
            }
        }
        }],
        options: {
        indexAxis: chartType === "horizontalBar" ? "y" : "x",
        interaction: {
            intersect: false,
            mode: 'index',
        }
        },
        scales: {
        x: {
            grid: { display: false },
        },
        left: {
            grid: { display: false },
            ticks: {
            beginAtZero: true,
            callback: function(value) {
                if (args == "pct") return Math.round(value * 100) + '%';
                else return value
            },
            font: 14,
            },
            type: 'linear',
            position: 'left',
        },
        right: {
            grid: { display: false },
            ticks: {
            beginAtZero: true,
            callback: function(value) {
                if (args == "pct") return Math.round(value * 100) + '%';
                else return value
            },
            font: 14,
            color: rightColor,
            },
            type: 'linear',
            position: 'right',
            display: right == true ? true : false
        }
        } }
    return config
}


function basicChart(chartClass, chartObject, chartType, chartColor, chartData) {
  chartObject = new Chart(chartClass, {
    type: chartType,
    data: {
      labels: years,
      datasets: [{
        data: chartData,
        backgroundColor: chartColor,
      },],},
    options: chartConfig("normal", false, "0", true),
  }); 
}





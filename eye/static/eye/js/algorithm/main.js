const algorithm_canvas = document.querySelector(".algorithm_canvas").getContext("2d")

date = dateChart(date)

const algorithm_canvas1 = new Chart(algorithm_canvas, {
  type: "line",
  data: {
    labels: date,
    datasets: [{
      label: "Price",
      data: closePrice,
      backgroundColor: "cyan",
      borderColor: "cyan",
    }
  ],},
  options: chartConfig(),
});


function dateChart(date) {
  console.log(date)
}
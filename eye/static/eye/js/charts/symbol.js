const stock_margins_chart = document.querySelector('.stock_margins_chart').getContext('2d');
const chart1 = new Chart(stock_margins_chart, {
  type: 'bar',
  data: {
    labels: years,
    datasets: [{
      label: "Gross Margin",
      data: grossMargin,
      backgroundColor: "rgb(0, 110, 255)",
    }, {
      label: "Operating Margin",
      data: operatingMargin,
      backgroundColor: "rgb(20, 150, 255)",
    }, {
      label: "Profit Margin",
      data: profitMargin,
      backgroundColor: "rgb(20, 200, 240)",
    },],
  },
  options: chartConfig(),
});

const stock_metrics_chart = document.querySelector('.stock_metrics_chart').getContext('2d');
const chart2 = new Chart(stock_metrics_chart, {
  type: 'line',
  data: {
    labels: years,
    datasets: [{
      label: "EPS",
      data: eps,
      backgroundColor: "rgb(110, 255, 255)",
      borderColor: "rgb(110, 255, 255, 0.3)",
    }, {
      label: "P/B Ratio",
      data: pbRatio,
      backgroundColor: "rgb(110, 255, 0)",
      borderColor: "rgb(110, 255, 0, 0.3)",
    }, {
      label: "P/E Ratio",
      data: peRatio,
      backgroundColor: "rgb(138, 48, 255)",
      borderColor: "rgb(138, 48, 255, 0.3)",
      yAxisID: "right",
    },],
  },
  options: chartConfig("normal", true, "rgb(138, 48, 255)"),
});

const dividend_chart = document.querySelector('.stock_dividend_chart').getContext('2d');
const chart3 = new Chart(dividend_chart, {
  type: 'line',
  data: {
    labels: years,
    datasets: [{
      label: "Dividend in %",
      data: dividendYield,
      backgroundColor: "rgb(20, 150, 255)",
      borderColor: "rgb(20, 150, 255, 0.3)",
      yAxisID: "right",
    }, {
      label: "Payout Ratio",
      data: payoutRatio,
      backgroundColor: "rgb(144, 0, 255)",
      borderColor: "rgb(144, 0, 255, 0.4)",
    }]
  },
  options: chartConfig("pct", true, "rgb(20, 150, 255)"),
});



const cc_rev = document.querySelector('.chart_revenue').getContext('2d');
const cc_gp = document.querySelector('.chart_grossProfit').getContext('2d');
const cc_gm = document.querySelector('.chart_grossMargin').getContext('2d');
const cc_oe = document.querySelector('.chart_operatingExpenses').getContext('2d');
const cc_om = document.querySelector('.chart_operatingMargin').getContext('2d');
const cc_ni = document.querySelector('.chart_netIncome').getContext('2d');
const cc_pm = document.querySelector('.chart_profitMargin').getContext('2d');
const cc_eps = document.querySelector('.chart_eps').getContext('2d');
let c_rev, c_gp, c_gm, c_oe, c_om, c_ni, c_pm, c_eps;

const cc_rev2 = document.querySelector('.chart_revenue2').getContext('2d');
const cc_gp2 = document.querySelector('.chart_grossProfit2').getContext('2d');
const cc_gm2 = document.querySelector('.chart_grossMargin2').getContext('2d');
const cc_rd2 = document.querySelector('.chart_researchDevelopment2').getContext('2d');
const cc_sga2 = document.querySelector('.chart_sga2').getContext('2d');
const cc_oe2 = document.querySelector('.chart_operatingExpenses2').getContext('2d');
const cc_om2 = document.querySelector('.chart_operatingMargin2').getContext('2d');
const cc_ebt2 = document.querySelector('.chart_ebitda2').getContext('2d');
const cc_ibt2 = document.querySelector('.chart_incomeBeforeTax2').getContext('2d');
const cc_ni2 = document.querySelector('.chart_netIncome2').getContext('2d');
const cc_pm2 = document.querySelector('.chart_profitMargin2').getContext('2d');
const cc_eps2 = document.querySelector('.chart_eps2').getContext('2d');
const cc_pe2 = document.querySelector('.chart_peRatio2').getContext('2d');
let c_rev2, c_gp2, c_gm2, c_rd2, c_sga2, c_oe2, c_om2, c_ebt2, c_ibt2, c_ni2, c_pm2, c_eps2, c_pe2;

let chartClasses = [cc_rev, cc_gp, cc_gm, cc_oe, cc_om, cc_ni, cc_pm, cc_eps,
                    cc_rev2, cc_gp2, cc_gm2, cc_rd2, cc_sga2, cc_oe2, cc_om2, 
                    cc_ebt2, cc_ibt2, cc_ni2, cc_pm2, cc_eps2, cc_pe2];
let chartObjects = [c_rev, c_gp, c_gm, c_oe, c_om, c_ni, c_pm, c_eps,
                    c_rev2, c_gp2, c_gm2, c_rd2, c_sga2, c_oe2, c_om2, 
                    c_ebt2, c_ibt2, c_ni2, c_pm2, c_eps2, c_pe2];
let chartDataa = [revenue, grossProfit, grossMargin, operatingExpenses, operatingMargin,
                  netIncome, profitMargin, eps, revenue, grossProfit, grossMargin, rd, sga,
                  operatingExpenses, operatingMargin, ebitda, incomeBeforeTax, netIncome,
                  profitMargin, eps, peRatio];

for (let i = 0; i < chartClasses.length; i++) {
  basicChart(chartClasses[i], chartObjects[i], "bar", "rgb(20, 150, 255)", chartDataa[i]);
}


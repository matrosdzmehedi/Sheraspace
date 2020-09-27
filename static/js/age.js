
  $(document).ready(function () {
    var datas = [];
    var labels = [];
    var label = ['male','female'];
    $.ajax({
      method: "GET",
      url: "/api/data/age",
      success: function (data) {
        labels = data.labels;
        datas = data.data;
        setChart();
      },
      error: function (error_data) {
        console.log("error");
        console.log(error_data);
      },
    })

    function setChart() {
      var ctx = document.getElementById("myChart2").getContext("2d");
      var myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: label,
              data: datas,
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
               
                
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
               
              ],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      });
    }
  });

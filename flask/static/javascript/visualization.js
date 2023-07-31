/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Visualization page */
/* Last Update: Dylan Kayyem, 7/31/2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {
    // table 
    var table = document.getElementById('bloodTable');
    //table.style.border = "1px solid yellow";

    // Function to sort the table based on A+ units (column index 4)
    function sortTable(columnIndex) {
        var rows, switching, i, x, y, shouldSwitch;
        switching = true;
        while (switching) {
            switching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = parseFloat(rows[i].getElementsByTagName("td")[columnIndex].textContent);
                y = parseFloat(rows[i + 1].getElementsByTagName("td")[columnIndex].textContent);
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }
   
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(5)').addEventListener('click', function () {
        sortTable(4); // Column index 4 is for A+ units
        console.log('header 5 was clicked');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(6)').addEventListener('click', function () {
        sortTable(5); // Column index 5 is for B+ units
        console.log('header 6 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(7)').addEventListener('click', function () {
        sortTable(6); // Column index 6 is for AB+ units
        console.log('header 7 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(8)').addEventListener('click', function () {
        sortTable(7); // Column index 7 is for O+ units
        console.log('header 8 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(9)').addEventListener('click', function () {
        sortTable(8); // Column index 8 is for A- units
        console.log('header 9 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(10)').addEventListener('click', function () {
        sortTable(9); // Column index 9 is for B- units
        console.log('header 10 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(11)').addEventListener('click', function () {
        sortTable(10); // Column index 10 is for AB- units
        console.log('header 11 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(12)').addEventListener('click', function () {
        sortTable(11); // Column index 11 is for O- units
        console.log('header 12 was clicked ');
    });

    // pie chart
    var pieChartCanvas = document.getElementById('pieChart');
    var labels = pieChartCanvas.dataset.labels.split(',');
    var data = pieChartCanvas.dataset.data.split(',').map(Number);
    var ctx = pieChartCanvas.getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels, // Bloodtypes for labels
            datasets: [{
                data: data,
                backgroundColor: [
                    // 
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    // negative styles
                    'rgba(238, 130, 238, 0.6)',
                    'rgba(255, 0, 0, 0.6)',
                    'rgba(255, 165, 0, 0.6)',
                    'rgba(106, 90, 205, 0.6)'
               ],
               borderColor: [
                    // positive styles
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    // negative styles
                    'rgba(238, 130, 238, 1)',
                    'rgba(255, 0, 0, 1)',
                    'rgba(255, 165, 0, 1)',
                    'rgba(106, 90, 205, 1)'
               ],
               borderWidth: 1
           }]
       },
       options: {
           responsive: false, // Set to true if you want the chart to resize with the window
           legend: {
               display: true,
               position: 'right', // style for legend
           }
       }
   });
});
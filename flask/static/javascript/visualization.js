/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Visualization page */
/* Last Update: Dylan Kayyem, 8/3/2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {
    // table 
    var table = document.getElementById('bloodTable');
    // Function to sort the table based on A+ units (column index 4)
    function sortTable(columnIndex) {
        var tb = document.getElementById('bloodTable');
        var rows, switching, i, x, y, shouldSwitch;
        switching = true;
        while (switching) {
            switching = false;
            rows = tb.rows;
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
    function attachSortListeners() {
        var table = document.getElementById('bloodTable');
        if (table) {
          var headers = table.getElementsByTagName('th');
          for (let i = 0; i < headers.length; i++) {
            headers[i].addEventListener('click', function () {
              // Check if the column is currently removed
              if (currentlyRemovedColumns.indexOf(i) === -1) {
                sortTable(i);
              }
            });
          }
        }
      }
      
      // Call this function once your table is rendered
    attachSortListeners();
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(3)').addEventListener('click', function () {
        sortTable(3); // Column index 4 is for A+ units
        console.log('header 3 was clicked');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(4)').addEventListener('click', function () {
        sortTable(4); // Column index 4 is for A+ units
        console.log('header 4 was clicked');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(5)').addEventListener('click', function () {
        sortTable(5); // Column index 4 is for A+ units
        console.log('header 5 was clicked');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(6)').addEventListener('click', function () {
        sortTable(6); // Column index 5 is for B+ units
        console.log('header 6 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(7)').addEventListener('click', function () {
        sortTable(7); // Column index 6 is for AB+ units
        console.log('header 7 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(8)').addEventListener('click', function () {
        sortTable(8); // Column index 7 is for O+ units
        console.log('header 8 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(9)').addEventListener('click', function () {
        sortTable(9); // Column index 8 is for A- units
        console.log('header 9 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(10)').addEventListener('click', function () {
        sortTable(9); // Column index 9 is for B- units
        console.log('header 10 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(11)').addEventListener('click', function () {
        sortTable(11); // Column index 10 is for AB- units
        console.log('header 11 was clicked ');
    });
    // Attach the event listener to the header cell (th) element
    table.querySelector('thead tr th:nth-child(12)').addEventListener('click', function () {
        sortTable(12); // Column index 11 is for O- units
        console.log('header 12 was clicked ');
    });

    // pie chart
//     var pieChartCanvas = document.getElementById('pieChart');
//     var pie_labels = pieChartCanvas.dataset.labels.split(',');
//     var pie_data = pieChartCanvas.dataset.data.split(',').map(Number);
//     var pctx = pieChartCanvas.getContext('2d');
//     var myPieChart = new Chart(pctx, {
//         type: 'pie',
//         data: {
//             labels: pie_labels, // Bloodtypes for labels
//             datasets: [{
//                 data: pie_data,
//                 backgroundColor: [
//                     'rgba(255, 99, 132, 0.6)',
//                     'rgba(54, 162, 235, 0.6)',
//                     'rgba(255, 206, 86, 0.6)',
//                     'rgba(75, 192, 192, 0.6)',
//                     // negative styles
//                     'rgba(238, 130, 238, 0.6)',
//                     'rgba(255, 0, 0, 0.6)',
//                     'rgba(255, 165, 0, 0.6)',
//                     'rgba(106, 90, 205, 0.6)'
//                ],
//                borderColor: [
//                     // positive styles
//                     'rgba(255, 99, 132, 1)',
//                     'rgba(54, 162, 235, 1)',
//                     'rgba(255, 206, 86, 1)',
//                     'rgba(75, 192, 192, 1)',
//                     // negative styles
//                     'rgba(238, 130, 238, 1)',
//                     'rgba(255, 0, 0, 1)',
//                     'rgba(255, 165, 0, 1)',
//                     'rgba(106, 90, 205, 1)'
//                ],
//                borderWidth: 1
//            }]
//        },
//        options: {
//            responsive: false, // Set to true if you want the chart to resize with the window
//            legend: {
//                display: true,
//                position: 'right', // style for legend
//            }
//        }
//    });

    // Bar Graph 
    var barChartCanvas = document.getElementById('barChart');
    var ctx = barChartCanvas.getContext('2d');
    var bar_labels = barChartCanvas.dataset.labels.split(',');
    var bar_data = barChartCanvas.dataset.data.split(',').map(Number);
    let barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: bar_labels,
            datasets: [{
                
                data: bar_data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 2,
                borderSkipped: false,
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#777',
                        font: {
                            size: 14
                        }
                    },
                    grid: {
                        borderColor: '#ddd'
                    }
                },
                x: {
                    ticks: {
                        color: '#777',
                        font: {
                            size: 14
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    align: 'center',
                    position: 'bottom', 
                    text: 'Total Units of Blood Available'
                },
                legend: {
                    display: false,
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeInOutQuad'
            },
        }
    });
    let count = 0;
    let removedColumnsData  = [];
    let currentlyRemovedColumns = [];
    let allColumns = [4,5,6,7,8,9,10,11];
    let columnsToRemove = {
        "A+": [5,6,7,8,9,10,11],
        "B+": [4,6,7,8,9,10,11],
        "AB+": [4,5,7,8,9,10,11],
        "O+": [4,5,6,8,9,10,11],
        "A-": [4,5,6,7,9,10,11],
        "B-": [4,5,6,7,8,10,11],
        "AB-": [4,5,6,7,8,9,11],
        "O-": [4,5,6,7,8,9,10]
    };
      
    // Add a click event listener to the chart
    barChart.canvas.onclick = function (evt) {
        var activePoints = barChart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);

        if (activePoints.length) {
            var firstPoint = activePoints[0];
            var label = barChart.data.labels[firstPoint.index];
            var total_value = barChart.data.datasets[firstPoint.datasetIndex].data[firstPoint.index];
            
            function removeAndStoreColumns(tableId, columnIndices) {
                // First, restore any previously removed columns
                if (currentlyRemovedColumns.length > 0) {
                  restoreColumns(tableId, currentlyRemovedColumns);
                }
              
                const table = document.getElementById(tableId);
                if (table) {
                  for (let i = 0; i < table.rows.length; i++) {
                    const row = table.rows[i];
                    removedColumnsData[i] = [];
                    for (let j = columnIndices.length - 1; j >= 0; j--) {
                      if (row.cells.length > columnIndices[j]) {
                        // Store the text content of the cell
                        removedColumnsData[i][j] = row.cells[columnIndices[j]].textContent;
                        // Remove the cell
                        row.deleteCell(columnIndices[j]);
                      }
                    }
                  }
                  // Update the currently removed columns
                  currentlyRemovedColumns = columnIndices;
                }
            }
            function restoreColumns(tableId, columnIndices) {
                const table = document.getElementById(tableId);
                if (table && removedColumnsData.length > 0) {
                    for (let i = 0; i < table.rows.length; i++) {
                        const row = table.rows[i];
                        for (let j = 0; j < columnIndices.length; j++) {
                            // Create a new cell
                            const cell = row.insertCell(columnIndices[j]);
                            // Set the text content of the cell to the stored data
                            cell.textContent = removedColumnsData[i][j];
                        }
                    }
                    // Clear the stored data
                    removedColumnsData = [];
                }
            }
            function toggleColumns(label) {
                if (removedColumnsData[label]) {
                  // Restore the columns
                  restoreColumns('bloodTable', columnsToRemove[label]);
                  removedColumnsData[label] = false;
                } else {
                  // Remove the columns and store the data
                  removeAndStoreColumns('bloodTable', columnsToRemove[label]);
                  removedColumnsData[label] = true;
                }
            }
            // 
            if (label == "A+") {
                removeAndStoreColumns('bloodTable', [5,6,7,8,9,10,11]);
                sortTable(4);
                
            } 
            if (label == "B+" ) {
                removeAndStoreColumns('bloodTable', [4,6,7,8,9,10,11]); 
            } 
            
            if (label == "AB+") {
         
                removeAndStoreColumns('bloodTable', [4,5,7,8,9,10,11]); 
            }
            if (label == "O+") {

                removeAndStoreColumns('bloodTable', [4,5,6,8,9,10,11]); 
            }
            if (label == "A-") {

                removeAndStoreColumns('bloodTable', [4,5,6,7,9,10,11]); 
                
            }
            if (label == "B-") {

                removeAndStoreColumns('bloodTable', [4,5,6,7,8,10,11]); 
            }
            if (label == "AB-") {

                removeAndStoreColumns('bloodTable', [4,5,6,7,8,9,11]); 
                
            }
            if (label == "O-") {
                removeAndStoreColumns('bloodTable', [4,5,6,7,8,9,10]); 
                
                // Attach the event listener to the header cell (th) element
            }
        };
    };
    
});


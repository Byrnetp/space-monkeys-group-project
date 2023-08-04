/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Visualization page */
/* Last Update: Dylan Kayyem, 8/3/2023 */


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

/* remove and stores columns function */
function removeAndStoreColumns(tableId, columnIndices) {
    // First, restore any previously removed columns
    if (currentlyRemovedColumns.length > 0) {
      restoreColumns(tableId, currentlyRemovedColumns);
    }
    const table = document.getElementById(tableId);
    if (table) {
        removedColumnsData = [];
        // Store the header cells
        const headerRow = table.rows[0];
        removedColumnsData[0] = [];
        for (let j = columnIndices.length - 1; j >= 0; j--) {
            if (headerRow.cells.length > columnIndices[j]) {
                removedColumnsData[0][j] = headerRow.cells[columnIndices[j]].outerHTML;
                headerRow.deleteCell(columnIndices[j]);
            }
        }

        // Store the data cells
        for (let i = 1; i < table.rows.length; i++) {
            const row = table.rows[i];
            removedColumnsData[i] = [];
            for (let j = columnIndices.length - 1; j >= 0; j--) {
                if (row.cells.length > columnIndices[j]) {
                    removedColumnsData[i][j] = row.cells[columnIndices[j]].outerHTML;
                    row.deleteCell(columnIndices[j]);
                }
            }
        }
        // Update the currently removed columns
        currentlyRemovedColumns = columnIndices;
        attachTableHeaderListeners();
    }
}

/* restores columns function */
function restoreColumns(tableId, columnIndices) {
    const table = document.getElementById(tableId);
    if (table && removedColumnsData.length > 0) {
        // Restore the header cells
        const headerRow = table.rows[0];
        for (let j = 0; j < columnIndices.length; j++) {
            const cell = headerRow.insertCell(columnIndices[j]);
            cell.outerHTML = removedColumnsData[0][j];
        }

        // Restore the data cells
        for (let i = 1; i < table.rows.length; i++) {
            const row = table.rows[i];
            for (let j = 0; j < columnIndices.length; j++) {
                const cell = row.insertCell(columnIndices[j]);
                cell.outerHTML = removedColumnsData[i][j];
            }
        }
        // Clear the stored data
        removedColumnsData = [];
        // Re-attach the header listeners
        attachTableHeaderListeners();
        console.log('restored columns');
    }
}

function sortTable(tableId, columnIndex) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchCount = 0;
    table = document.getElementById(tableId);
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[columnIndex];
            y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
            if (x && y ) { // Check that x and y are defined
                if (dir === "asc") {
                    if (isNaN(x.innerHTML) || isNaN(y.innerHTML)) {
                        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    } else {
                        if (Number(x.innerHTML) > Number(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                } else if (dir === "desc") {
                    if (isNaN(x.innerHTML) || isNaN(y.innerHTML)) {
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    } else {
                        if (Number(x.innerHTML) < Number(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
            } 
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchCount++;
        } else {
            if (switchCount === 0 && dir === "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

// Function to attach click listeners to table headers
function attachTableHeaderListeners() {
    var table = document.getElementById('bloodTable');
    var headers = table.getElementsByTagName('th');
    for (var i = 0; i < headers.length; i++) {
        (function (index) {
            headers[index].addEventListener('click', function () {
                sortTable('bloodTable', index);
            });
        })(i);
    }
}

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {
    attachTableHeaderListeners();
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
    
    // Add a click event listener to the chart
    barChart.canvas.onclick = function (evt) {
        var activePoints = barChart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);
        if (activePoints.length) {
            var firstPoint = activePoints[0];
            var label = barChart.data.labels[firstPoint.index];
            if (label == "A+") {
                removeAndStoreColumns('bloodTable', [5,6,7,8,9,10,11]);
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
            }
        };
    };
});
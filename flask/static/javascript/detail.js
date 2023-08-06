// CS 3308 Group Project
// Team 2: Space Monkeys
// Main Flask driver code
// Last Update: Travis Byrne, 1 August 2023

// Get checkbox elements
let donCheck = document.getElementById("donations");
let xfusionCheck = document.getElementById("transfusions");
let xferInCheck = document.getElementById("incomingTransfers");
let  xferOutCheck = document.getElementById("outgoingTransfers");

// Get table elements
let donTable = document.getElementById("donationTable");
let xfusionTable = document.getElementById("transfusionTable");
let xferInTable = document.getElementById("incomingTransferTable");
let xferOutTable = document.getElementById("outgoingTransferTable");

// Event listeners to hide and display data tables based on their checkboxes
donCheck.addEventListener('change', ()=> {
    if (!donCheck.checked) {
        donTable.style = "display: none";
    } else {
        donTable.style = "display: block";
    }
});

xfusionCheck.addEventListener('change', ()=> {
    if (!xfusionCheck.checked) {
        xfusionTable.style = "display: none";
    } else {
        xfusionTable.style = "display: block";
    }
});

xferInCheck.addEventListener('change', ()=> {
    if (!xferInCheck.checked) {
        xferInTable.style = "display: none";
    } else {
        xferInTable.style = "display: block";
    }
});

xferOutCheck.addEventListener('change', ()=> {
    if (!xferOutCheck.checked) {
        xferOutTable.style = "display: none";
    } else {
        xferOutTable.style = "display: block";
    }
});

// Get hospital select element
let hospitalSelect = document.getElementById("hospital");

// When a hospital is selected, send an async request to get the data for that hospital
hospitalSelect.addEventListener('change', ()=> {

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            // Add the new tables to the tables container
            document.getElementById("tablesContainer").innerHTML = this.responseText

            // Get new table elements so that event listeners continue to work
            donTable = document.getElementById("donationTable");
            xfusionTable = document.getElementById("transfusionTable");
            xferInTable = document.getElementById("incomingTransferTable");
            xferOutTable = document.getElementById("outgoingTransferTable");

            // Hide any tables that need to be hidden again
            if (!donCheck.checked) {
                donTable.style = "display: none";
            }
            if (!xfusionCheck.checked) {
                xfusionTable.style = "display: none";
            }
            if (!xferInCheck.checked) {
                xferInTable.style = "display: none";
            }
            if (!xferOutCheck.checked) {
                xferOutTable.style = "display: none";
            }

    }
    };
    xhttp.open("GET", "detail/" + hospitalSelect.value, true);
    xhttp.send();
});
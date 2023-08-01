// Get checkbox elements
donCheck = document.getElementById("donations");
xfusionCheck = document.getElementById("transfusions");
xferCheck = document.getElementById("transfers");

// Get table elements
donTable = document.getElementById("donationTable");
xfusionTable = document.getElementById("transfusionTable");
xferTable = document.getElementById("transferTable");

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

xferCheck.addEventListener('change', ()=> {
    if (!xferCheck.checked) {
        xferTable.style = "display: none";
    } else {
        xferTable.style = "display: block";
    }
});
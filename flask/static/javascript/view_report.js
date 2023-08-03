// This page should use Transfusion_ID to display Comments and/or complication_ID on the page


// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

  // Function to execute on form submission
  var complicationReportForm = document.getElementById("complicationReportForm");
  complicationReportForm.addEventListener("submit", async (event) => {

    console.log("Submitting....")

    // Don't reload page on form submission
    event.preventDefault();

    // Check Transfusion ID for valid input
    var transfusionIDInput = document.getElementById("transfusionID");
    var transfusionIDValid = isDatalistEntryValid("transfusionIDChoices", transfusionIDInput.value);

    setFormStyle(transfusionIDValid, "transfusionID", "Transfusion ID:", "Please enter a valid Transfusion ID");

    // Check if form entry is valid
    if (transfusionIDValid) {

      // Submit form
        document.complicationReportForm.submit();
    }

    // If form data is invalid
    else {
      alert("Please ensure you have a valid selection for all fields!");
    }

  });
});

// Function to check if the datalist entry is valid
function isDatalistEntryValid(datalistName, choice) {

  // Get datalist
  var datalist = document.getElementById(datalistName);

  // Initialize flag variable
  var optionFound = false;

  // Determine whether an option exists with the current value of the input.
  for (var j = 0; j < datalist.options.length; j++) {
      if (choice == datalist.options[j].value) {
          optionFound = true;
          break;
      }
  }

  return optionFound;
}

// Function to set style of form input based on whether choice is valid or invalid
function setFormStyle(valid, labelName, labelText, labelHover) {
  var label = document.getElementById(labelName);
  if (valid) {
    label.style.color = "black";
    label.style.fontWeight = "normal";
    label.title = "";
  } else {
    label.style.color = "red";
    label.style.fontWeight = "bold";
    label.title = labelHover;
  }
}



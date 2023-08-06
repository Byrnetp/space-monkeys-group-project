// This page should use Transfusion_ID to append comments into the table and return a validation message

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

  // Function to execute on form submission
  var complicationReportForm = document.getElementById("complicationReportForm");
  complicationReportForm.addEventListener("submit", (event) => {

    // Don't reload page on form submission
    event.preventDefault();

    // Check Transfusion ID for valid input
    var transfusionIDInput = document.getElementById("transfusionID");
    var transfusionIDValid = isDatalistEntryValid("transfusionIDChoices", transfusionIDInput.value);
    
    // var isCommentEmpty = document.getElementById("Comments");

    
    setFormStyle(transfusionIDValid, "transfusionIDLabel", "Transfusion ID:", "Please enter a valid Transfusion ID");

    // Check Comments for valid input
    var commentInput = document.getElementById("comment");

      
    var commentValid = !isEntryEmpty(commentInput.value);
    setFormStyle(commentValid, "commentLabel", "Comment:", "Please enter a comment");

    // Check if all form entries are valid
    if (transfusionIDValid && commentValid) {
      alert("Report submitted successfully!");
      // Submit form
      document.complicationReportForm.submit();

      // Show success message (optional, only if you want to show it on the form)
      var successMessage = document.getElementById("successMessage");
      successMessage.style.display = "block";

      // Reset form values (optional)
      complicationReportForm.reset();
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

// Function to check if entry is empty
function isEntryEmpty(choice) {
  if (choice == "") {
    return true;
  }
  return false;
}

// Function to set style of form input based on whether choice is valid or invalid
function setFormStyle(valid, labelName, labelText, labelHover) {

  // Set style if Transfusion ID is valid
  var label = document.getElementById(labelName);
  if (valid) {
    label.innerHTML = labelText;
    label.style.color = "black";
    label.style.fontWeight = "normal";
    label.title = "";
  }

  // Set style if Transfusion ID is invalid
  else {
    label.innerHTML = "&#9888; " + labelText;
    label.style.color = "red";
    label.style.fontWeight = "bold";
    label.title = labelHover;
  }
}
// This page should use Transfusion_ID to display Comments and/or complication_ID on the page


// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

  // Function to execute on form submission
  var complicationReportForm = document.getElementById("complicationReportForm");
  complicationReportForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Check Transfusion ID for valid input
    var transfusionIDInput = document.getElementById("transfusionID");
    var transfusionIDValid = !isEntryEmpty(transfusionIDInput.value);

    setFormStyle(transfusionIDValid, "transfusionID", "Transfusion ID:", "Please enter a valid Transfusion ID");

    // Check if form entry is valid
    if (transfusionIDValid) {
      // Get the Complication ID from the form input
      var complicationID = parseInt(transfusionIDInput.value);

      // Make an API call to get comments and Complication ID for the given Complication ID
      try {
        var response = await fetch(`/view_complication?transfusionID=${complicationID}`);
        if (response.ok) {
          var data = await response.text(); // Assuming you're rendering the template directly

          var complicationIDDisplay = document.getElementById("transfusionIDData");
          var commentsDisplay = document.getElementById("commentsDisplay");

          if (data) {
            // Assuming the fetched data is directly rendered within the HTML
            complicationIDDisplay.innerHTML = data;
            commentsDisplay.innerHTML = data;
          } else {
            complicationIDDisplay.textContent = "Complication ID not found for transfusion " + complicationID;
            commentsDisplay.textContent = "No comments available";
          }
        } else {
          console.error("Error fetching comments:", response.statusText);
          alert("Error fetching comments. Please try again later.");
        }
      } catch (error) {
        console.error("Error fetching comments:", error);
        alert("Error fetching comments. Please try again later.");
      }
    }

    // If form data is invalid
    else {
      alert("Please ensure you have a valid selection for all fields!");
    }

  });
});
// Function to check if entry is empty
function isEntryEmpty(choice) {
  if (choice == "") {
    return true;
  }
  return false;
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



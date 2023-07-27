/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Patient Entry page */
/* Last Update: David Hughes, 26 July 2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

    // Function to execute on form submission
    var patientEntryForm = document.getElementById("patientEntryForm");
    patientEntryForm.addEventListener("submit", (event) => {

      // Don't reload page on form submission
      event.preventDefault();
    
      // Check blood bank name for valid input
      var patientNameInput = document.getElementById("patientName");
      var patientNameValid = !isEntryEmpty(patientNameInput.value);
      setFormStyle(patientNameValid, "patientNameLabel", "Patient Name:", "Please enter a valid patient name");

      // Check blood type for valid input
      var patientBloodTypeInput = document.getElementById("patientBloodType");
      var patientBloodTypeValid = !isEntryEmpty(patientBloodTypeInput.value);
      setFormStyle(patientBloodTypeValid, "patientBloodTypeLabel", "Patient Blood Type:", "Please choose a blood type");

      // Check if all form entries are valid
      if (patientNameValid && patientBloodTypeValid) {
        
        // Submit form
        document.patientEntryForm.submit();
        alert("This form has been successfully submitted!");
        
        // Reset form values
        patientNameInput.value = "";
        patientBloodTypeInput.value = "";
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

      // Set style if patient name is valid
      var label = document.getElementById(labelName);
      if (valid) {
        label.innerHTML = labelText;
        label.style.color = "black";
        label.style.fontWeight = "normal";
        label.title = "";
      }

      // Set style if patient name is invalid
      else {
        label.innerHTML = "&#9888; " + labelText;
        label.style.color = "red";
        label.style.fontWeight = "bold";
        label.title = labelHover;
      }
}
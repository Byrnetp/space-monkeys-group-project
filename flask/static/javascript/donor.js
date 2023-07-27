/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Donor Entry page */
/* Last Update: David Hughes, 26 July 2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

    // Function to execute on form submission
    var donorEntryForm = document.getElementById("donorEntryForm");
    donorEntryForm.addEventListener("submit", (event) => {

      // Don't reload page on form submission
      event.preventDefault();
    
      // Check blood bank name for valid input
      var donorNameInput = document.getElementById("donorName");
      var donorNameValid = !isEntryEmpty(donorNameInput.value);
      setFormStyle(donorNameValid, "donorNameLabel", "Donor Name:", "Please enter a valid donor name");

      // Check blood type for valid input
      var donorBloodTypeInput = document.getElementById("donorBloodType");
      var donorBloodTypeValid = !isEntryEmpty(donorBloodTypeInput.value);
      setFormStyle(donorBloodTypeValid, "donorBloodTypeLabel", "Donor Blood Type:", "Please choose a blood type");

      // Check if all form entries are valid
      if (donorNameValid && donorBloodTypeValid) {
        
        // Submit form
        document.donorEntryForm.submit();
        alert("This form has been successfully submitted!");
        
        // Reset form values
        donorNameInput.value = "";
        donorBloodTypeInput.value = "";
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

      // Set style if donor name is valid
      var label = document.getElementById(labelName);
      if (valid) {
        label.innerHTML = labelText;
        label.style.color = "black";
        label.style.fontWeight = "normal";
        label.title = "";
      }

      // Set style if donor name is invalid
      else {
        label.innerHTML = "&#9888; " + labelText;
        label.style.color = "red";
        label.style.fontWeight = "bold";
        label.title = labelHover;
      }
}
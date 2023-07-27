/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Blood Bank Entry page */
/* Last Update: David Hughes, 26 July 2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

    // Function to execute on form submission
    var bloodbankEntryForm = document.getElementById("bloodbankEntryForm");
    bloodbankEntryForm.addEventListener("submit", (event) => {

      // Don't reload page on form submission
      event.preventDefault();
    
      // Check blood bank name for valid input
      var bloodbankNameInput = document.getElementById("bloodbankName");
      var bloodbankNameValid = !isEntryEmpty(bloodbankNameInput.value);
      setFormStyle(bloodbankNameValid, "bloodbankNameLabel", "Blood Bank Name:", "Please enter a valid blood bank name");

      // Check blood bank type for valid input
      var bloodbankTypeInput = document.getElementById("bloodbankType");
      var bloodbankTypeValid = !isEntryEmpty(bloodbankTypeInput.value);
      setFormStyle(bloodbankTypeValid, "bloodbankTypeLabel", "Blood Bank Type:", "Please enter a valid blood bank type");

      // Check blood bank city for valid input
      var bloodbankCityInput = document.getElementById("bloodbankCity");
      var bloodbankCityValid = !isEntryEmpty(bloodbankCityInput.value);
      setFormStyle(bloodbankCityValid, "bloodbankCityLabel", "Blood Bank City:", "Please enter a valid blood bank city");

      // Check blood bank state for valid input
      var bloodbankStateInput = document.getElementById("bloodbankState");
      var bloodbankStateValid = !isEntryEmpty(bloodbankStateInput.value);
      setFormStyle(bloodbankStateValid, "bloodbankStateLabel", "Blood Bank State:", "Please enter a valid blood bank state");

      // Check if all form entries are valid
      if (bloodbankNameValid && bloodbankTypeValid && bloodbankCityValid && bloodbankStateValid) {
        
        // Submit form
        document.bloodbankEntryForm.submit();
        alert("This form has been successfully submitted!");
        
        // Reset form values
        bloodbankNameInput.value = "";
        bloodbankTypeInput.value = "";
        bloodbankCityInput.value = "";
        bloodbankStateInput.value = "";
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

      // Set style if bloodbank name is valid
      var label = document.getElementById(labelName);
      if (valid) {
        label.innerHTML = labelText;
        label.style.color = "black";
        label.style.fontWeight = "normal";
        label.title = "";
      }

      // Set style if bloodbank name is invalid
      else {
        label.innerHTML = "&#9888; " + labelText;
        label.style.color = "red";
        label.style.fontWeight = "bold";
        label.title = labelHover;
      }
}
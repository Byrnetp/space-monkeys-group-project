/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Blood Bank Donation Entry page */
/* Last Update: David Hughes, 5 August 2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

    // Function to execute on form submission
    var donationEntryForm = document.getElementById("donationEntryForm");
    donationEntryForm.addEventListener("submit", (event) => {

      // Don't reload page on form submission
      event.preventDefault();
    
      // Check donor name for valid input
      var donorNameInput = document.getElementById("donorName");
      var donorNameValid = isDatalistEntryValid("donorNameChoices", donorNameInput.value);
      setFormStyle(donorNameValid, "donorNameLabel", "Donor Name:", "Please enter a valid donor name");

      // Check blood bank name for valid input
      var bloodBankNameInput = document.getElementById("bloodBankName");
      var bloodBankNameValid = isDatalistEntryValid("bloodBankNameChoices", bloodBankNameInput.value);
      setFormStyle(bloodBankNameValid, "bloodBankNameLabel", "Blood Bank Name:", "Please enter a valid blood bank name");

      // Check medical professional for valid input
      var medicalProfessionalInput = document.getElementById("medicalProfessional");
      var medicalProfessionalValid = !isEntryEmpty(medicalProfessionalInput.value);
      setFormStyle(medicalProfessionalValid, "medicalProfessionalLabel", "Medical Professional:", "Please enter a medical professional");

      // Check quantity for valid input
      var quantityInput = document.getElementById("quantity");
      var quantityValid = !isEntryEmpty(quantityInput.value);
      setFormStyle(quantityValid, "quantityLabel", "Quantity (Units):", "Please choose a valid quantity");

      // Check quantity for valid input
      var dateInput = document.getElementById("date");
      var dateValid = !isEntryEmpty(dateInput.value);
      setFormStyle(dateValid, "dateLabel", "Date of Donation:", "Please choose a valid date");
    
      // Check if all form entries are valid
      if (donorNameValid && bloodBankNameValid && medicalProfessionalValid && quantityValid && dateValid) {
        
        // Submit form
        document.donationEntryForm.submit();
        alert("This form has been successfully submitted!");
        
        // Reset form values
        donorNameInput.value = "";
        bloodBankNameInput.value = "";
        medicalProfessionalInput.value = "";
        quantityInput.value = "";
        dateInput.value = "";
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
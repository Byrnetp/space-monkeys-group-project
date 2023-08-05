/* CS 3308 Group Project */
/* Team 2: Space Monkeys */
/* Javascript for Blood Transfer Entry page */
/* Last Update: Michael Becker, 29 July 2023 */

// Wait until document is loaded before doing anything
document.addEventListener('DOMContentLoaded', function () {

    // Function to execute on form submission
    var TransferEntryForm = document.getElementById("TransferEntryForm");
    TransferEntryForm.addEventListener("submit", (event) => {

      // Don't reload page on form submission
      event.preventDefault();
    
      // Check Donaltion ID for valid input
      var DonationIDInput = document.getElementById("DonationID");
      var DonationIDValid = isDatalistEntryValid("donationIDChoices", DonationIDInput.value);
      setFormStyle(DonationIDValid, "DonationIDLabel", "Donation ID:", "Please enter a valid Donation ID");

      // Check Receiving Hospital ID for valid input
      var ReceivingHospitalIDInput = document.getElementById("ReceivingHospitalID");
      var ReceivingHospitalIDValid = isDatalistEntryValid("ReceivingHospitalIDChoices", ReceivingHospitalIDInput.value);
      setFormStyle(ReceivingHospitalIDValid, "ReceivingHospitalIDLabel", "Receiving Hospital ID:", "Please enter a valid Receiving Hospital ID");

      // Check Sending Hospital ID for valid input
      var SendingHospitalIDInput = document.getElementById("SendingHospitalID");
      var SendingHospitalIDValid = isDatalistEntryValid("SendingHospitalIDChoices", SendingHospitalIDInput.value);
      setFormStyle(SendingHospitalIDValid, "SendingHospitalIDLabel", "Sending Hospital ID:", "Please enter a valid Sending Hospital ID");

      // Check if all form entries are valid
      if (DonationIDValid && ReceivingHospitalIDValid && SendingHospitalIDValid) {
        
        // Submit form
        document.TransferEntryForm.submit();
        alert("This form has been successfully submitted!");
        
        // Reset form values
        DonationIDInput.value = "";
        ReceivingHospitalIDInput.value = "";
        SendingHospitalIDInput.value = "";
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
        
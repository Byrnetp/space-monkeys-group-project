## CSPB 3308 Project Ideas

### Vision Statement:
Blood is meant for circulation!

The vision of the Space Monkeys is to create a blood bank management application with the goal of safely providing as many patients as possible with clean, unexpired, compatible blood so that they have the best chance of a positive health outcome if they need a blood transfusion.

### Services 

•	When a blood donation is made, record information about the donation (date, quantity) and donor (name, contact information, blood type).

•	When a blood transfusion is made, record information about the transfusion (date, quantity) and patient (name, contact information, blood type).

•	Determine how much of each type of blood a given blood bank has on hand.

•	Given a patient with need for blood, run a query to return the compatible, unexpired units of blood at the blood bank in order to match the patient with available blood. The output could either be all of the valid units or a subset of the valid units.

•	If there is a shortage of a certain type of blood, run a query to determine the eligible donors of that blood type to retrieve their contact information and send out a targeted appeal for blood donations.

•	If there is a patient who has experienced medical complications after receiving a blood transfusion, run a query to determine which other patients have received blood from the same donor to see if any of those patients have also experienced the same complications, to see if there might be an issue with the blood from that donor.

•	If a hospital needs a certain amount/type of blood, they can request it from another hospital.

### Interfaces 

•	Blood Inventory Levels

•	Blood Details

•	Blood Request from Another Hospital Checkout

### Data 

- Blood Banks  
    - ID
    - Name
    - Address
    - Phone
    - Stock of Each Type of Blood
    
<br>

- Donors  
    - ID
    - Name
    - Address
    - Phone
    - Blood Type
    - Diagnosis
    
<br>

- Patients  
    - ID
    - Name
    - Address
    - Phone
    - Blood Type
    
<br>

- Donations
    - Donation ID
    - Donor ID
    - Blood Bank ID
    - Quantity
    - Date
    
<br>

- Transfusions
    - Transfusion ID
    - Patient ID
    - Blood Bank ID
    - Quantity
    - Date
    
<br>

### User Stories

•



---
## Project Guidelines

### Three Key Features:

Recommended to have at least __three key features__ for our main project proposal.

1. (...Insert a description of feature 1 here...)

2. (...Insert a description of feature 2 here...)

3. (...Insert a description of feature 3 here...)


### "Nice-to-have" Features: 

These features are not vital or necessary, and should only be implemented if primary key features are working. 

1. Ecommerce Feature - Adding ecommerce functionality that could utilize an already created key feature or simply be an addition of its own. 

	- For example, it could be for a non-patient users. An admin (non-patient) user could be a hospital or any accredited medical group looking for available blood for specific patients/types. 

2. Blood Inventory Levels - Data visualization of data; up to date, real time, estimates of blood inventories in the nearby area compared to the greater state/country/nation/etc. 

	- Private vs public access may be an issue depending on insurance coverage, etc. 

3. Blood Details - Could be added to the above feature if it's a basic interface... 

	- Or another example of a feature could be an interactive/animated feature where a user could learn more about the types of blood while waiting for their blood.

4. Blood Details - Another type of feature is to incorporates "...the query to return compatible blood, a history of the donor’s success rate with receiving compatible blood, and access to reported complications (as well as the ability to report an issue with the blood from that donor)"...  and if severe enough, the feature could then contact your health care provider. 

5. Blood Request from Another Hospital Checkout 



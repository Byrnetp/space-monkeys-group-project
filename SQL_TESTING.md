# CSPB 3308
# Group 2 - Space Monkeys
# Project Deliverable 5 - SQL Design

## <b>Database Architecture</b>

### <u>Table: Bloodbanks_and_Hospitals</u>

#### Table Description
- This page houses all of the information for each institution whether it is a blood bank, a hospital, or another health care institution in the Space Monkeys network. The PRIMARY KEY is the Institution_ID which is unique for each institution.

#### Field names and short description
Institution_ID 
- This field is the PRIMARY KEY and of INT type.  It specifies the number for each unique institution to uniquely identify each institution.

Type 
- This field is of VARCHAR(45) type.  It specifies the type of institution: Blood Bank, Hospital, etc.

Name 
- This field is of VARCHAR(90) type.  It specifies the name of the institution.

City 
- This field is of VARCHAR(45) type.  It specifies the city the institution is located in.

State 
- This field is of VARCHAR(2) type.  It specifies the state the institution is located in.

A_Positive_Units 
- This field is of INT type.  It specifies the units of A+ blood type at the institution.

A_Negative_Units 
- This field is of INT type.  It specifies the units of A- blood type at the institution.

B_Positive_Units 
- This field is of INT type.  It specifies the units of B+ blood type at the institution.

B_Negative_Units 
- This field is of INT type.  It specifies the units of B- blood type at the institution.

AB_Positive_Units 
- This field is of INT type.  It specifies the units of AB+ blood type at the institution.

AB_Negative_Units 
- This field is of INT type.  It specifies the units of AB- blood type at the institution.

O_Positive_Units 
- This field is of INT type.  It specifies the units of O+ blood type at the institution.

O_Negative_Units 
- This field is of INT type.  It specifies the units of O- blood type at the institution.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Bloodbanks_and_Hospitals table is if ('''SELECT * FROM Bloodbanks_and_Hospitals WHERE Institution_ID = 64;''') == (64, 'Hospital', 'Yuma County', 'Wray', 'CO', 76650, 13526, 2500, 441, 7300, 1000, 11000, 1941) which resulted in "First Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Donor</u>

#### Table Description
- This page houses all of the information for each blood donor in the Space Monkeys network. The PRIMARY KEY is the Donor_ID which is unique for each blood donor.

#### Field names and short description
Donor_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood donor in the network.  It is the PRIMARY KEY.

Name 
- This field is of VARCHAR(90) type.  It specifies the name of the blood donor.

Blood_Type 
- This field is of VARCHAR(2) type.  It specifies the blood type of the blood donor.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Donor table is if ('''SELECT * FROM Donor WHERE Donor_ID = 22;''') == (22, 'Steve Rogers', 'B-') which resulted in "Second Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Patient</u>

#### Table Description
- This page houses all of the information for each patient in the network who will/has received a blood transfusion at an institution in the Space Monkeys network. The PRIMARY KEY is the Patient_ID which is unique for each patient.

#### Field names and short description
Patient_ID 
- This field is of INT type.  It specifies the unique number assigned to each patient receiving blood in the network. It is the PRIMARY KEY.

Name 
- This field is of VARCHAR(90) type.  It specifies the name of the patient receiving blood.

Blood_Type 
- This field is of VARCHAR(2) type.  It specifies the blood type of the patient receiving blood.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Patient table is if ('''SELECT * FROM Patient WHERE Patient_ID = 26;''') == (26, 'Zena Zootopia', 'O+') which resulted in "Third Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Donation</u>

#### Table Description
- This page houses all of the information for each donation that takes place at an institution in the Space Monkeys network. The PRIMARY KEY is the Donation_ID which is unique for each blood donation.  The field Donor_ID is a FOREIGN KEY with the Donor_ID field from the Donor Table.  The field Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

#### Field names and short description
Donation_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood donation. It is the PRIMARY KEY.

Date_Time 
- This field is of DATETIME type.  It specifies the date and time which the blood donation takes place.

Donor_ID 
- This field is of INT type.  It specifies the blood donor of the donation. It is a FOREIGN KEY.

Medical_Professional 
- This field is of VARCHAR(90) type.  It specifies the doctor responsible for signing off for a completed donation for approval.

Hospital_ID 
- This field is of INT type.  It specifies the institution which the blood donation takes place.  It is a FOREIGN KEY.

Amount 
- This field is of INT type.  It specifies the units of blood donated.  Each donation will be 1 unit.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Donation table is if ('''SELECT * FROM Donation WHERE Donation_ID = 42;''') == (42, '20230711 9:00:00', 22, 'Dr. Stephan Strange', 23, 1) which resulted in "Fourth Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Transfusion</u>

#### Table Description
- This page houses all of the information for each blood transfusion that occurs at an institution in the Space Monkeys network. The PRIMARY KEY is the Transfusion_ID which is unique for each blood transfusion. The field Donation_ID is a FOREIGN KEY with the Donation_ID field from the Donation Table.  The field Patient_ID is a FOREIGN KEY with the Patient_ID field from the Patient Table.  The field Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

#### Field names and short description
Transfusion_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood transfusion. It is the PRIMARY KEY.

Date_Time 
- This field is of DATETIME type.  It specifies the date and time which the blood transfusion takes place.

Donation_ID 
- This field is of INT type.  It specifies the individual who donated the blood for the transfusion.  It is a FOREIGN KEY.

Patient_ID 
- This field is of INT type.  It specifies the individual receiving the blood for the transfusion.  It is a FOREIGN KEY.

Medical_Professional 
- This field is of VARCHAR(90) type.  It specifies the doctor responsible for signing off for a completed transfusion for approval.

Hospital_ID 
- This field is of INT type.  It specifies the institution which the blood transfusion takes place.  It is a FOREIGN KEY.

Amount 
- This field is of INT type.  It specifies the units of blood in the transfusion.  Each transfusion will be 1 unit.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Transfusion table is if ('''SELECT * FROM Transfusion WHERE Transfusion_ID = 4;''') == (4, '20230723 11:00:00', 4, 23, 'Dr. Harleen Quinzel', 61, 1) which resulted in "Fifth Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Transfer</u>

#### Table Description
- This page houses all of the information for each blood transfer that occurs between two institutions in the Space Monkeys network. The PRIMARY KEY is the Transfer_ID which is unique for each blood transfer.  The field Donation_ID is a FOREIGN KEY with the Donation_ID field from the Donation Table.  The field Sending_Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.  The field Receiving_Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

#### Field names and short description
Transfer_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood transfer. It is the PRIMARY KEY. 

Date_Time 
- This field is of DATETIME type.  It specifies the date and time which the blood transfer takes place.

Donation_ID 
- This field is of INT type.  It specifies the individual who donated the blood for the transfer.  It is a FOREIGN KEY.

Receiving_Hospital_ID 
- This field is of INT type.  It specifies the institution which will receive the blood from the blood transfer.  It is a FOREIGN KEY.

Sending_Hospital_ID 
- This field is of INT type.  It specifies the institution which will send the blood from the blood transfer.  It is a FOREIGN KEY.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Transfer table is if ('''SELECT * FROM Transfer WHERE Transfer_ID = 4;''') == (4, '20230704 11:00:00', 28, 37, 17) which resulted in "Sixth Test Passed!" when the "sm_dbAPI.py" file executed.

### <u>Table: Complication</u>

#### Table Description
- This page houses all of the information for each complication from a blood transfusion that is reported. The PRIMARY KEY is the Complication_ID which is unique for each complication.  The field Transfusion_ID is a FOREIGN KEY with the Transfusion_ID field from the Transfusion Table.

#### Field names and short description
Complication_ID 
- This field is of INT type.  It specifies the unique number assigned to each complication. It is the PRIMARY KEY. 

Transfusion_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood transfusion.  It is a FOREIGN KEY.

Comments 
- This field is of VARCHAR(180) type.  It specifies the complications that the patient is having from the blood transfusion.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_monkeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Complication table is if ('''SELECT * FROM Complication WHERE Complication_ID = 1;''') == (1, 4, 'Throwing up multiple times a day') which resulted in "Seventh Test Passed!" and "All Tests Passed!!!" when the "sm_dbAPI.py" file executed.

## <b>Data Access Methods and How Exactly Each of the Pages Behaves with these Methods</b>

### <u>About Page</u>

#### Eligibility Checks

Use case name:

    Verify page links you to information about blood donation eligibility.

Description:

    Test the About page.

Pre-conditions (what needs to be true about the system before the test can be applied):

    User has a valid username and password, and has auto-sign on. 

Test steps:

    1. Navigate to about page.

    2. Scroll through bullet points.

    3. Click on drop down menus.

Expected result:

    User should see more information about blood donations and other resources. 

Actual result:

    User is navigated to About page with information concerning donors eligibility.

Status (Pass/Fail, when this test was performed)

    N/A

Notes:

    N/A

Post-conditions (what must be true about the system when the test has completed successfully):

    N/A

### <u>Blood Donation Entry Page</u>

### <u>Blood Transfusion Entry Page</u>

### <u>Blood Transfer Page</u>
#### Blood unit viewing by clicking button
Use case name : 
    Verify blood unit viewing
Description:
    Test if the enter button/link correctly retrieves Bloodbanks_and_Hospitals Table for the blood type specified in the input box
Pre-conditions (what needs to be true about the system before the test can be applied):
    Blood type entered needs to be field in Bloodbanks_and_Hospitals Table 
Test steps:
    1. Navigate to login page
    2. Navigate to Donations, Transfusions, and Transfers
    3. Enter blood type
    4. Click enter button
Expected result:
    User should see amount of units available for specified blood type at each instituion in Space Monkeys network.
Actual result (when you are testing this, how can you tell it worked):
    User sees table view
Status (Pass/Fail, when this test was performed)
    N/A
Notes:
    N/A
Post-conditions (what must be true about the system when the test has completed successfully):
    User can see blood that can be potentially transferred to their instituion 
    
#### Request blood to be transferred by clicking button
Use case name : 
    Verify blood units request
Description:
    Test if the request button/link correctly requests blood from a hospital
Pre-conditions (what needs to be true about the system before the test can be applied):
    Donation_ID, Receiving Hospital, and Sending Hospital entered needs to be field in Donation and Bloodbanks_and_Hospitals Tables
Test steps:
    1. Navigate to login page
    2. Navigate to Donations, Transfusions, and Transfers
    3. Enter Donation_ID, Receiving Hospital, and Sending Hospital 
    4. Click request button
Expected result:
    Bloodbanks_and_Hospitals should update based on requested amounts
Actual result (when you are testing this, how can you tell it worked):
    Bloodbanks_and_Hospitals should show amount changes
Status (Pass/Fail, when this test was performed)
    N/A
Notes:
    N/A
Post-conditions (what must be true about the system when the test has completed successfully):
    Bloodbanks_and_Hospitals should be updated

### <u>Donor Page</u>

#### Donor Table Display
Use case name: 

Test the Donor Table

Description:

Verify Donor Table is able to be correctly displayed on the donor page 

Pre-conditions (what needs to be true about the system before the test can be applied):

Donor data must be entered into the database.

Test steps:

1. Navigate to the donor page
2. Ensure that the Donors data is displayed

Expected result:

User should be able to view Donor data

Actual result (when you are testing this, how can you tell it worked):

User should see Donor data displayed in a table 

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

All data for Donors that exist in the Donor table in the database must be visible

<hr>

#### Add a donor to the database
Use case name:

Verify donor table update in the database

Description:

Test if the add donor button correctly updates the donor table in the database

Pre-conditions (what needs to be true about the system before the test can be applied):

Donor_ID, Name, and Blood_Type needs to be entered into the form on the donor page

Test steps:

1. Navigate to donor page
2. Enter Donor_ID, Name, and Blood_Type into the form elements
3. Click add donor button

Expected result:

Donor table should update with the data entered into the form

Actual result (when you are testing this, how can you tell it worked):

Check the database to ensure that the donor data was entered

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

Donor table should be updated


### <u>Patient Page</u>

#### Patient Table Display
Use case name: 

Test the Patient Table

Description:

Verify Patient Table is able to be correctly displayed on the patient page 

Pre-conditions (what needs to be true about the system before the test can be applied):

The patient table in the database must contain patient data for at least one patient

Test steps:

1. Navigate to patient page
2. Ensure that patient data is displayed correctly

Expected result:

User should be able to view patient data

Actual result (when you are testing this, how can you tell it worked):

User should see patient data displayed in a table 

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

All data for patients that exist in the Patient table in the database must be visible

<hr>

#### Add a patient to the database
Use case name:

Verify patient table update in the database

Description:

Test if the add patient button correctly updates the patient table in the database

Pre-conditions (what needs to be true about the system before the test can be applied):

Patient_ID, Name, and Blood_Type needs to be entered into the form on the patient page

Test steps:

1. Navigate to patient page
2. Enter Patient_ID, Name, and Blood_Type into the form elements
3. Click add patient button

Expected result:

Patient table should update with the data entered into the form

Actual result (when you are testing this, how can you tell it worked):

Check the database to ensure that the patient data was entered

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

Patient table should be updated


### <u>Blood Levels and Visualization Page</u>

#### Table Display

Use case name:

    Verify correct data from table is displayed on Blood Levels Page.

Description:

    Test the Bloodbank and Hospitals table.

Pre-conditions (what needs to be true about the system before the test can be applied):

    Valid bloodbanks and hospitals table must be retrievable from the database.

Test steps:

    1. Navigate to Blood Levels & Visualization page.

Expected result:

    User should be able to see all blood levels

Actual result:

    User should see table of each hospital/bloodbanks current levels of blood.

Status (Pass/Fail, when this test was performed)

    Pass

Notes:

    N/A

Post-conditions (what must be true about the system when the test has completed successfully):

    All data for hospitals and bloodbanks must be valid and have a value for each blood type.

#### Visual Display

Use case name:

    Verify the data from table is displayed appropriately on the pie graph.

Description:

    Test the Bloodbank and Hospitals pie graph.

Pre-conditions (what needs to be true about the system before the test can be applied):

    Valid bloodbanks and hospitals table must be retrievable from the database.

Test steps:

    1. Navigate to Blood Levels & Visualization page.
    2. Verify data is appropriately displayed in both table and graph.

Expected result:

    User should be able to see two models that represent all blood levels.


Actual result:

    User is navigated to a visualization of all blood data in the space monkey's bloodbank.

Status (Pass/Fail, when this test was performed)

    Pass

Notes:

    N/A

Post-conditions (what must be true about the system when the test has completed successfully):

    All data for hospitals and bloodbanks must be valid and have a value for each blood type, represented in the table and pie graph.


### <u>Blood Details Page</u>

#### Donation Table Display
Use case name: 

Test the Donation Table

Description:

Verify Donation Table is able to be correctly displayed on the details page

Pre-conditions (what needs to be true about the system before the test can be applied):

A valid hospital with Donation data must be selected on the page, Display: Donations checkbox must be checked

Test steps:

1. Navigate to details page
2. Choose a hospital
3. Ensure that the Donations checkbox is displayed

Expected result:

User should be able to view Donations of the selected hospital

Actual result (when you are testing this, how can you tell it worked):

User should see Donation data displayed when a hospital is chosen and the Display: Donations checkbox is active

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

All data for Donations that exist in the Donation table in the database must be visible for the selected hospital

<hr>

#### Transfusion Table Display
Use case name: 

Test the Transfusion Table

Description:

Verify Transfusion Table is able to be correctly displayed on the details page

Pre-conditions (what needs to be true about the system before the test can be applied):

A valid hospital with Transfusion data must be selected on the page, Display: Transfusions checkbox must be checked

Test steps:

1. Navigate to details page
2. Choose a hospital
3. Ensure that the Transfusions checkbox is displayed

Expected result:

User should be able to view Transfusions of the selected hospital

Actual result (when you are testing this, how can you tell it worked):

User should see Transfusion data displayed when a hospital is chosen and the Display: Transfusions checkbox is active

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

All data for Transfusions that exist in the Transfusion table in the database must be visible for the selected hospital

<hr>

#### Transfer Table Display
Use case name: 

Test the Transfer Table

Description:

Verify Transfer Table is able to be correctly displayed on the details page

Pre-conditions (what needs to be true about the system before the test can be applied):

A valid hospital with Transfer data must be selected on the page, Display: Transfers checkbox must be checked

Test steps:

1. Navigate to details page
2. Choose a hospital
3. Ensure that the Transfers checkbox is displayed

Expected result:

User should be able to view Transfers of the selected hospital

Actual result (when you are testing this, how can you tell it worked):

User should see Transfer data displayed when a hospital is chosen and the Display: Transfers checkbox is active

Status (Pass/Fail, when this test was performed):

N/A

Notes:

N/A

Post-conditions (what must be true about the system when the test has completed successfully):

All data for Transfers that exist in the Transfer table in the database must be visible for the selected hospital

### <u>Report Complications Page</u>
#### Table Description
Use case name:
    Complication Table

Description:
    The complication table stores the Transfusion_ID, Complication_ID and Comments about a transfusion. A person can search 
the data about a certain transfusion and add a complication report (Comments) about that patient or problems related to the transfusion and its attributes (blood type, amount, patient, etc). 

#### Field names and short description

Complication_ID:
- This is of INT type ,ad it is the primary key for this table. It specifies the unique number assigned to each complication report.

Transfusion_ID:
- This field is of INT type.  It specifies the unique number assigned to each blood transfusion. It is the FOREIGN KEY.

Comments:
- This field is of VARCHAR(180) type.  It specifies the possible complications that the patient is having from the blood transfusion.


#### Test to verify each table
 1. Navigate to Complication Report page
 2. Search for the transfusion_ID
 3. Make sure the checkbox is displayed
 4. Check if transfusion_ID input exist
 5. Check if submitting 'Comment' works and display a message ("New Comment added!")
 6. Check if the table has the new data

Expected result:

User should be able to find the transfusion
User should be able to see a confirmation message about the new data added

Status (Pass/Fail, when this test was performed):
N/A

Notes:
N/A

Post-conditions (what must be true about the system when the test has completed successfully):
The new data (Comments) should be able to be viewed in the 'Report Complications Page'.


### <u>View Complication Reports Page</u>

#### Table Description
Use case name:
    Complication Table
    Transfusion Table
    

Description:
    The View Complication Reports Page uses 2 functions to fetch data from the 'Transfusion Table' where a user can search a complication report using the 'Transfusion_ID' key to access the 'Comments'. Other informations would be displayed (Hospital_ID, Amount, Patient_ID, etc) fetching the data from Transfusion Table using the 'Transfusion_ID'.
    
#### Test to verify each table
 1. Navigate to View Complication Report page
 2. Search for the transfusion_ID
 3. Make sure the checkbox is displayed
 4. Check if transfusion_ID input exist in the Complication Table
 5. Check if transfusion_ID input exist in the Transfusion Table
 5. Check if the output boxes are displaying the correct values

Patient_ID:
- This field is of INT type.  It specifies the individual receiving the blood for the transfusion.  It is a FOREIGN KEY.

Amount:
- This field is of INT type.  It specifies the units of blood in the transfusion.  Each transfusion will be 1 unit.

Blood type:
- This field is of VARCHAR(2) type.  It specifies the blood type of the patient receiving blood. A_Positive_Units INT, A_Negative_Units INT, B_Positive_Units INT, B_Negative_Units INT, AB_Positive_Units INT, AB_Negative_Units INT, O_Positive_Units INT, O_Negative_Units INT.

Blood Bank ID:
- Institution_ID INT. It is a FOREIGN KEY. It specifies the institution which the blood donation takes place.  

Date_TIME:
- Date_Time DATETIME

Comments:
- This field is of VARCHAR(180) type.  It specifies the possible complications that the patient is having from the blood transfusion.

Donor_ID:
- This field is of INT type.  It specifies the blood donor of the donation. It is a FOREIGN KEY.

Transfusion_ID:
- This field is of INT type.  It specifies the unique number assigned to each blood transfusion. It is the FOREIGN KEY.

Expected result:

User should be able to check the report using the transfusion id. 
User should be able to see all the attributes displayed on the page. 

Status (Pass/Fail, when this test was performed):
N/A

Notes:
The function are already implemented and working as expected. 

Post-conditions (what must be true about the system when the test has completed successfully):
The data from the database tables should be able to be viewed in the 'View Complication Reports Page'.

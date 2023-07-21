# CSPB 3308
# Group 2 - Space Monkeys
# Project Deliverable 4 - Web Pages Design

## <b>Database Architecture</b>

### <u>Table: Bloodbanks_and_Hospitals</u>

#### Table Description
- This page houses all of the information for each institution whether it is a blood bank, a hospital, or another health care institution in the space monkeys network. The PRIMARY KEY is the Institution_ID which is unique for each institution.

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
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Bloodbanks_and_Hospitals table is if ('''SELECT * FROM Bloodbanks_and_Hospitals WHERE Institution_ID = 64;''') == (64, 'Hospital', 'Yuma County', 'Wray', 'CO', 76650, 13526, 2500, 441, 7300, 1000, 11000, 1941) which resulted in "First Test Passed!?" when the "sm_dbAPI.py" file executed.

### <u>Table: Donor</u>

#### Table Description
- This page houses all of the information for each blood donor in the space monkeys network. The PRIMARY KEY is the Donor_ID which is unique for each blood donor.

#### Field names and short description
Donor_ID 
- This field is of INT type.  It specifies the unique number assigned to each blood donor in the network.  It is the PRIMARY KEY.

Name 
- This field is of VARCHAR(90) type.  It specifies the name of the blood donor.

Blood_Type 
- This field is of VARCHAR(2) type.  It specifies the blood type of the blood donor.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Donor table is if ('''SELECT * FROM Donor WHERE Donor_ID = 22;''') == (22, 'Steve Rogers', 'B-') which resulted in "Second Test Passed!?" when the "sm_dbAPI.py" file executed.

### <u>Table: Patient</u>

#### Table Description
- This page houses all of the information for each patient in the network who will/has received a blood transfusion at an institution in the space monkeys network. The PRIMARY KEY is the Patient_ID which is unique for each patient.

#### Field names and short description
Patient_ID 
- This field is of INT type.  It specifies the unique number assigned to each patient receiving blood in the network. It is the PRIMARY KEY.

Name 
- This field is of VARCHAR(90) type.  It specifies the name of the patient receiving blood.

Blood_Type 
- This field is of VARCHAR(2) type.  It specifies the blood type of the patient receiving blood.

#### Test to verify each table
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Patient table is if ('''SELECT * FROM Patient WHERE Patient_ID = 26;''') == (26, 'Zena Zootopia', 'O+') which resulted in "Third Test Passed!?" when the "sm_dbAPI.py" file executed.

### <u>Table: Donation</u>

#### Table Description
- This page houses all of the information for each donation that takes place at an institution in the space monkeys network. The PRIMARY KEY is the Donation_ID which is unique for each blood donation.  The field Donor_ID is a FOREIGN KEY with the Donor_ID field from the Donor Table.  The field Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

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
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Donation table is if ('''SELECT * FROM Donation WHERE Donation_ID = 42;''') == (42, '20230711 9:00:00', 22, 'Dr. Stephan Strange', 23, 1) which resulted in "Fourth Test Passed!?" when the "sm_dbAPI.py" file executed.

### <u>Table: Transfusion</u>

#### Table Description
- This page houses all of the information for each blood transfusion that occurs at an institution in the space monkeys network. The PRIMARY KEY is the Transfusion_ID which is unique for each blood transfusion. The field Donation_ID is a FOREIGN KEY with the Donation_ID field from the Donation Table.  The field Patient_ID is a FOREIGN KEY with the Patient_ID field from the Patient Table.  The field Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

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
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Transfusion table is if ('''SELECT * FROM Transfusion WHERE Transfusion_ID = 4;''') == (4, '20230723 11:00:00', 4, 23, 'Dr. Harleen Quinzel', 61, 1) which resulted in "Fifth Test Passed!?" when the "sm_dbAPI.py" file executed.

### <u>Table: Transfer</u>

#### Table Description
- This page houses all of the information for each blood transfer that occurs between two institutions in the space monkeys network. The PRIMARY KEY is the Transfer_ID which is unique for each blood transfer.  The field Donation_ID is a FOREIGN KEY with the Donation_ID field from the Donation Table.  The field Sending_Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.  The field Receiving_Hospital_ID is a FOREIGN KEY with the Institution_ID field from the Bloodbanks_and_Hospitals Table.

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
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Transfer table is if ('''SELECT * FROM Transfer WHERE Transfer_ID = 4;''') == (4, '20230704 11:00:00', 28, 37, 17) which resulted in "Sixth Test Passed!?" when the "sm_dbAPI.py" file executed.

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
- There is a function in the "sm_dbAPI.py" file called "test_tables(db_filename)". Its only parameter is "db_filename" which is the database name, for our project the "db_filename = space_mokeys_db".  This "test_tables" function tests each database table to make sure the data was filled in correctly.  Each table is tested with a query of the database and the known output. It lets the developer know if all of the tests passed by prints "Tests Passed" messages when running the "sm_dbAPI.py" file to set-up the database.
- The test for the Complication table is if ('''SELECT * FROM Complication WHERE Complication_ID = 1;''') == (1, 4, 'Throwing up multiple times a day') which resulted in "Seventh Test Passed!?" and "All Tests Passed!!!" when the "sm_dbAPI.py" file executed.

## <b>Data Access Methods and How Exactly Each of the Pages Behaves with these Methods</b>

### <u>About Page</u>

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
    User should see amount of units available for specified blood type at each instituion in space monkeys network.
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

### <u>Blood Levels and Visualization Page</u>

### <u>Blood Details Page</u>

### <u>Report Complications Page</u>

### <u>View Complication Reports Page</u>

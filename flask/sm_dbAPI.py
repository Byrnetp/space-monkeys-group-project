## CS 3308 Group Project
## Team 2: Space Monkeys
## Main database driver code
## Last Update: Travis Byrne, 9 August 2023

import psycopg2
import datetime

# Creates a database with the filename given. Create the required tables and fields.
def create(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Drop existing tables to start fresh
    c.execute("DROP TABLE IF EXISTS Bloodbanks_and_Hospitals CASCADE")
    c.execute("DROP TABLE IF EXISTS Donor CASCADE")
    c.execute("DROP TABLE IF EXISTS Patient CASCADE")
    c.execute("DROP TABLE IF EXISTS Donation CASCADE")
    c.execute("DROP TABLE IF EXISTS Transfusion CASCADE")
    c.execute("DROP TABLE IF EXISTS Transfer CASCADE")
    c.execute("DROP TABLE IF EXISTS Complication CASCADE")
    conn.commit()
    
    c.execute('''CREATE TABLE Bloodbanks_and_Hospitals
                (Institution_ID INT, 
                Type VARCHAR(45), 
                Name VARCHAR(90), 
                City VARCHAR(45), 
                State VARCHAR(2), 
                A_Positive_Units INT, 
                A_Negative_Units INT, 
                B_Positive_Units INT,
                B_Negative_Units INT,
                AB_Positive_Units INT,
                AB_Negative_Units INT,
                O_Positive_Units INT,
                O_Negative_Units INT,
                PRIMARY KEY(Institution_ID));''')
    c.execute('''CREATE TABLE Donor
                (Donor_ID INT, 
                Name VARCHAR(90), 
                Blood_Type VARCHAR(3), 
                PRIMARY KEY(Donor_ID));''')
    c.execute('''CREATE TABLE Patient
                (Patient_ID INT, 
                Name VARCHAR(90), 
                Blood_Type VARCHAR(3), 
                PRIMARY KEY(Patient_ID));''')
    c.execute('''CREATE TABLE Donation
                (Donation_ID INT, 
                Date_Time VARCHAR(30), 
                Donor_ID INT, 
                Medical_Professional VARCHAR(90), 
                Hospital_ID INT, 
                Amount INT,
                PRIMARY KEY(Donation_ID),
                FOREIGN KEY(Donor_ID) REFERENCES Donor(Donor_ID),
                FOREIGN KEY(Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Transfusion
                (Transfusion_ID INT, 
                Date_Time VARCHAR(30), 
                Donation_ID INT, 
                Patient_ID INT, 
                Medical_Professional VARCHAR(90), 
                Hospital_ID INT, 
                Amount INT,
                PRIMARY KEY(Transfusion_ID),
                FOREIGN KEY(Donation_ID) REFERENCES Donation(Donation_ID),
                FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID),
                FOREIGN KEY(Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Transfer
                (Transfer_ID INT, 
                Date_Time VARCHAR(30),
                Donation_ID INT, 
                Receiving_Hospital_ID INT,
                Sending_Hospital_ID INT,
                PRIMARY KEY(Transfer_ID),
                FOREIGN KEY(Donation_ID) REFERENCES Donation(Donation_ID),
                FOREIGN KEY(Sending_Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID),
                FOREIGN KEY(Receiving_Hospital_ID) REFERENCES Bloodbanks_and_Hospitals(Institution_ID));''')
    c.execute('''CREATE TABLE Complication
                (Complication_ID INT, 
                Transfusion_ID INT,
                Comments VARCHAR(180), 
                PRIMARY KEY(Complication_ID),
                FOREIGN KEY(Transfusion_ID) REFERENCES Transfusion(Transfusion_ID));''')
    conn.commit()
    conn.close()

def fill(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    
    # Fill in the Bloodbanks_and_Hospitals table
    with open("sample_data/bloodbanks.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "bloodbanks_and_hospitals", sep=",")
        
    # Fill Donors table
    with open("sample_data/donors.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "donor", sep=",")
        
    # Fill in the Patient table
    with open("sample_data/patients.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "patient", sep=",")

    # Fill in the Donation table
    with open("sample_data/donations.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "donation", sep=",")
    
    # Fill in the Transfusion table
    with open("sample_data/transfusions.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "transfusion", sep=",")
    
    # Fill in the Transfer table
    with open("sample_data/transfers.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "transfer", sep=",")
        
    # Fill in the Complication table
    with open("sample_data/complications.csv") as csvFile:
       next(csvFile) # skip column names
       c.copy_from(csvFile, "complication", sep=",")

    conn.commit()
    conn.close()

# Function to get Donor ID given Donor Name
def getDonorID(db_filename, donorName):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    if (donorName):
        c.execute('''SELECT Donor_ID FROM Donor WHERE Name = ?''', (donorName,))
        result = c.fetchone()
    else:
        result = None

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None

# Function to get Patient ID given Patient Name
def getPatientID(db_filename, patientName):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    if (patientName):
        c.execute('''SELECT Patient_ID FROM Patient WHERE Name = {};'''.format(patientName))
        result = c.fetchone()
    else:
        result = None

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None

# Function to get Blood Bank ID given Blood Bank Name
def getBloodBankID(db_filename, bloodBankName):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT Institution_ID FROM Bloodbanks_and_Hospitals WHERE Name = ?;''', (bloodBankName,))
    result = c.fetchone()

    # Commit and close connection
    conn.commit()
    conn.close()

    # Return result
    if result:
         return result[0]
    else:
        return None
        
# Function to verify donation entry
def getDonation(db_filename, medicalProfessional):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT * FROM Donation WHERE Medical_Professional = ?;''', (medicalProfessional,))
    result = c.fetchall()

    for line in result:
        print(line)

    # Commit and close connection
    conn.commit()
    conn.close()
    return
        
# Function to verify transfusion entry
def getTransfusion(db_filename, medicalProfessional):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find donor ID
    c.execute('''SELECT * FROM Transfusion WHERE Medical_Professional = ?;''', (medicalProfessional,))
    result = c.fetchall()

    for line in result:
        print(line)

    # Commit and close connection
    conn.commit()
    conn.close()
    return
        
# Function to enter blood bank in Blood Banks table
def enterBloodBank(db_filename, bloodBankName, bloodBankType, bloodBankCity, bloodBankState):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next blood bank ID
    c.execute('''SELECT MAX(Institution_ID) FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchone()
    bloodBankID = result[0] + 1

    # Insert blood bank
    c.execute('''INSERT INTO Bloodbanks_and_Hospitals (Institution_ID, Name, Type, City, State, A_Positive_Units, A_Negative_Units, B_Positive_Units, B_Negative_Units, AB_Positive_Units, AB_Negative_Units, O_Positive_Units, O_Negative_Units) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);''', (bloodBankID, bloodBankName, bloodBankType, bloodBankCity, bloodBankState, 0, 0, 0, 0, 0, 0, 0, 0))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter donor in Donor table
def enterDonor(db_filename, donorName, donorBloodType):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next donor ID
    c.execute('''SELECT MAX(Donor_ID) FROM Donor;''')
    result = c.fetchone()
    donorID = result[0] + 1

    # Insert donor
    c.execute('''INSERT INTO Donor (Donor_ID, Name, Blood_Type) VALUES (?,?,?);''', (donorID, donorName, donorBloodType))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter patient in Patient table
def enterPatient(db_filename, patientName, patientBloodType):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next patient ID
    c.execute('''SELECT MAX(Patient_ID) FROM Patient;''')
    result = c.fetchone()
    patientID = result[0] + 1

    # Insert patient
    c.execute('''INSERT INTO Patient (Patient_ID, Name, Blood_Type) VALUES (?,?,?);''', (patientID, patientName, patientBloodType))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter donation in Donations table
def enterDonation(db_filename, donorID, bloodBankID, medicalProfessional, quantity, date):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next donation ID
    c.execute('''SELECT MAX(Donation_ID) FROM Donation;''')
    result = c.fetchone()
    donationID = result[0] + 1

    # Insert donation
    c.execute('''INSERT INTO Donation (Donation_ID, Donor_ID, Hospital_ID, Medical_Professional, Amount, Date_Time) VALUES (?,?,?,?,?,?);''', (donationID, donorID, bloodBankID, medicalProfessional, quantity, date))
    
    # Increment blood bank inventory
    c.execute('''SELECT Blood_Type FROM Donor WHERE Donor_ID = (?);''', (donorID,))
    result = c.fetchone()
    bloodtype = result[0]

    if bloodtype == 'A+':
        bt_column = 'A_Positive_Units'
    elif bloodtype == 'A-':
        bt_column = 'A_Negative_Units'
    elif bloodtype == 'B+':
        bt_column = 'B_Positive_Units'
    elif bloodtype == 'B-':
        bt_column = 'B_Negative_Units'
    elif bloodtype == 'AB+':
        bt_column = 'AB_Positive_Units'
    elif bloodtype == 'AB-':
        bt_column = 'AB_Negative_Units'
    elif bloodtype == 'O+':
        bt_column = 'O_Positive_Units'
    elif bloodtype == 'O-':
        bt_column = 'O_Negative_Units'

    # Calculate the new quantity for Receiving Hospital
    sql = 'SELECT '+bt_column+' FROM Bloodbanks_and_Hospitals WHERE Institution_ID = '+str(bloodBankID)+';'''
    c.execute(sql)
    result = c.fetchone()
    newamount_r = result[0] + int(quantity)
    
    # Update Receiving Hospital Inventory
    sql = 'UPDATE Bloodbanks_and_Hospitals SET '+bt_column+' = '+str(newamount_r)+' WHERE Institution_ID = '+str(bloodBankID)+';'''
    c.execute(sql)

    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to find compatible blood 
def findCompatibleBlood(db_filename, patientID, bloodBankID):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Find blood type of patient
    c.execute('''SELECT Blood_Type FROM Patient WHERE Patient_ID = (?);''', (patientID,))
    result = c.fetchone()
    if result:
        bloodtype = result[0]

        # Find a compatible donation at that blood bank
        # That has not already been transfused
        if bloodtype == 'A+':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("A+", "A-", "O+", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'A-':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("A-", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'B+':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("B+", "B-", "O+", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'B-':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("B-", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'AB+':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'AB-':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("A-", "B-", "AB-", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'O+':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("O+", "O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        elif bloodtype == 'O-':
            c.execute('''SELECT Donation_ID FROM Donation
                        JOIN Donor ON Donation.Donor_ID = Donor.Donor_ID
                        WHERE Blood_Type IN ("O-")
                        AND Hospital_ID = (?)
                        AND Donation_ID NOT IN (
                            SELECT Donation_ID FROM Transfusion
                        );''', (bloodBankID,))
        result = c.fetchone()

        # If there is a valid result, return it, otherwise return None
        if result:
            return result[0]
        else:
            return None
    else:
        return None

# Function to enter transfusion in Transfusions table
def enterTransfusion(db_filename, patientID, bloodBankID, donationID, medicalProfessional, quantity, date):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next transfusion ID
    c.execute('''SELECT MAX(Transfusion_ID) FROM Transfusion;''')
    result = c.fetchone()
    transfusionID = result[0] + 1

    # Insert transfusion
    c.execute('''INSERT INTO Transfusion (Transfusion_ID, Patient_ID, Donation_ID, Hospital_ID, Medical_Professional, Amount, Date_Time) VALUES (?,?,?,?,?,?,?);''', (transfusionID, patientID, donationID, bloodBankID, medicalProfessional, quantity, date))
    
    # Decrement blood bank inventory
    c.execute('''SELECT Blood_Type FROM Donor 
                JOIN Donation ON Donor.Donor_ID = Donation.Donor_ID
                WHERE Donation_ID = (?);''', (donationID,))
    result = c.fetchone()
    bloodtype = result[0]

    if bloodtype == 'A+':
        bt_column = 'A_Positive_Units'
    elif bloodtype == 'A-':
        bt_column = 'A_Negative_Units'
    elif bloodtype == 'B+':
        bt_column = 'B_Positive_Units'
    elif bloodtype == 'B-':
        bt_column = 'B_Negative_Units'
    elif bloodtype == 'AB+':
        bt_column = 'AB_Positive_Units'
    elif bloodtype == 'AB-':
        bt_column = 'AB_Negative_Units'
    elif bloodtype == 'O+':
        bt_column = 'O_Positive_Units'
    elif bloodtype == 'O-':
        bt_column = 'O_Negative_Units'

    # Calculate the new quantity for Providing Hospital
    sql = 'SELECT '+bt_column+' FROM Bloodbanks_and_Hospitals WHERE Institution_ID = '+str(bloodBankID)+';'''
    c.execute(sql)
    result = c.fetchone()
    newamount_r = result[0] - int(quantity)
    
    # Update Providing Hospital Inventory
    sql = 'UPDATE Bloodbanks_and_Hospitals SET '+bt_column+' = '+str(newamount_r)+' WHERE Institution_ID = '+str(bloodBankID)+';'''
    c.execute(sql)
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to get list of Donors
def getDonorsList(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Donor;''')
    result = c.fetchall()

    # Build donor list
    donorsList = []
    for donor in result:
        donorsList.append(donor[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return donorsList

# Function to get list of Transfusion IDs
def getTransfusionIDList(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Transfusion_ID FROM Transfusion;''')
    result = c.fetchall()

    # Build transfusion ID list
    transfusionIDList = []
    for transfusion in result:
        transfusionIDList.append(transfusion[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return transfusionIDList

# Function to get list of Patients
def getPatientsList(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Patient;''')
    result = c.fetchall()

    # Build donor list
    patientsList = []
    for patient in result:
        patientsList.append(patient[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return patientsList

# Function to get list of Donation IDs
def getDonationIDsList(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Donation_ID FROM Donation;''')
    result = c.fetchall()

    # Build donor list
    donationIDsList = []
    for donationID in result:
        donationIDsList.append(donationID[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return donationIDsList

# Function to get list of Blood Banks
def getBloodBanksList(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Name FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()

    # Build donor list
    bloodBanksList = []
    for bloodBank in result:
        bloodBanksList.append(bloodBank[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return bloodBanksList

# Function to get list of Blood Banks by Number
def getBloodBanksListNUM(db_filename):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # SQL query to get all donor names
    c.execute('''SELECT Institution_ID FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()

    # Build donor list
    bloodBanksList = []
    for bloodBank in result:
        bloodBanksList.append(bloodBank[0])
    
    # Commit and close connection
    conn.commit()
    conn.close()

    return bloodBanksList

# Function to update Bloodbanks_and_Hospitals Table for a Blood Transfer
def UpdateInstitutionInventory(db_filename, donationid, receivinghospitalID, sendinghospitalID):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    
    # Get next transfer ID
    c.execute('''SELECT Donor_ID FROM Donation WHERE Donation_ID = (?);''', (donationid,))
    dresult = c.fetchone()
    donorID = dresult[0]
    c.execute('''SELECT Blood_Type FROM Donor WHERE Donor_ID = (?);''', (donorID,))
    result = c.fetchone()
    bloodtype = result[0]

    if bloodtype == 'A+':
        bt_column = 'A_Positive_Units'
    elif bloodtype == 'A-':
        bt_column = 'A_Negative_Units'
    elif bloodtype == 'B+':
        bt_column = 'B_Positive_Units'
    elif bloodtype == 'B-':
        bt_column = 'B_Negative_Units'
    elif bloodtype == 'AB+':
        bt_column = 'AB_Positive_Units'
    elif bloodtype == 'AB-':
        bt_column = 'AB_Negative_Units'
    elif bloodtype == 'O+':
        bt_column = 'O_Positive_Units'
    elif bloodtype == 'O-':
        bt_column = 'O_Negative_Units'

    # Calculate the new quantity for Receiving Hospital
    sql = 'SELECT '+bt_column+' FROM Bloodbanks_and_Hospitals WHERE Institution_ID = '+str(receivinghospitalID)+';'''
    c.execute(sql)
    result = c.fetchone()
    newamount_r = result[0] + 1
    
    # Calculate the new quantity for Sending Hospital
    sql = 'SELECT '+bt_column+' FROM Bloodbanks_and_Hospitals WHERE Institution_ID = '+str(sendinghospitalID)+';'''
    c.execute(sql)
    result = c.fetchone()
    newamount_s = result[0] - 1

    # Update Receiving Hospital
    sql = 'UPDATE Bloodbanks_and_Hospitals SET '+bt_column+' = '+str(newamount_r)+' WHERE Institution_ID = '+str(receivinghospitalID)+';'''
    c.execute(sql)
    
    # Update Sending Hospital
    sql = 'UPDATE Bloodbanks_and_Hospitals SET '+bt_column+' = '+str(newamount_s)+' WHERE Institution_ID = '+str(sendinghospitalID)+';'''
    c.execute(sql)
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to enter blood transfer in Transfer table
def enterTransfer(db_filename, donationID, receivinghospitalID, sendinghospitalID):

    # Initialize connection
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()

    # Get next transfer ID
    c.execute('''SELECT MAX(Transfer_ID) FROM Transfer;''')
    result = c.fetchone()
    transferID = result[0] + 1
    
    # Get current datetime
    dt_now = datetime.datetime.now()

    # Insert transfer
    c.execute('''INSERT INTO Transfer (Transfer_ID, Date_Time, Donation_ID, Receiving_Hospital_ID, Sending_Hospital_ID) VALUES (?,?,?,?,?);''', (transferID, dt_now, donationID, receivinghospitalID, sendinghospitalID,))
    
    # Commit and close connection
    conn.commit()
    conn.close()
    return

# Function to get A postive units
def getBloodAList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all A positive units
    c.execute('''SELECT A_POSITIVE_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A positive units:
def getTotalAPositiveUnits(db_filename):
    a_positive_units = getBloodAList(db_filename)
    total_a_positive_units = sum(a_positive_units)
    return total_a_positive_units

# Function to get B positive units
def getBloodBList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all B positive units
    c.execute('''SELECT B_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total b positive units:
def getTotalBPositiveUnits(db_filename):
    b_positive_units = getBloodBList(db_filename)
    total_b_positive_units = sum(b_positive_units)
    return total_b_positive_units

# Function to get AB positive units
def getBloodABList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all AB psoitive units
    c.execute('''SELECT AB_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total AB positive units:
def getTotalABPositiveUnits(db_filename):
    ab_positive_units = getBloodABList(db_filename)
    total_ab_positive_units = sum(ab_positive_units)
    return total_ab_positive_units

# Function to get O positive units
def getBloodOList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all O positive units
    c.execute('''SELECT O_Positive_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total O positive units:
def getTotalOPositiveUnits(db_filename):
    o_positive_units = getBloodOList(db_filename)
    total_o_positive_units = sum(o_positive_units)
    return total_o_positive_units

# Function to get A negative units
def getBloodANList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all A negative units
    c.execute('''SELECT A_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalANegativeUnits(db_filename):
    a_negative_units = getBloodANList(db_filename)
    total_a_negative_units = sum(a_negative_units)
    return total_a_negative_units

# Function to get B negative units
def getBloodBNList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    # SQL query to get all donor names
    c.execute('''SELECT B_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total B Negative units:
def getTotalBNegativeUnits(db_filename):
    b_negative_units = getBloodBNList(db_filename)
    total_b_negative_units = sum(b_negative_units)
    return total_b_negative_units

# Function to get AB negative units
def getBloodABNList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT AB_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalABNegativeUnits(db_filename):
    ab_negative_units = getBloodANList(db_filename)
    total_ab_negative_units = sum(ab_negative_units)
    return total_ab_negative_units

# Function to get O negative units
def getBloodONList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT O_Negative_Units FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# function to get total A Negative units:
def getTotalONegativeUnits(db_filename):
    o_negative_units = getBloodONList(db_filename)
    total_o_negative_units = sum(o_negative_units)
    return total_o_negative_units

# Function to get all bank ids
def getBloodID(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Institution_ID FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to get city and state 
def getAddress(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT City, State FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to return blood bank types
def getBankType(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Type FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    bloodList = []
    for bloodBank in result:
        bloodList.append(bloodBank[0])
    conn.commit()
    conn.close()
    return bloodList

# Function to get all data from the Donation table for a given blood bank ID
def getDonationTable(db_filename, bankID):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Donation WHERE Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all data from the Transfusion table for a given blood bank ID
def getTransfusionTable(db_filename, bankID):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfusion WHERE Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all incoming transfer data from the Transfer table for a given blood bank ID
def getIncomingTransferTable(db_filename, bankID):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfer WHERE Receiving_Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all outgoing transfer data from the Transfer table for a given blood bank ID
def getOutgoingTransferTable(db_filename, bankID):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Transfer WHERE Sending_Hospital_ID = {};'''.format(bankID))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get list of Blood Banks and their IDs
def getBloodBanksIDsList(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT Name, Institution_ID FROM Bloodbanks_and_Hospitals;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to get all donor data
def getDonors(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Donor;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


# Function to get all patient data
def getPatients(db_filename):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    c.execute('''SELECT * FROM Patient;''')
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


#Function to enter Comments on complication_report.html
def enterComments(db_filename, transfusion_id, comments):
    try:
        # Connect to the database
        conn = psycopg2.connect(db_filename)
        c = conn.cursor()

        # Check if the Transfusion_ID exists in the Transfusion table
        c.execute("SELECT * FROM Transfusion WHERE Transfusion_ID=?", (transfusion_id,))
        result = c.fetchone()

        if result is None:
            print(f"Transfusion with ID {transfusion_id} not found.")
            return False
        else:
            # If the Transfusion_ID exists, insert the data into the Complication table
            
            # Get next complication ID
            c.execute('''SELECT MAX(Complication_ID) FROM Complication;''')
            result = c.fetchone()
            complicationID = result[0] + 1

            c.execute("INSERT INTO Complication (Complication_ID, Transfusion_ID, Comments) VALUES (?, ?, ?)",
                      (complicationID, transfusion_id, comments))
            conn.commit()
            print("Comments added successfully.")
            return True

        # Close the database connection
        conn.close()

    except psycopg2.Error as e:
        print("Error:", e)
        return False

# Function to get Comments for view_report.html
def getComplication(db_filename, transfusion_id):
    conn = psycopg2.connect(db_filename)
    c = conn.cursor()
    
    # Retrieve the Complication_ID and Comments for the given transfusion_id from the Complication table
    c.execute('''SELECT Complication_ID, Comments FROM Complication WHERE Transfusion_ID = ?;''', (transfusion_id,))
    result = c.fetchone()
    print(result)
    
    conn.close()
    
    if result:
        complication_id, comments = result
        return complication_id, comments
    else:
        return None, None
    
# Code to run to set up database
if __name__ == "__main__":
    space_monkeys_db = 'postgres://space_monkeys_db_user:5Unps05ZIjef9xcdQDYsCB3swwVforRy@dpg-cj9ibhivvtos73ejdvdg-a.oregon-postgres.render.com/space_monkeys_db'
    create(space_monkeys_db)
    fill(space_monkeys_db)
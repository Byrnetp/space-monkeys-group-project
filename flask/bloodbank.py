## CS 3308 Group Project
## Team 2: Space Monkeys
## Main Flask driver code
## Last Update: David Hughes, 26 July 2023

import prefix
from flask import Flask, url_for, request, render_template
from markupsafe import escape
import sm_dbAPI

# Create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)

# Define database name
space_monkeys_db = 'space_monkeys_db'

###############################################################################

# Home page
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Home page (alternate)
@app.route('/home')
def home():
    return render_template('homepage.html')

# Blood bank entry page
@app.route('/bloodbank')
def bloodbank():

    # Get input parameters from URL
    bloodBankName = request.args.get('bloodBankName', None)
    bloodBankType = request.args.get('bloodBankType', None)
    bloodBankCity = request.args.get('bloodBankCity', None)
    bloodBankState = request.args.get('bloodBankState', None)

    # Insert data if all entries are populated
    if (space_monkeys_db and bloodBankName and bloodBankType and bloodBankCity and bloodBankState):
        sm_dbAPI.enterBloodBank(space_monkeys_db, bloodBankName, bloodBankType, bloodBankCity, bloodBankState)
        
    # Render page
    return render_template('bloodbank.html')

# Donor entry page
@app.route('/donor')
def donor():

    # Get input parameters from URL
    donorName = request.args.get('donorName', None)
    donorBloodType = request.args.get('donorBloodType', None)

    # Insert data if all entries are populated
    if (space_monkeys_db and donorName and donorBloodType):
        sm_dbAPI.enterDonor(space_monkeys_db, donorName, donorBloodType)
        
    # Render page
    return render_template('donor.html')

# Patient entry page
@app.route('/patient')
def patient():

    # Get input parameters from URL
    patientName = request.args.get('patientName', None)
    patientBloodType = request.args.get('patientBloodType', None)

    # Insert data if all entries are populated
    if (space_monkeys_db and patientName and patientBloodType):
        sm_dbAPI.enterPatient(space_monkeys_db, patientName, patientBloodType)
        
    # Render page
    return render_template('patient.html')

# Donation entry page
@app.route('/donation')
def donation():

    # Get input parameters from URL
    donorName = request.args.get('donorName', None)
    donorBloodType = request.args.get('donorBloodType', None)
    bloodBankName = request.args.get('bloodBankName', None)
    medicalProfessional = request.args.get('medicalProfessional', None)
    quantity = request.args.get('quantity', None)
    date = request.args.get('date', None)

    # Query database to get Donor ID
    donorID = sm_dbAPI.getDonorID(space_monkeys_db, donorName)

    # Query database to get Blood Bank ID
    bloodBankID = sm_dbAPI.getBloodBankID(space_monkeys_db, bloodBankName)

    # Insert data if all entries are populated
    if (space_monkeys_db and donorID and bloodBankID and medicalProfessional and quantity and date):
        sm_dbAPI.enterDonation(space_monkeys_db, donorID, bloodBankID, medicalProfessional, quantity, date)
        
    # Query database to get list of donors
    donorsList = sm_dbAPI.getDonorsList(space_monkeys_db)

    # Query database to get list of blood banks
    bloodBanksList = sm_dbAPI.getBloodBanksList(space_monkeys_db)

    # Render page
    return render_template(
        'donation.html', 
        numDonors = len(donorsList), 
        donorsList = donorsList, 
        numBloodBanks = len(bloodBanksList), 
        bloodBanksList = bloodBanksList,
        )

# Transfusion entry page
@app.route('/transfusion')
def transfusion():

    # Get input parameters from URL
    patientName = request.args.get('patientName', None)
    patientBloodType = request.args.get('patientBloodType', None)
    donationID = request.args.get('donationID', None)
    bloodBankName = request.args.get('bloodBankName', None)
    medicalProfessional = request.args.get('medicalProfessional', None)
    quantity = request.args.get('quantity', None)
    date = request.args.get('date', None)

    # Query database to get Patient ID
    patientID = sm_dbAPI.getPatientID(space_monkeys_db, patientName)

    # Query database to get Blood Bank ID
    bloodBankID = sm_dbAPI.getBloodBankID(space_monkeys_db, bloodBankName)

    # Insert data if all entries are populated
    if (space_monkeys_db and patientID and bloodBankID and donationID and medicalProfessional and quantity and date):
        sm_dbAPI.enterTransfusion(space_monkeys_db, patientID, bloodBankID, donationID, medicalProfessional, quantity, date)
        
    # Query database to get list of patients
    patientsList = sm_dbAPI.getPatientsList(space_monkeys_db)

    # Query database to get list of donation IDs
    donationsList = sm_dbAPI.getDonationIDsList(space_monkeys_db)

    # Query database to get list of blood banks
    bloodBanksList = sm_dbAPI.getBloodBanksList(space_monkeys_db)

    # Render page
    return render_template(
        'transfusion.html', 
        numPatients = len(patientsList), 
        patientsList = patientsList, 
        numDonations = len(donationsList),
        donationsList = donationsList,
        numBloodBanks = len(bloodBanksList), 
        bloodBanksList = bloodBanksList,
        )

# Blood bank entry page
@app.route('/transfer')
def transfer():

    # Get input parameters from URL
    DonationID = request.args.get('DonationID', None)
    ReceivingHospitalID = request.args.get('ReceivingHospitalID', None)
    SendingHospitalID = request.args.get('SendingHospitalID', None)

    # Insert data if all entries are populated
    if (space_monkeys_db and DonationID and ReceivingHospitalID and SendingHospitalID):
        sm_dbAPI.enterTransfer(space_monkeys_db, DonationID, ReceivingHospitalID, SendingHospitalID)
        
    # Update table
    if (space_monkeys_db and DonationID and ReceivingHospitalID and SendingHospitalID):
        sm_dbAPI.UpdateInstitutionInventory(space_monkeys_db, DonationID, ReceivingHospitalID, SendingHospitalID)
        
    # Query database to get list of donation IDs
    donationsList = sm_dbAPI.getDonationIDsList(space_monkeys_db)
    
    # Query database to get list of Hospital IDs
    hospitalsList = sm_dbAPI.getBloodBanksList(space_monkeys_db)
        
    # Render page
    return render_template(
        'transfer.html',
        numDonations = len(donationsList),
        donationsList = donationsList,
        numHospitals = len(hospitalsList),
        hospitalsList = hospitalsList
        )

###############################################################################

# Main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


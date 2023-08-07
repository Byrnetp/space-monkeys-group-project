## CS 3308 Group Project
## Team 2: Space Monkeys
## Main Flask driver code
## Last Update: Travis Byrne, 2 August 2023

import prefix
from flask import Flask, url_for, request, render_template, request, jsonify
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
    bloodBankName = request.args.get('bloodBankName', None)
    medicalProfessional = request.args.get('medicalProfessional', None)
    quantity = request.args.get('quantity', None)
    date = request.args.get('date', None)

    # Query database to get Patient ID
    patientID = sm_dbAPI.getPatientID(space_monkeys_db, patientName)

    # Query database to get Blood Bank ID
    bloodBankID = sm_dbAPI.getBloodBankID(space_monkeys_db, bloodBankName)

    # Query database to get compatible donation
    donationID = sm_dbAPI.findCompatibleBlood(space_monkeys_db, patientID, bloodBankID)

    # Insert data if all entries are populated
    if (space_monkeys_db and patientID and bloodBankID and donationID and medicalProfessional and quantity and date):
        sm_dbAPI.enterTransfusion(space_monkeys_db, patientID, bloodBankID, donationID, medicalProfessional, quantity, date)
        
    # Set flag if any entries are populated
    donationFlag = False
    if (space_monkeys_db and patientID and bloodBankID and medicalProfessional and quantity and date):
        donationFlag = True

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
        numBloodBanks = len(bloodBanksList), 
        bloodBanksList = bloodBanksList,
        donationID = donationID,
        donationFlag = donationFlag,
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

# Blood Visualization Page
@app.route('/visualization')
def visualization():
    # Get input parameters from URL
    bloodBankName = request.args.get('bloodBankName', None)
    # Query database to get Blood Bank ID
    getBloodID = sm_dbAPI.getBloodID(space_monkeys_db)
    # Query database to get list of blood banks names
    bloodBanksList = sm_dbAPI.getBloodBanksList(space_monkeys_db)
    # Query database to get list of A positive units
    blood_A_positive = sm_dbAPI.getBloodAList(space_monkeys_db)
    # Query database to get list of B positive units
    blood_B_positive = sm_dbAPI.getBloodBList(space_monkeys_db)
    # query db to get list of AB positive units
    blood_AB_positive = sm_dbAPI.getBloodABList(space_monkeys_db)
    # query db to get list of O positive units
    blood_O_positive = sm_dbAPI.getBloodOList(space_monkeys_db)
    # query db to get list of A negative units
    blood_A_negative = sm_dbAPI.getBloodANList(space_monkeys_db)
    # query db to get list of B negative units
    blood_B_negative = sm_dbAPI.getBloodBNList(space_monkeys_db)
    # query db to get list of AB negative units
    blood_AB_negative = sm_dbAPI.getBloodABNList(space_monkeys_db)
    # query db to get list of B negative units
    blood_O_negative = sm_dbAPI.getBloodONList(space_monkeys_db)
    # query db to get address
    bloodBankAddress = sm_dbAPI.getAddress(space_monkeys_db)
    # query db to get bank types
    bloodBankType = sm_dbAPI.getBankType(space_monkeys_db)
    # total A positive
    totalAPositiveUnits = sm_dbAPI.getTotalAPositiveUnits(space_monkeys_db)
    # total B positive
    totalBPositiveUnits = sm_dbAPI.getTotalBPositiveUnits(space_monkeys_db)
    # total AB positive
    totalABPositiveUnits = sm_dbAPI.getTotalABPositiveUnits(space_monkeys_db)
    # total O positive
    totalOPositiveUnits = sm_dbAPI.getTotalOPositiveUnits(space_monkeys_db)
    # total A negative
    totalANegativeUnits = sm_dbAPI.getTotalANegativeUnits(space_monkeys_db)
    # total B negative
    totalBNegativeUnits = sm_dbAPI.getTotalBNegativeUnits(space_monkeys_db)
    # total AB negative
    totalABNegativeUnits = sm_dbAPI.getTotalABNegativeUnits(space_monkeys_db)
    # total O negative
    totalONegativeUnits = sm_dbAPI.getTotalONegativeUnits(space_monkeys_db)
    # define labels for the pie chart
    pie_chart_labels=['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
    # define the data for the pie chart
    pie_chart_data = [totalAPositiveUnits,totalBPositiveUnits,totalABPositiveUnits,totalOPositiveUnits,totalANegativeUnits,totalBNegativeUnits,totalABNegativeUnits, totalONegativeUnits]
    # define labels for the bar chart
    bar_chart_labels = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
    # # define labels for the bar data
    bar_chart_data = [totalAPositiveUnits,totalBPositiveUnits,totalABPositiveUnits,totalOPositiveUnits,totalANegativeUnits,totalBNegativeUnits,totalABNegativeUnits, totalONegativeUnits]
    # blood info
    #getBloodInfo = sm_dbAPI.getBloodInfo(space_monkeys_db)

    # Render page
    return render_template(
        'visualization.html', 
        getBloodID = getBloodID,
        numBloodBanks = len(bloodBanksList), 
        bloodBanksList = bloodBanksList,
        bloodBankAddress = bloodBankAddress,
        bloodBankType = bloodBankType,
        blood_A_positive = blood_A_positive,
        blood_B_positive= blood_B_positive, 
        blood_AB_positive = blood_AB_positive,
        blood_O_positive = blood_O_positive,
        blood_A_negative = blood_A_negative,
        blood_B_negative = blood_B_negative,
        blood_AB_negative = blood_AB_negative,
        blood_O_negative = blood_O_negative,
        pie_chart_labels=pie_chart_labels,  # Pass the labels to the template
        pie_chart_data=pie_chart_data,      # Pass the data to the template
        totalAPositiveUnits=totalAPositiveUnits,
        totalBPositiveUnits=totalBPositiveUnits,
        totalABPositiveUnits=totalABPositiveUnits,
        totalOPositiveUnits=totalOPositiveUnits,
        totalANegativeUnits=totalANegativeUnits,
        totalBNegativeUnits=totalBNegativeUnits,
        totalABNegativeUnits=totalABNegativeUnits,
        totalONegativeUnits=totalONegativeUnits,
        bar_chart_data=bar_chart_data,
        bar_chart_labels=bar_chart_labels,
    )

# Detailed inventory page
@app.route('/detail')
def detail():

    # Get the blood banks list
    hospitals = sm_dbAPI.getBloodBanksIDsList(space_monkeys_db)

    # Get donation, transfusion, and transfer tables for the default bank
    donations = sm_dbAPI.getDonationTable(space_monkeys_db, hospitals[0][1])
    transfusions = sm_dbAPI.getTransfusionTable(space_monkeys_db, hospitals[0][1])
    outgoingTransfers = sm_dbAPI.getOutgoingTransferTable(space_monkeys_db, hospitals[0][1])
    incomingTransfers = sm_dbAPI.getIncomingTransferTable(space_monkeys_db, hospitals[0][1])

    return render_template('detail.html', hospitals=hospitals, donations=donations, transfusions=transfusions, outgoingTransfers=outgoingTransfers, incomingTransfers=incomingTransfers)

@app.route('/detail/<hospital_ID>')
def get_tables(hospital_ID):

    # Get donation, transfusion, and transfer data for the given hospital
    donations = sm_dbAPI.getDonationTable(space_monkeys_db, hospital_ID)
    transfusions = sm_dbAPI.getTransfusionTable(space_monkeys_db, hospital_ID)
    outgoingTransfers = sm_dbAPI.getOutgoingTransferTable(space_monkeys_db, hospital_ID)
    incomingTransfers = sm_dbAPI.getIncomingTransferTable(space_monkeys_db, hospital_ID)

    # Build the html to send 
    tables = '<div id="donationTable"><h3>Donations</h3><table><tr><th>Donation ID</th><th>Date & Time</th><th>Donor ID</th><th>Medical Professional</th><th>Amount</th></tr>'

    # Donation table data
    for donation in donations:
        tables += '<tr><td>' + str(donation[0]) + '</td><td>' + donation[1] + '</td><td>' + str(donation[2]) + '</td><td>' + str(donation[3]) + '</td><td>' + str(donation[5]) + '</td></tr>'

    tables += '</table></div><div id="transfusionTable"><h3>Transfusions</h3><table><tr><th>Transfusion ID</th><th>Date & Time</th><th>Donation ID</th><th>Patient ID</th> <th>Medical Professional</th><th>Amount</th></tr>'
    
    # Patient table data
    for transfusion in transfusions:
        tables += '<tr><td>' + str(transfusion[0]) + '</td><td>' + transfusion[1] + '</td><td>' + str(transfusion[2]) + '</td><td>' + str(transfusion[3]) + '</td><td>' + str(transfusion[4]) + '</td><td>' + str(transfusion[6]) + '</td></tr>'

    tables += '</table></div><div id="incomingTransferTable"><h3>Incoming Transfers</h3><table><tr><th>Transfer ID</th><th>Date & Time</th><th>Donation ID</th><th>Sending Hospital ID</th></tr>'

    # Incoming transfer data
    for i_transfer in incomingTransfers:
        tables += '<tr><td>' + str(i_transfer[0]) + '</td><td>' + i_transfer[1] + '</td><td>' + str(i_transfer[2]) + '</td><td>' + str(i_transfer[4]) + '</td></tr>'

    tables += '</table></div><div id="outgoingTransferTable"><h3>Outgoing Transfers</h3><table><tr><th>Transfer ID</th><th>Date & Time</th><th>Donation ID</th><th>Recieving Hospital ID</th></tr>'

    # Outgoing transfer data
    for o_transfer in outgoingTransfers:
        tables += '<tr><td>' + str(o_transfer[0]) + '</td><td>' + o_transfer[1] + '</td><td>' + str(o_transfer[2]) + '</td><td>' + str(o_transfer[3]) + '</td></tr>'

    tables += '</table></div>'

    return tables

@app.route('/view-donors')
def view_donors():

    # Get donor data
    donors = sm_dbAPI.getDonors(space_monkeys_db)

    return render_template('viewDonors.html', donors=donors)

@app.route('/view-patients')
def view_patients():

    # Get donor data
    patients = sm_dbAPI.getPatients(space_monkeys_db)

    return render_template('viewPatients.html', patients=patients)
 
#complication
@app.route('/complication')
def complication():

    # Get input parameters from URL
    transfusionID = request.args.get('transfusionID', None)
    comment = request.args.get('comment', None)

    # Validate that the required data is present
    if transfusionID and comment:
        sm_dbAPI.enterComments(space_monkeys_db, transfusionID, comment)

    # Query database to get list of transfusion IDs
    transfusionIDList = sm_dbAPI.getTransfusionIDList(space_monkeys_db)

    # Render the complication report form 
    return render_template(
        'complication_report.html',
        numTransfusionIDs = len(transfusionIDList), 
        transfusionIDList = transfusionIDList,
    )

#view complication
@app.route('/view_complication')
def view_complication():

    # Get input parameters from URL
    transfusionID = request.args.get('transfusionID', None)

    # If there is a transfusion ID, query database for data associated with it
    complicationID = None
    complicationComment = None
    if transfusionID:
        (complicationID, complicationComment) = sm_dbAPI.getComplication(space_monkeys_db, transfusionID)

    # Query database to get list of transfusion IDs
    transfusionIDList = sm_dbAPI.getTransfusionIDList(space_monkeys_db)

    return render_template(
        'view_report.html',
        numTransfusionIDs = len(transfusionIDList), 
        transfusionIDList = transfusionIDList, 
        transfusionID = transfusionID,
        complicationID = complicationID,
        complicationComment = complicationComment,
    )


# About
@app.route('/about')
def about():
   
    return render_template('about.html')
###############################################################################

# Main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


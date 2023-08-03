## CS 3308 Group Project
## Team 2: Space Monkeys
## Main Flask driver code
## Last Update: David Hughes, 26 July 2023

import prefix
from flask import Flask, url_for, request, render_template, request, jsonify
from markupsafe import escape
import sm_dbAPI
from sm_dbAPI import getComments

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


# Complication Report
@app.route('/complication', methods=['GET', 'POST'])
def complication():

    if request.method == 'POST':
        # Get input parameters from the form submission
        transfusion_id = request.form.get('transfusionID')
        comments = request.form.get('comment')

        # Validate that the required data is present
        if transfusion_id and comments:
            # Replace 'your_database_filename.db' with the actual name of your SQLite database file
            enterComments(space_monkeys_db, transfusion_id, comments)
            # You can add success message handling if desired, e.g., return render_template('complication_report.html', success=True)

    # Render the complication report form (including the success message if applicable)
    return render_template('complication_report.html')

#view complication
@app.route('/view_complication', methods=['GET', 'POST'])
def view_complication():
    if request.method == 'POST':
        # Get input parameters from the form submission
        transfusion_id = request.form.get('transfusionID')
        comments = request.form.get('comments')

        # Validate that the required data is present
        if transfusion_id and comments:
            # Call function to enter comments into the database
            # Replace 'your_database_filename.db' with the actual name of your SQLite database file
            enterComments(space_monkeys_db, transfusion_id, comments)
            # You can add success message handling if desired, e.g., return render_template('complication_report.html', success=True)

    elif request.method == 'GET':
        # Get the Transfusion ID from the query parameters (URL)
        # transfusion_id = request.args.get('transfusionID')
        transfusion_id= 1
        if transfusion_id:
            # Call the getComments function to fetch the Complication ID and Comments
            # complication_id, comments = getComments(space_monkeys_db, transfusion_id)
            complication_id=12345
            comments="Dummy comment 1"
            # Render the view_report.html template with the fetched data
            return render_template('view_report.html', transfusionID=transfusion_id, complicationID=complication_id, comments=comments)

    return render_template('view_report.html')


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


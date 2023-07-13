import prefix
from flask import Flask, url_for, request, render_template
from markupsafe import escape

# Create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)

###############################################################################

# Home page
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Home page (alternate)
@app.route('/home')
def home():
    return render_template('homepage.html')

# Donation page
@app.route('/donation')
def donation():
    return render_template('donation.html')

# Transfusion page
@app.route('/transfusion')
def transfusion():
    return render_template('transfusion.html')

# Detailed inventory page
@app.route('/detail')
def detail():
    return render_template('detail.html')

###############################################################################

# Main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


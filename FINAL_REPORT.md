### Project Title: 
Space Monkeys' Human Blood Bank Management App

### Team #: 
2

### Team Name: 
Space Monkeys

### Team Members (GitHub username, email address): 
Michael Becker (csdse100, mibe4187@colorado.edu), 

Travis Byrne (Byrnetp, travis.byrne@colorado.edu), 

Cyro Freire De Lima (CyroEstevao, cyfr7595@colorado.edu), 

David Hughes (dahu3614, dahu3614@colorado.edu), 

Dylan Kayyem, (dylankayyem, dyga6971@colorado.edu)

### Project Deployment
https://space-monkeys-blood-bank-app.onrender.com/

### Project tracker
https://trello.com/w/spacemonkeys18/home

### Demonstration Video
https://drive.google.com/file/d/10Pae3zoTyz_D8uAznW3AAKSShdM3XjnB/view?usp=drive_link

### GitHub Repository
https://github.com/Byrnetp/space-monkeys-group-project

### Instructions for running the website in the JupyterHub envirionment:
1. Fork and clone the repository

2. Navigate to the `space-monkeys-group-project/flask` directory

3. Start the venv virtual envirionment

ex: `. ~/venv/bin/activate`

4. Run the setup commands in the flask directory 

`. ./setup.cmds`

5. Run the app with flask 

`flask --app bloodbank.py run`

6. Navigate to the appropriate URL for your username at port 3308

`.../user/<your username>/proxy/3308`

### Final Status Report
#### What we completed
- Home page with blood donation information

- Entry pages for donors, patients, donations, transfusions, transfers, complications

- Form checking and verification

- Automatic matching of a patient to suitable blood for a transfusion

- Displays for blood levels across all hospitals and blood banks

- Visualization of blood levels in a bar graph

- Sorting and filtering of displayed data

- Page for displaying detailed data on the inventory of specific hospitals

- Pages for viewing donor and patient data

- Page for viewing comlications associated with a specific blood transfusion

- Deployment of our app using Render

- Storing and manipulating data in both SQLite and PostgreSQL databases

- Using Flask middleware to serve pages on multiple routes and manage the flow of data to and from the frontend 
and backend

- Using HTML and templates to structure web pages

- Using CSS to add style to pages

- Using Javascript to create dynamic pages that allow the user to interact with them


#### What we were in the middle of implementing
- Transfers update Donation table with current location of the blood

#### What we had planned for the future
- Get contact info for Donors from email

- Login system

- Transfers of multiple units of blood at a time

- Transfusions of multiple units

- Automatic blood expiration notifications

- Payment between hospitals for blood transfers


### Known problems
- If browser not maximized, navbar sometimes gets cut off at the bottom
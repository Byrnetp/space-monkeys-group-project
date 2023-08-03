## CS 3308 Group Project
## Team 2: Space Monkeys
## Flask test code
## Last Update: David Hughes, 3 August 2023
## USAGE: python3 -m pytest

import os
import pytest
from bloodbank import app

@pytest.fixture
def client():

    app.config["TESTING"] = True
    app.testing = True

    client = app.test_client()
    yield client

# Test Blood Bank Entry page
def test_bloodbank(client):

    # Get HTML
    response = client.get("/bloodbank")

    # Ensure all expected elements are on the page
    assert b"<h1>Blood Bank Entry Page</h1>" in response.data
    assert b'<form id="bloodbankEntryForm" name="bloodbankEntryForm">' in response.data
    assert b'<input type="text" id="bloodbankName" name="bloodbankName">' in response.data
    assert b'<input type="text" id="bloodbankType" name="bloodbankType">' in response.data
    assert b'<input type="text" id="bloodbankCity" name="bloodbankCity">' in response.data
    assert b'<input type="submit" value="Submit">' in response.data

    # Form entry
    response = client.get("/bloodbank", data={
        "bloodBankName": "testBB",
        "bloodBankType": "testBB",
        "bloodBankCity": "testBB",
        "bloodBankState": "testBB",
    })
    assert response.status_code == 200

# Test Donor Entry page
def test_donor(client):

    # Get HTML
    response = client.get("/donor")

    # Ensure all expected elements are on the page
    assert b"<h1>Donor Entry Page</h1>" in response.data
    assert b'<form id="donorEntryForm" name="donorEntryForm">' in response.data
    assert b'<input type="text" id="donorName" name="donorName">' in response.data
    assert b'<select id="donorBloodType" name="donorBloodType">' in response.data
    assert b'<input type="submit" value="Submit">' in response.data

    # Form entry
    response = client.get("/donor", data={
        "donorName": "testDonor",
        "donorBloodType": "A+",
    })
    assert response.status_code == 200

# Test Patient Entry page
def test_patient(client):

    # Get HTML
    response = client.get("/patient")

    # Ensure all expected elements are on the page
    assert b"<h1>Patient Entry Page</h1>" in response.data
    assert b'<form id="patientEntryForm" name="patientEntryForm">' in response.data
    assert b'<input type="text" id="patientName" name="patientName">' in response.data
    assert b'<select id="patientBloodType" name="patientBloodType">' in response.data
    assert b'<input type="submit" value="Submit">' in response.data

    # Form entry
    response = client.get("/patient", data={
        "patientName": "testPatient",
        "patientBloodType": "A+",
    })
    assert response.status_code == 200

# Test Donation Entry page
def test_donation(client):

    # Get HTML
    response = client.get("/donation")

    # Ensure all expected elements are on the page
    assert b"<h1>Donation Entry Page</h1>" in response.data
    assert b'<form id="donationEntryForm" name="donationEntryForm">' in response.data
    assert b'<input list="donorNameChoices" id="donorName" name="donorName">' in response.data
    assert b'<input list="bloodBankNameChoices" id="bloodBankName" name="bloodBankName">' in response.data
    assert b'<input type="text" id="medicalProfessional" name="medicalProfessional">' in response.data
    assert b'<select id="quantity" name="quantity">' in response.data
    assert b'<input type="date" id="date" name="date">' in response.data
    assert b'<input type="submit" value="Submit">' in response.data

    # Form entry
    response = client.get("/donation", data={
        "donorName": "testDonor",
        "donorBloodType": "A+",
        "bloodBankName": "testBB",
        "medicalProfessional": "testMP",
        "quantity": 1,
        "date": "20230701 8:00:00",
    })
    assert response.status_code == 200

# Test Transfusion Entry page
def test_transfusion(client):

    # Get HTML
    response = client.get("/transfusion")

    # Ensure all expected elements are on the page
    assert b"<h1>Transfusion Entry Page</h1>" in response.data
    assert b'<form id="transfusionEntryForm" name="transfusionEntryForm">' in response.data
    assert b'<input list="patientNameChoices" id="patientName" name="patientName">' in response.data
    assert b'<input list="donationIDChoices" id="donationID" name="donationID">' in response.data
    assert b'<input list="bloodBankNameChoices" id="bloodBankName" name="bloodBankName">' in response.data
    assert b'<input type="text" id="medicalProfessional" name="medicalProfessional">' in response.data
    assert b'<select id="quantity" name="quantity">' in response.data
    assert b'<input type="date" id="date" name="date">' in response.data
    assert b'<input type="submit" value="Submit">' in response.data

    # Form entry
    response = client.get("/transfusion", data={
        "patientName": "testPatient",
        "patientBloodType": "A+",
        "donationID": 1,
        "bloodBankName": "testBB",
        "medicalProfessional": "testMP",
        "quantity": 1,
        "date": "20230701 8:00:00",
    })
    assert response.status_code == 200

# Test Details page
def test_detail(client):

    # Get HTML
    response = client.get("/detail")

    # Ensure menu and header elements are on the page
    assert b'<h1>Inventory Details</h1>' in response.data
    assert b'<div id="menu">' in response.data
    assert b'<h3>Menu</h3>' in response.data
    assert b'<label for="hospital">Choose a blood bank or hospital:</label>' in response.data
    assert b'<select id="hospital">' in response.data
    assert b'<div id="checkbox-container">' in response.data
    assert b'<label>Display: </label>' in response.data
    assert b'<input type="checkbox" id="donations" checked>' in response.data
    assert b'<label for="donations">Donations</label>' in response.data
    assert b'<input type="checkbox" id="transfusions" checked>' in response.data
    assert b'<label for="transfusions">Transfusions</label>' in response.data
    assert b'<input type="checkbox" id="incomingTransfers" checked>' in response.data
    assert b'<label for="incomingTransfers">Incoming Transfers</label>' in response.data
    assert b'<input type="checkbox" id="outgoingTransfers" checked>' in response.data
    assert b'<label for="outgoingTransfers">Outgoing Transfers</label>' in response.data
    
    # Ensure tables are on the page
    assert b'<div id="tablesContainer">' in response.data
    assert b'<div id="donationTable">' in response.data
    assert b'<h2>Donations</h2>' in response.data
    assert b'<th>Donation ID</th>' in response.data
    assert b'<th>Date & Time</th>' in response.data
    assert b'<th>Donor ID</th>' in response.data
    assert b'<th>Medical Professional</th>' in response.data
    assert b'<th>Amount</th>' in response.data
    assert b'<div id="transfusionTable">' in response.data
    assert b'<h2>Transfusions</h2>' in response.data
    assert b'<th>Transfusion ID</th>' in response.data
    assert b'<th>Date & Time</th>' in response.data
    assert b'<th>Donation ID</th>' in response.data
    assert b'<th>Patient ID</th> ' in response.data
    assert b'<th>Medical Professional</th>' in response.data
    assert b'<th>Amount</th>' in response.data
    assert b'<div id="incomingTransferTable">' in response.data
    assert b'<h2>Incoming Transfers</h2>' in response.data
    assert b'<th>Transfer ID</th>' in response.data
    assert b'<th>Date & Time</th>' in response.data
    assert b'<th>Donation ID</th>' in response.data
    assert b'<th>Sending Hospital ID</th>' in response.data
    assert b'<div id="outgoingTransferTable">' in response.data
    assert b'<h2>Outgoing Transfers</h2>' in response.data
    assert b'<th>Transfer ID</th>' in response.data
    assert b'<th>Date & Time</th>' in response.data
    assert b'<th>Donation ID</th>' in response.data
    assert b'<th>Recieving Hospital ID</th> ' in response.data

# Test the view donors page
def test_viewDonors(client):

    # Get HTML
    response = client.get("/view-donors")

    # Ensure the expeceted elements and data are displayed
    assert b'<h1>Donors</h1>' in response.data
    assert b'<hr>' in response.data
    assert b'<div id="tablesContainer">' in response.data
    assert b'<th>Donor ID</th>' in response.data
    assert b'<th>Name</th>' in response.data
    assert b'<th>Blood Type</th>' in response.data
    assert b'<td>1</td>' in response.data
    assert b'<td>Bugs Bunny</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>2</td>' in response.data
    assert b'<td>Daffy Duck</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>3</td>' in response.data
    assert b'<td>Porky Pig</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>4</td>' in response.data
    assert b'<td>Elmer Fudd</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>5</td>' in response.data
    assert b'<td>Tweety Bird</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>6</td>' in response.data
    assert b'<td>Yosemite Sam</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>7</td>' in response.data
    assert b'<td>Lola Bunny</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>8</td>' in response.data
    assert b'<td>Snow White</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>9</td>' in response.data
    assert b'<td>Tinker Bell</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>10</td>' in response.data
    assert b'<td>Cinderlla Castle</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>11</td>' in response.data
    assert b'<td>Ariel Mermaid</td>' in response.data
    assert b'<td>A-</td>' in response.data
    assert b'<td>12</td>' in response.data
    assert b'<td>Jasmine Magic</td>' in response.data
    assert b'<td>A-</td>' in response.data
    assert b'<td>13</td>' in response.data
    assert b'<td>Mulan Wall</td>' in response.data
    assert b'<td>O-</td>' in response.data
    assert b'<td>14</td>' in response.data
    assert b'<td>Belle Book</td>' in response.data
    assert b'<td>O-</td>' in response.data
    assert b'<td>15</td>' in response.data
    assert b'<td>Raya Dragon</td>' in response.data
    assert b'<td>AB+</td>' in response.data
    assert b'<td>16</td>' in response.data
    assert b'<td>Peter Pan</td>' in response.data
    assert b'<td>AB-</td>' in response.data
    assert b'<td>17</td>' in response.data
    assert b'<td>Merida Greene</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>18</td>' in response.data
    assert b'<td>Bruce Wayne</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>19</td>' in response.data
    assert b'<td>Clark Kent</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>20</td>' in response.data
    assert b'<td>Barry Allen</td>' in response.data
    assert b'<td>B-</td>' in response.data
    assert b'<td>21</td>' in response.data
    assert b'<td>Tony Stark</td>' in response.data
    assert b'<td>B-</td>' in response.data
    assert b'<td>22</td>' in response.data
    assert b'<td>Steve Rogers</td>' in response.data
    assert b'<td>B-</td>' in response.data

# Test the view Patients page
def test_viewPatients(client):

    # Get HTML
    response = client.get("/view-patients")

    # Ensure the expeceted elements and data are displayed
    assert b'<h1>Patients</h1>' in response.data
    assert b'<hr>' in response.data
    assert b'<div id="tablesContainer">' in response.data
    assert b'<table>' in response.data
    assert b'<th>Patient ID</th>' in response.data
    assert b'<th>Name</th>' in response.data
    assert b'<th>Blood Type</th>' in response.data
    assert b'<td>1</td>' in response.data
    assert b'<td>Arnold Artwood</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>2</td>' in response.data
    assert b'<td>Beatrice Berry</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>3</td>' in response.data
    assert b'<td>Clarence Coldwater</td>' in response.data
    assert b'<td>AB+</td>' in response.data
    assert b'<td>4</td>' in response.data
    assert b'<td>Drake Duckle</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>5</td>' in response.data
    assert b'<td>Elen Eagleton</td>' in response.data
    assert b'<td>A-</td>' in response.data
    assert b'<td>6</td>' in response.data
    assert b'<td>Frank French</td>' in response.data
    assert b'<td>B-</td>' in response.data
    assert b'<td>7</td>' in response.data
    assert b'<td>Gretchen Gamey</td>' in response.data
    assert b'<td>AB-</td>' in response.data
    assert b'<td>8</td>' in response.data
    assert b'<td>Harold Horton</td>' in response.data
    assert b'<td>O-</td>' in response.data
    assert b'<td>9</td>' in response.data
    assert b'<td>Irene Ibola</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>10</td>' in response.data
    assert b'<td>John Jamison</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>11</td>' in response.data
    assert b'<td>Katrina Kelly</td>' in response.data
    assert b'<td>AB+</td>' in response.data
    assert b'<td>12</td>' in response.data
    assert b'<td>Lawrence Lavender</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>13</td>' in response.data
    assert b'<td>Matthew McConaughey</td>' in response.data
    assert b'<td>A-</td>' in response.data
    assert b'<td>14</td>' in response.data
    assert b'<td>Natelie Nevers</td>' in response.data
    assert b'<td>B-</td>' in response.data
    assert b'<td>15</td>' in response.data
    assert b'<td>Orrvile Oggelthorpe</td>' in response.data
    assert b'<td>AB-</td>' in response.data
    assert b'<td>16</td>' in response.data
    assert b'<td>Pamela Parkinson</td>' in response.data
    assert b'<td>O-</td>' in response.data
    assert b'<td>17</td>' in response.data
    assert b'<td>Quinton Quizine</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>18</td>' in response.data
    assert b'<td>Raegan Rizzola</td>' in response.data
    assert b'<td>B+</td>' in response.data
    assert b'<td>19</td>' in response.data
    assert b'<td>Samuel Sanderson</td>' in response.data
    assert b'<td>AB+</td>' in response.data
    assert b'<td>20</td>' in response.data
    assert b'<td>Trinity Thompson</td>' in response.data
    assert b'<td>O+</td>' in response.data
    assert b'<td>21</td>' in response.data
    assert b'<td>Usef Unisone</td>' in response.data
    assert b'<td>A-</td>' in response.data
    assert b'<td>22</td>' in response.data
    assert b'<td>Virginia Vain</td>' in response.data
    assert b'<td>B-</td>' in response.data
    assert b'<td>23</td>' in response.data
    assert b'<td>Wayne Wellington</td>' in response.data
    assert b'<td>AB-</td>' in response.data
    assert b'<td>24</td>' in response.data
    assert b'<td>Xelia Xlan</td>' in response.data
    assert b'<td>O-</td>' in response.data
    assert b'<td>25</td>' in response.data
    assert b'<td>Yale Young</td>' in response.data
    assert b'<td>A+</td>' in response.data
    assert b'<td>26</td>' in response.data
    assert b'<td>Zena Zootopia</td>' in response.data
    assert b'<td>O+</td>' in response.data

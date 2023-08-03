## CS 3308 Group Project
## Team 2: Space Monkeys
## Flask test code
## Last Update: David Hughes, 3 August 2023
## USAGE: python3 test_bloodbank.py

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


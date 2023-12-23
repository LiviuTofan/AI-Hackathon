# Get data from firebase from user input about last added company and program data to generate emails, and save info into input.txt

import firebase_admin as fa
from firebase_admin import db
import json

def get_latest_data():
    # Initialize Firebase Admin SDK
    cred = fa.credentials.Certificate("C:\\Users\\liviu\\PycharmProjects\\Hackathon\\ai-discoverybot-firebase-adminsdk-hnav1-214de178dc.json")
    app = fa.initialize_app(credential=cred)

    ref = db.reference(url="https://ai-discoverybot-default-rtdb.europe-west1.firebasedatabase.app/")

    # Get data from Firebase
    firebase_data = ref.get()

    # Extract companyData and programData
    company_data = firebase_data.get("companyData", {})
    program_data = firebase_data.get("programData", {})

    # Get the last added company from companyData
    last_added_company_name = list(company_data.keys())[-1]
    last_added_company_data = company_data.get(last_added_company_name, {})

    # Combine data into a dictionary
    output_data = {
        "lastAddedCompany": {last_added_company_name: last_added_company_data},
        "latestProgramData": program_data
    }

    # Save data in input.txt
    with open("input.txt", "w") as output_file:
        json.dump(output_data, output_file, indent=2)

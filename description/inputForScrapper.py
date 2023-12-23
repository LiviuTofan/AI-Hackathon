# Get company URL and name from firebase an insert into companyURL.txt for scraper

import firebase_admin as fa
from firebase_admin import db
import json

def get_data_for_scrapper():
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

    # Extract only companyName and website from the last added company
    last_added_company_website = last_added_company_data.get("website", "")
    last_added_company_name = last_added_company_data.get("companyName", "")

    # Combine data into a dictionary
    output_data = {
        "lastAddedCompany": {
            "companyName": last_added_company_name,
            "website": last_added_company_website
        }
    }

    # Save data to input.txt
    with open("companyURL.txt", "w") as output_file:
        json.dump(output_data, output_file, indent=2)

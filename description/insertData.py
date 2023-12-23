# Update generated by AI description and Industry Field into firebase.

from firebase_admin import db
import json

def update_description_industry_inFirebase(file_path="description.txt", database_url="https://ai-discoverybot-default-rtdb.europe-west1.firebasedatabase.app/"):

    ref = db.reference(url=database_url)
    firebase_data = ref.get()

    with open(file_path, "r") as file:
        file_content = file.read()

        # Parse JSON data from the file
        data = json.loads(file_content)

        # Get the last added company from companyData
        company_data = firebase_data.get("companyData", {})
        last_added_company_name = list(company_data.keys())[-1]

        # Check if the company exists in Firebase
        company_ref = ref.child("companyData").child(last_added_company_name)
        if company_ref.get():
            # Update data in Firebase for the last added company
            company_ref.update({
                "companyDescription": data.get("companyDescription", ""),
                "selectedIndustry": data.get("selectedIndustry", "")
            })
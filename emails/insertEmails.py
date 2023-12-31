# Insert the generated mails into firebase.

import firebase_admin as fa
from firebase_admin import db
import json

# Function that updates data in firebase with data from emails.txt file which are Promotional & Reward emails generated by AI.
def update_data_in_firebase(file_path="emails.txt", database_url="https://ai-discoverybot-default-rtdb.europe-west1.firebasedatabase.app/", app_name="hackathon-app"):
    # Check if the app is already initialized
    if not fa._apps.get(app_name):
        # Initialize Firebase Admin SDK
        cred = fa.credentials.Certificate("C:\\Users\\liviu\\PycharmProjects\\Hackathon\\ai-discoverybot-firebase-adminsdk-hnav1-214de178dc.json")
        app = fa.initialize_app(credential=cred, name=app_name)

    # Reference
    ref = db.reference(url=database_url)

    with open(file_path, "r") as file:
        file_content = file.read()

    data = json.loads(file_content)

    # Update data in Firebase
    for key, value in data.items():
        ref.child(key).update(value)

if __name__ == "__main__":
    update_data_in_firebase()
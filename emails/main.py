from emails.inputData import get_latest_data
from emails.mails import generate_emails
from insertEmails import update_data_in_firebase

get_latest_data()

# Read user input from input.txt
with open('input.txt', 'r', encoding='utf-8') as file:
    user_input = file.read()

# Generate emails based on user input
emails = generate_emails(user_input)

# Write generated emails to emails.txt
with open('emails.txt', 'w', encoding='utf-8') as file:
    file.write(emails)

update_data_in_firebase()

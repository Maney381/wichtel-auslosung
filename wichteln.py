from dotenv import load_dotenv
import os
from utils.contacts_utils import load_contacts, derange
from resources import email_config
from utils.email_utils import EmailHandler

load_dotenv()
# Access the variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
photo_file = "resources/weihnachtsmann.jpg"
subject = email_config.subject


contacts = load_contacts('resources/contacts.json')['contacts']
shuffled_contacts = derange(contacts)

# Initialize the EmailHandler
email_handler = EmailHandler(
    smtp_server=SMTP_SERVER,
    smtp_port=SMTP_PORT,
    sender_email=EMAIL_ADDRESS,
    sender_password=EMAIL_PASSWORD
)
# Connect to the SMTP server
email_handler.connect()

for index, contact in enumerate(contacts):
    wichtel_contact = shuffled_contacts[index]

    # Create the email
    recipient_name = contact['name']
    recipient_email = contact['email']

    other_name = wichtel_contact['name']
    msg = email_handler.create_message(
        recipient_name=recipient_name,
        other_name=other_name,
        recipient_email=recipient_email,
        photo_file=photo_file,
        subject=subject,
        body_template=email_config.get_body,
    )

    # Send the email
    email_handler.send_mail(recipient_name, recipient_email, msg)

# Disconnect from the SMTP server
email_handler.disconnect()
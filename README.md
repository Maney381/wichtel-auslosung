# Wichtel Auslosung

This project helps manage a **Secret Santa (Wichteln)** event by randomly assigning participants to each other and sending personalized emails. The system will take a list of participants, randomly pair them up, and send an email to each participant with the name of their Secret Santa partner.

## Features

- Randomly assigns participants to each other (ensuring no one is assigned to themselves).
- Sends an email to each participant with the name of their assigned "Wichtelpartner" (Secret Santa).
- Option to attach a personalized photo to each email.
- Configurable email subject, body, and other settings via a `.env` file (not tracked in the repo for security reasons).
- Easily configurable for different Secret Santa events.

## Installation

### Prerequisites
- Email account (for sending emails) or another SMTP server (for example gmail account with 2FA & App Password)

1. Create a `.env` file in the root of the project to store sensitive information (like email credentials):

   ```bash
    EMAIL_ADDRESS=your_email
    EMAIL_PASSWORD=your_password
    SMTP_SERVER=your_smtp_server
    SMTP_PORT=your_port
   ````

2. (Optional) If you need to change the subject or body of the email, you can modify the `email_config.py` file.
3. (Optional) You can uplaod an photo (.jpg) into the resources folder, which will be handled as an attachment to the email.
## Usage

1. Update the `contacts.json` file with the names and email addresses of your participants.
2. Run the script to generate the pairings and send emails:

   ```bash
   python wichteln.py
   ```

3. Each participant will receive an email with their assigned Secret Santa partner and a personalized message.

## Contributing
If you'd like to contribute to the project, feel free to submit a pull request. All contributions are welcome!
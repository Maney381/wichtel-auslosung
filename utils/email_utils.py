from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email import encoders
from email.mime.base import MIMEBase
import os
import smtplib

class EmailHandler:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the EmailHandler with SMTP server details and sender credentials.
        
        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            sender_email (str): Email address of the sender.
            sender_password (str): Password or app-specific password for the sender email.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.server = None

    def connect(self):
        """
        Connect to the SMTP server and log in.
        """

        self.server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        self.server.login(self.sender_email, self.sender_password)
        print("Connected to SMTP server.")

    def disconnect(self):
        """
        Disconnect from the SMTP server.
        """
        if self.server:
            self.server.quit()
            print("Disconnected from SMTP server.")

    def add_photo(self, msg, photo_file):
        """
        Add a photo attachment to the email message.
        
        Args:
            msg (MIMEMultipart): The email message object.
            photo_file (str): Path to the photo file to attach.
        
        Returns:
            MIMEMultipart: The email message with the photo attached.
        """
        if os.path.isfile(photo_file):
            with open(photo_file, "rb") as file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(photo_file)}",
            )
            msg.attach(part)
        else:
            print(f"Warning: Photo file '{photo_file}' not found. No attachment will be added.")
        return msg

    def create_message(self, recipient_name, other_name, recipient_email, photo_file, subject, body_template):
        """
        Create an HTML email message with optional photo attachment.
        
        Args:
            recipient_name (str): Name of the recipient.
            other_name (str): Name of the recipient's secret partner.
            recipient_email (str): Recipient's email address.
            photo_file (str): Path to the photo file to attach.
            subject (str): Email subject.
            body_template (callable): A function or template to generate the email body.
        
        Returns:
            MIMEMultipart: The formatted email message.
        """
        # Generate the email body
        html_body = body_template(recipient_name, other_name)
        
        # Create the email object
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html"))

        # Add the photo attachment
        msg = self.add_photo(msg, photo_file)

        return msg

    def send_mail(self, recipient_name, recipient_email, msg):
        """
        Send an email.
        
        Args:
            recipient_name (str): Name of the recipient.
            recipient_email (str): Email address of the recipient.
            msg (MIMEMultipart): The email message to send.
        """
        self.server.sendmail(self.sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_name} <{recipient_email}>")
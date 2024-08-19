# Import the necessary modules
import smtplib
from email.mime.text import MIMEText

# Configuration
smtp_server = "smtp.gmail.com"  # Gmail SMTP server
port = 587  # Port number for TLS encryption
login = "shair914@gmail.com"  # Your Gmail address
password = "Get a password from Gmail"  # Your Gmail app-specific password

sender_email = "shair914@gmail.com"  # Sender's email address
receiver_email = "salmonzoor@gmail.com"  # Receiver's email address

# Plain text content
text = """\
Type Message Here!
"""

# Create a MIMEText object to construct the email
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"  # Set the email subject
message["From"] = sender_email  # Set the sender's email address
message["To"] = receiver_email  # Set the receiver's email address

# Send the email using SMTP
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Secure the connection using TLS encryption
        server.login(login, password)  # Login to the SMTP server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
    print('Sent')  # Print a success message
except Exception as e:
    print(f"An error occurred: {e}")  # Print an error message if something goes wrong
"""
README
Simple Email Sender
Description
This script sends a plain text email using the Simple Mail Transfer Protocol (SMTP). It uses the smtplib library to connect to the Gmail SMTP server and the email.mime.text module to construct the email.
Configuration
smtp_server: The SMTP server address (e.g., smtp.gmail.com)
port: The port number for TLS encryption (e.g., 587)
login: Your Gmail address
password: Your Gmail app-specific password
sender_email: The sender's email address
receiver_email: The receiver's email address
Usage
Replace the login and password variables with your Gmail address and app-specific password.
Replace the sender_email and receiver_email variables with the desired email addresses.
Type your message in the text variable.
Run the script to send the email.
Note
Make sure to enable "Less secure apps" in your Google account settings to allow the script to access your Gmail account.
You can also use other SMTP servers and email providers by changing the smtp_server and port variables.
"""
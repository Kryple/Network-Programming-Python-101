import email.message
import smtplib
import poplib
import imaplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email(sender_email, receiver_email, subject, body):
    """Sends an email using SMTP.
  
    Args:
      sender_email: The sender's email address.
      receiver_email: The receiver's email address.
      subject: The subject of the email.
      body: The body of the email.
  
    Raises:
      smtplib.SMTPException: If there's an error sending the email.
    """

    # Create a message object
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Connect to the SMTP server (replace with your SMTP server details)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail(sender_email, receiver_email, msg.as_string())

# SMTP_SERVER = "smtp.gmail.com"
SMTP_SERVER = "aspmx.l.google.com"
SMTP_PORT = 25 #587
    
    
def send_email_2(sender_email, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['To'] = receiver_email
    msg['From'] = sender_email
    
    tempSubject = input("Enter subject: ")
    msg['Subject'] = subject
    
    message = input('Enter message: ')
    part = MIMEText('text', 'plain')
    part.set_payload(body)
    msg.attach(part)

    #Create session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    
#     Send
    session.sendmail(sender_email, receiver_email, msg.as_string())





if __name__ == "__main__":
    sender_email = "ttnam957@gmail.com"
    receiver_email = "namwizard67@example.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."

    # send_email(sender_email, receiver_email, subject, body)
    send_email_2(sender_email, receiver_email, subject, body)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    sender_email = "akoiralaaa@gmail.com"
    receiver_email = "aabhu57shan@gmail.com"
    subject = "Daily Report"
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # Email body
    body = "Hello,\n\nThis is your daily report.\n\nBest regards,\nYour Name"
    msg.attach(MIMEText(body, 'plain'))
    # SMTP server configuration (for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "akoiralaaa@gmail.com"
    smtp_password = "A@dharshan6"
    # Establish a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    # Log in to the email account
    server.login(smtp_username, smtp_password)
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    # Quit the server
    server.quit()
# Schedule the script to run daily at a specific time (adjust as needed)
schedule.every().day.at("11:17").do(send_email)
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
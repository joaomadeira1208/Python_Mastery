# Not working

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "João Madeira"
message["to"] = "email"
message["subject"] = "This is a test"
message.attach(MIMEText("Body", "plain"))
message.ayyach(MIMEImage(Path("image.png").read_bytes()))

try:

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email", "password")
        smtp.send_message(message)
        print("Sent...")

except smtplib.SMTPAuthenticationError as e:
    print(f'Failed to send email: {e}')

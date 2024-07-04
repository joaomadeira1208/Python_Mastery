# Not working

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "João Madeira"
message["to"] = "email"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
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

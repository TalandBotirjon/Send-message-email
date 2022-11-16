from email.message import EmailMessage
import ssl
import smtplib
sender = 'Sender Email'
password = "Sender Password"
receiver = 'Receiver Email'

subject = "Message Subject."
body = """
Message Body 
"""

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    print("Email login...")
    smtp.login(sender, password)
    print("Login success")
    smtp.sendmail(sender, receiver, em.as_string())
    print("Send message success.")

import time
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import *
root = Tk()
root.title("Qr code Generator")
root.geometry('900x750')
root.configure(background='#d9ffb3', bg="#59b300")


def sent_message():
    sender = email_entry.get()
    password = password_entry.get()
    receiver = receiver_entry.get()
    subject = subject_entry.get()
    body = message_entry.get()
    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        # time.sleep(2)
        label_run.config(text="Login Check:")
        smtp.login(sender, password)
        # time.sleep(2)
        label_run.config(text="Success Login. Sending Message:")
        smtp.sendmail(sender, receiver, message.as_string())
        # time.sleep(2)
        label_run.config(text="Send Message :)")
        email_entry.delete(0, END)
        email_entry.insert(0, "")
        password_entry.delete(0, END)
        password_entry.insert(0, "")
        receiver_entry.delete(0, END)
        receiver_entry.insert(0, "")
        subject_entry.delete(0, END)
        subject_entry.insert(0, "")
        message_entry.delete(0, END)
        message_entry.insert(0, "")


label_email = Label(root, text="Sender Email:", background="#ccff99", font=('Helvetica', 16))
label_email.pack(pady=10)
email_entry = Entry(root, font=('Helvetica', 16), background="#ccff99", width=35)
email_entry.pack(pady=10)


label_receiver = Label(root, text="Receiver Email:", background="#ccff99", font=('Helvetica', 16))
label_receiver.pack(pady=10)
receiver_entry = Entry(root, font=('Helvetica', 16), background="#ccff99", width=35)
receiver_entry.pack(pady=10)

label_password = Label(root, text="Password Sender:", background="#ccff99", font=('Helvetica', 16))
label_password.pack(pady=10)
password_entry = Entry(root, font=('Helvetica', 16), background="#ccff99", width=20)
password_entry.pack(pady=10)

label_subject = Label(root, text="Subject: ", background="#ccff99", font=('Helvetica', 16))
label_subject.pack(pady=10)
subject_entry = Entry(root, font=('Helvetica', 16), background="#ccff99", width=40)
subject_entry.pack(pady=10)

label_message = Label(root, text="Message: ", background="#ccff99", font=('Helvetica', 16))
label_message.pack(pady=10)
message_entry = Entry(root, font=('Helvetica', 14), background="#ccff99", width=50)
message_entry.pack(pady=10)

button = Button(root, text="Sent message..", background="#59b300", command=sent_message, font=('Helvetica', 16))
button.pack(pady=10)

label_run = Label(root, text=":(", background="#ccff99", font=('Helvetica', 20))
label_run.pack(pady=10)
root.mainloop()

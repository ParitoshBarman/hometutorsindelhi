from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def sendEmailTest(messageText):
    # emailReceiver="barmanpari163@gmail.com"
    emailReceiver="noorajput.1314@gmail.com"
    emailSender = "eloanbajajfinserv@gmail.com"
    ePassword = "jfuzrnhhnpqbkpdm"
    smtpServerName = "smtp.gmail.com"
    subject = f"Website send Email Test {datetime.now()}"
    body =messageText

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServerName, 465, context=context) as smtp:
        smtp.login(emailSender, ePassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())


def sendEmail(subject, messageText, recver):
    emailReceiver="barmanpari163@gmail.com"
    # emailReceiver="noorajput.1314@gmail.com"
    emailSender = "contact@hometutorsindelhi.com"
    ePassword = "Pedagogyservices@85"
    smtpServerName = "smtpout.secureserver.net"
    subject = f"Contact message from Home Tutors In Delhi  {datetime.now()}"
    body = messageText

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServerName, 465, context=context) as smtp:
        smtp.login(emailSender, ePassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())


def sendEmailAws(subject, messageText, recver):
    emailReceiver="barmanpari163@gmail.com"
    
    emailSender = "contact@hometutorsindelhi.com"
    ePassword = "Pedagogyservices@85"
    smtpServerName = "smtpout.secureserver.net"
    subject = f"Contact message from Home Tutors In Delhi  {datetime.now()}"
    body = messageText

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServerName, 465, context=context) as smtp:
        smtp.login(emailSender, ePassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

# sendEmail("Subject", "This is message", "barmanpari163@gmail.com")

sendEmailAws("Subject", "This is message", "barmanpari163@gmail.com")


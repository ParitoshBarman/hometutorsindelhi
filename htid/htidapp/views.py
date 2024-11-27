from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from htidapp.models import ContactMessage
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from htidapp import whatsappcloud
import json
from django.views.decorators.csrf import csrf_exempt

mytoken = "hometutorsindelhitoken"

def sendEmail(subject, messageText, emailReceiver):
    # emailReceiver="barmanpari163@gmail.com"
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


# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email3 = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        cmsgdb = ContactMessage(fullname=fullname, email=email3, phone=phone, subject=subject, message=message)
        cmsgdb.save()

        whatsappcloud.sendText(f"Name: {fullname}\nEmail: {email3}\nPhone: {phone}\nTime: {cmsgdb.msgTime},{cmsgdb.msgdate}\n\nSubject: {subject}\nMessage:\n{message}\n\n\n\n\n\nGo To Message List https://www.hometutorsindelhi.com/admin/htidapp/contactmessage/", "919091467852")
        sendEmail(f"{subject}", f"Name: {fullname}\nEmail: {email3}\nPhone: {phone}\nTime: {cmsgdb.msgTime},{cmsgdb.msgdate}\n\nSubject: {subject}\nMessage:\n{message}\n\n\n\n\n\nGo To Message List https://www.hometutorsindelhi.com/admin/htidapp/contactmessage/", "barmanpari163@gmail.com")

        return render(request, "contact.html", {"backmsg":"Successfully Send your message. We will get back to you soon! Thank You!"})
    return render(request, "contact.html")

def service(request):
    return render(request, "service.html")
def teacher(request):
    return render(request, "teacher.html")
def privacypolicy(request):
    return render(request, "privacy-policy.html")
def termsandcondition(request):
    return render(request, "termsandcondition.html")
def pricing(request):
    return render(request, "pricing.html")
def classes(request):
    return render(request, "class.html")



@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        mode = request.GET.get("hub.mode")
        challenge = request.GET.get("hub.challenge")
        verify_token = request.GET.get("hub.verify_token")
        
        if mode and verify_token:
            if mode == "subscribe" and verify_token == mytoken:
                return HttpResponse(challenge, status=200)
            else:
                return HttpResponse(status=403)

        return HttpResponse(status=400)

    if request.method == 'POST':
        body_param = json.loads(request.body.decode('utf-8'))

        if body_param:
            if (body_param.get("entry") and 
                body_param["entry"][0].get("changes") and 
                body_param["entry"][0]["changes"][0].get("value") and 
                body_param["entry"][0]["changes"][0]["value"].get("messages") and 
                body_param["entry"][0]["changes"][0]["value"]["messages"][0]):

                phone_number_id = body_param["entry"][0]["changes"][0]["value"]["metadata"]["phone_number_id"]
                from_ = body_param["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
                msg_body = body_param["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

                # print(f"Phone number ID: {phone_number_id}")
                # print(f"From: {from_}")
                # print(f"Message body: {msg_body}")

                whatsappcloud.sendText(f"From: {from_}\nMessage: {msg_body}", "919091467852")
                return HttpResponse(status=200)

            return HttpResponse(status=404)
    return HttpResponse(status=405)
    




def base(request):
    return render(request, "base.html")
import requests
import json

url = "https://graph.facebook.com/v20.0/358554990685260/messages"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer EAARFP9GM4eQBO8ZAEWast3HIXRiB5qcbzZC0LWfthxmcnzrB1UB6jifiCSjNwMhcBiPZCcC6W9ivZAZBf4evdhN7DOQaDyZBR2PaCyxUfGTq0mqSRc6tLT5fxqvt3LjCC8UujieLs8jcG5SiVp9TZA34DjqMeCsjblfz1xgmBheZBTZASZAyeo1fZCuGH1b0OgU711kngZDZD'
}



def sendText(msg, number):
    payload = json.dumps({
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": f"{number}",
    "type": "text",
    "text": {
    "preview_url": True,
    "body": f"{msg}"
        }
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    

def sendTemplate(templateName, number):
    payload = json.dumps({
    "messaging_product": "whatsapp",
    "to": f"{number}",
    "type": "template",
    "template": {
        "name": f"{templateName}",
        "language": {
        "code": "en_US"
        }
    }
    })

    response = requests.request("POST", url, headers=headers, data=payload)


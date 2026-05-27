import requests
import json
API_KEY = ""


def send_sms(receptor, variables, pattern_code):
    url = "https://api2.ippanel.com/api/v1/sms/pattern/normal/send"
    payload = json.dumps({
        "code": pattern_code,
        "sender": "+983000505",
        "recipient": receptor,
        "variable": variables
    })
    headers = {
        'apikey': IPPANEL_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

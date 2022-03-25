import http.client
import json
from os import environ
from dotenv import load_dotenv
load_dotenv()

def build_payload(subject, content, to_email, from_email) -> dict:
    payload = json.dumps({
    "personalizations": [
        {
            "to":
            [
                {
                    "email": to_email
                }
            ]
        }
        ],
        "from": {
            "email": from_email
            },
        "subject": subject,
        "content": [
            {
                "type": "text/plain",
                "value": content
            }
        ]
    })
    return payload

def build_headers() -> dict:
    headers = {
        'Authorization': 'Bearer '+environ.get('MESSAGE_BEARER'),
        'Content-Type': 'application/json'
    }
    return headers

def send_message(subject, content, to_email, from_email):
    conn = http.client.HTTPSConnection(environ.get('MESSAGE_API_BASE'))
    conn.request("POST",
    environ.get('MESSAGE_API'),
    build_payload(subject, content, to_email, from_email),
    build_headers())
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_content(name, gender, content):
    final_message="Hi again{0}{1}, glad to see you again!\n\n".format(" Mr. " if gender=="male" else (" Ms. " if gender=="female" else " "), name)
    final_message+=content
    final_message+="\n\nThis message was sent by Evergreen, please don't answer back."
    return final_message
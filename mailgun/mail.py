import requests
from django.conf import settings


def send_mail(subject, body, sender, to):
    return requests.post(
        settings.MAILGUN_BASE_URL,
        auth=('api', settings.MAILGUN_API_KEY),
        data={'from': sender,
              'to': to,
              'subject': subject,
              'text': body
              })

def send_mass_mail(*args):
    for mail in args:
        try:
            subject, body, sender, to = mail
            yield(send_mail(subject, body, sender, to))
        except ValueError as e:
            print("Not Enough Values provided, expected 4")

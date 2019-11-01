import requests
from django.conf import settings


def send_mail(subject, body, sender, to, fail_silently=True):
    # Post a request to MailGun API, It will process it and mail it through it's system
    response =  requests.post(
        settings.MAILGUN_BASE_URL,
        auth=('api', settings.MAILGUN_API_KEY),
        data={'from': sender,
              'to': to,
              'subject': subject,
              'text': body
              })
    # If Response is not OK(200) show failed message
    if not fail_silently and response.status_code != 200:
        print("Failed to send mail to ", to, "\nSubject: ", subject, "\nBody: ", body)
        # TODO raise any error or log failed email.
    return response

def send_mass_mail(datatuples, fail_silently=True):
    for mail in datatuples:
        try:
            subject, body, sender, to = mail
            yield send_mail(subject, body, sender, to, fail_silently=fail_silently)
        except ValueError as e:
            print("Not Enough Values provided, expected 4")

import requests
from django.conf import settings


def send_mail(subject, body, to, sender=settings.EMAIL_HOST_USER, fail_silently=True):
    # Post a request to MailGun API, It will process it and mail it through it's system
    response = requests.post(
        settings.MAILGUN_BASE_URL,
        auth=('api', settings.MAILGUN_API_KEY),
        data={'from': sender,
              'to': to,
              'subject': subject,
              'text': body
              })
    # If Response is not OK(200) show failed message
    if not fail_silently and response.status_code != 200:
        # TODO raise any error or log failed email.
        pass
    return response


def send_mass_mail(datatuples, fail_silently=True):
    with requests.Session() as my_session:
        my_session.auth = ('api', settings.MAILGUN_API_KEY)
        for mail in datatuples:
            if len(mail) == 3:
                subject, body, to = mail
                sender = settings.EMAIL_HOST_USER
            elif len(mail) == 4:
                subject, body, to, sender = mail
            else:
                # TODO Log Error (Wrong Request)
                continue
            response = my_session.post(
                settings.MAILGUN_BASE_URL,
                data={'from': sender,
                      'to': to,
                      'subject': subject,
                      'text': body})
            print(response.status_code)
            # If Response is not OK(200) show failed message
            if not fail_silently and response.status_code != 200:
                # TODO raise any error or log failed email.
                pass
        my_session.close()

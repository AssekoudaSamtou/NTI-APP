import os

from sendgrid import Mail, SendGridAPIClient


def test(from_email, to_emails):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>'
    )
    try:
        sg = SendGridAPIClient("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")
        print(os.environ.get('SENDGRID_API_KEY'), "###############")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

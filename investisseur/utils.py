import os

from sendgrid import Mail, SendGridAPIClient


def test(to_emails):
    message = Mail(
        from_email="new.touch.investing@gmail.com",
        to_emails=to_emails,
        subject='Bienvenu(e) sur New Touch Investing',
        html_content='<strong>and easy to do anywhere, even with Python</strong>'
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        # print(os.environ.get('SENDGRID_API_KEY'), "###############")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

import os

from sendgrid import Mail, SendGridAPIClient


def send_welcome_mail(to):
    message = Mail(
        from_email="new.touch.investing@gmail.com",
        to_emails=to.email,
        subject='Bienvenu(e) sur New Touch Investing',
        html_content=f'<strong>Mot de passe temporaire: {to.init_password}</strong>'
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

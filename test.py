import smtplib
import ssl

sender_email = "rocketbot418@gmail.com"
receiver_email = "rocketbot418@gmail.com"
subject = "Your Subject Here"
body = "Hello, this is a test email sent from Python."
password = "Rocketbot122$"

context = ssl.create_default_context()

def send_email(sender_email, receiver_email, subject, body, password):
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, msg)

send_email(sender_email, receiver_email, subject, body, password)
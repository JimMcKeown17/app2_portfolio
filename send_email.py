# import smtplib, ssl
# host = 'smtp.gmail.com'
# port = 465
#
# username = "luncumopython@gmail.com"
# password = 'ixdbnlwutntsyekr'
#
# context = ssl.create_default_context()
# receiver = "luncumopython@gmail.com"
#
# # message = """
# # Hi!
# # How are you?
# Bye!
# """
#
# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(username, password)
#     server.sendmail(username, receiver, message)

from email.message import EmailMessage
import smtplib
import ssl

# The Gmail SMTP server we'll use to send the message.
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

# Our credentials for that server.
GMAIL_USERNAME = "luncumopython@gmail.com"

GMAIL_PASSWORD = 'ixdbnlwutntsyekr'


def send_email(from_email, subject, message):
    """
    Sends an email via the above SMTP server. All comms go through SSL.
    :param from_email: address of the sender.
    :param subject: subject for the message.
    :param message: the main text of the message.
    """
    # Encrypt conversation with email server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        # Construct the email.
        msg = EmailMessage()
        msg['From'] = from_email
        msg['To'] = GMAIL_USERNAME
        msg['Subject'] = subject
        msg.set_content(message)

        # Lick the stamp and send it!
        server.send_message(msg)
        server.quit()


subject = "This is not the greatest email in the world"
message = "No, this is just a tribute."

send_email('luncumopython@gmail.com', subject, message)
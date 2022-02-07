import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


def getAccount(dotenv_path=''):
    """
    Get the environment variables `GM_USERNAME` and `GM_PASSWORD` from the
    specified `.env` file and return as a tuple.

    example:
    `user, password = getAccount('./.env')`
    """
    if dotenv_path:
        load_dotenv(dotenv_path=dotenv_path)
    else:
        load_dotenv()
    return (os.getenv('GM_USERNAME'), os.getenv('GM_PASSWORD'))


def emailUpdate(subject, from_email, to_email, password, text, htmlText=''):
    """
    Email a message with the provided account details and message.

    Parameters
    ----------
    subject : str
        Email subject
    from_email : str
        Account to sign into
    to_email : str, list[str]
        Email recipient(s)
    password : str
        Password for account `from_email`
    text : str
        Plain text message to be sent
    htmlText : str
        Html alternative message for rich text formatting
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    msg.set_content(text)
    if htmlText:
        msg.add_alternative(htmlText, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(msg)

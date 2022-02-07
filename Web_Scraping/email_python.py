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
    if dotenv_path: load_dotenv(dotenv_path=dotenv_path)
    else: load_dotenv()
    return (os.getenv('GM_USERNAME'), os.getenv('GM_PASSWORD'))


def emailUpdate(subject,
                from_email,
                to_email,
                password,
                htmlText='',
                text=''):
    """
    Email data collected in the main function
    Parameters
    ----------
    data : dict[]
        List of dictionaries with title, link, and price of wishlist items
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    msg.set_content(text)
    msg.add_alternative(htmlText, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(msg)

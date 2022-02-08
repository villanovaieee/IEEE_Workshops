"""
Copyright 2021 The Villanova Chapter of the Institute of Electrical and
Electronics Engineers (IEEE)
This file is part of the IEEE_Workshops library.

The IEEE_Workshops libary is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

The IEEE_Workshops libary is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
the IEEE_Workshops library. If not, see <https://www.gnu.org/licenses/>.
"""
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

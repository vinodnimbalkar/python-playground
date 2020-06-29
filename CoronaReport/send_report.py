# import necessary packages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import requests
import os, shutil
from datetime import date
import schedule as sh
import time
from credentials import *

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TODAY_DATE = date.today().strftime('%d%m%Y')
REPORT_LINK = f'COVID-19_Report_dated_on_{TODAY_DATE}_NMMC.pdf'

if not os.path.exists('./Report'):
    os.makedirs('./Report')

def get_pdf_report():
    print("Download Starting...")
    downloadUrl = f'{URL}/{REPORT_LINK}'
    path = BASEDIR+"/Report/Corona.pdf"
    r = requests.get(downloadUrl)
    with open(path, 'wb') as f:
        f.write(r.content)
    print("Download complete")

def mail_report():
    print("Sending Mail in Progress...")
    subject = 'Today\'s Corona Report of Navi Mumbai'

    msg = MIMEMultipart()
    msg['From'] = USER_EMAIL
    msg['To'] = ", ".join(SENDER_EMAIL)
    msg['Subject'] = subject

    filename= ['Report/Corona.pdf']
    for f in filename:
        attachment = open(f,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+f)

        msg.attach(part)
    text = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        server.starttls()
        server.login(USER_EMAIL, USER_PASSWORD)

        server.sendmail(USER_EMAIL, SENDER_EMAIL, text)
        server.quit()
        print("Mail successfully send")
    except smtplib.SMTPException:
         print("Error: unable to send email")

def delete_report():
    path = BASEDIR+"/Report"
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Corona Report Deleted")

if __name__ == "__main__":
    sh.every().day.at("16:00").do(get_pdf_report)
    sh.every().day.at("16:05").do(mail_report)
    sh.every().day.at("16:06").do(delete_report)
    while True:
        sh.run_pending()
        time.sleep(1)

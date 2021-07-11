# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
import requests


def sendMail(mailContent):
    from main import smtp_url, smtp_port, smtp_from_address, smtp_password, smtp_to_address
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect(smtp_url, smtp_port)
    smtp.login(smtp_from_address, smtp_password)
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = smtp_from_address
    msg['subject'] = '船票Get'
    msg['to'] = smtp_to_address
    txt = email.mime.text.MIMEText(mailContent, 'HTML', 'utf-8')
    msg.attach(txt)
    smtp.sendmail(msg['from'], msg['to'], str(msg))


def mailGun(mailContent):
    from main import mailgun_domain_name, mailgun_api_key, mailgun_to_address
    return requests.post(
        "https://api.mailgun.net/v3/" + mailgun_domain_name + "/messages",
        auth=('api', mailgun_api_key),
        data={"from": "船票Get <mailmaster@" + mailgun_domain_name + ">",
              "to": [mailgun_to_address],
              "subject": "船票Get",
              "text": mailContent})

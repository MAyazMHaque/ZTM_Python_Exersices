import  smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
list = ['inbox.ayaz@outlook.com','ayazhaque8@gmail.com','inbox.sidrah@gmail.com']
email['from'] = 'inbox.dev.ayaz@gmail.com'
email['to'] = list
email['Subject'] = 'Email from Python program'

email.set_content(html.substitute({'name': 'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('inbox.dev.ayaz@gmail.com', 'zlcezplvmrmrwdux')
    smtp.send_message(email)
    print('all good boss!')

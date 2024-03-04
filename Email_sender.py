import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'LD Python'
email['to'] = 'xxxxxxxxx@gmail.com'
email['subject'] = 'Test Message pythons'


email.set_content('I am Python programmer What is the next step')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yyyyyyyyyy@gmail.com','ojchgfthxnmrminw')
    smtp.send_message(email)
    print('all done!')

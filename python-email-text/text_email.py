import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Email sending example using Python. It\'s Simple Text Message')

fromEmail = 'gmailaddress@gmail.com'
toEmail = 'gmailaddress@gmail.com'

msg['Subject'] = 'Simple Text Message'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromEmail, 'gmailaddress address's password')
s.send_message(msg)
s.quit()
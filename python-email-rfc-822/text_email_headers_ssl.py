import smtplib

from email.parser import BytesParser, Parser
from email.policy import default

headers = Parser(policy=default).parsestr(
	'From: Foo Bar <gmail@gmail.com>\n'
	'To: <gmail@gmail.com>\n'
	'Subject: Simple Text Message\n'
	'\n'
	'Email sending example using Python. It\'s Simple Text Message\n')

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

s.login('gmail@gmail.com', 'gmail\s password')
s.send_message(headers)
s.quit()
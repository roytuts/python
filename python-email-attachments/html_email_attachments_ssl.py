import smtplib

from email.message import EmailMessage
from email.utils import make_msgid

msg = EmailMessage()

asparagus_cid = make_msgid()
msg.set_content('This is a text message')
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Hello</p>
    <p>
		Here is an example of sending attachments in email using Python.        
    </p>
	<img src="cid:{asparagus_cid}" />
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

with open("sample.jpg", 'rb') as img:
	msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid=asparagus_cid)
	
with open("sample.pdf", 'rb') as fp:
	pdf_data = fp.read()
	ctype = 'application/octet-stream'
	maintype, subtype = ctype.split('/', 1)
	msg.add_attachment(pdf_data, maintype=maintype, subtype=subtype, filename='sample.pdf')

fromEmail = 'gmail@gmail.com'
toEmail = 'gmail@gmail.com'

msg['Subject'] = 'HTML message with attachments'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

s.login(fromEmail, 'gmail password')
s.send_message(msg)
s.quit()
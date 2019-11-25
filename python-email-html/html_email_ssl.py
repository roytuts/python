import smtplib

from email.message import EmailMessage
from email.utils import make_msgid

msg = EmailMessage()

asparagus_cid = make_msgid()
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Hello</p>
    <p>Here is an example of sending HTML email using Python. Please click on below link:
        <a href="https://www.roytuts.com/how-to-send-an-html-email-using-python/">
            Send an HTML email using Python
        </a>
    </p>
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

fromEmail = 'gmail@gmail.com'
toEmail = 'gmail@gmail.com'

msg['Subject'] = 'HTML Message'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

s.login(fromEmail, 'gmail password')
s.send_message(msg)
s.quit()
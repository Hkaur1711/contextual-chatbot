
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "ankitekart@gmail.com"
toaddr = "geekankit318@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input('Enter subject of the mail: ')
 
body = input('Enter your message: ')
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, input('Enter your password: '))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
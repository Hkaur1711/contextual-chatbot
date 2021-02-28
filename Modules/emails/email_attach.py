
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "ankitekart@gmail.com"
toaddr = "geekankit318@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input('Enter subject of the Email: ')
 
body = input('Enter body of the mail: ')
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "a.png"
attachment = open("C:\\Users\\ANKIT\\Downloads\\Downloads\\Wallpapers\\a.png", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, input('Enter your password: '))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
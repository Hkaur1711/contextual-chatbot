## assuming that the intent is already classified.

# initially working with only persons identified by the current extractor.

# very basic mail bot.

# author : A.M.D.Srinivas

from entity_extraction.entity_extractor import data_extractor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass


def main_dialog(input_query):
    de = data_extractor(input_data=input_query)
    entities = de.extract_entities()
    print(entities)
    persons_involved = []
    persons_mails = []
    for item in entities['entities']:
        if entities[item] == 'PERSON':
            persons_involved.append(item)
    for person in persons_involved:
        persons_mails.append(input('Please enter the email id  of {0}\t'.format(person)).strip())

    from_address = input("Enter your email id :\t").strip()
    password = getpass.getpass("Enter your password :\t")

    for mail in persons_mails:
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = mail
        msg['Subject'] = input('Enter subject of the mail: \t')

        body = input('Enter your message: \t ')
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, mail, text)
        server.quit()

main_dialog(input('Enter your command').strip())

import imaplib, email, os
import getpass
from entity_extraction import entity_extractor as ee

user = input("Enter your email address:\n").strip()   # changed for user input.
password = getpass.getpass("Enter your password:\t")  # changed for user input.
imap_url = 'imap.gmail.com'
#Where you want your attachments to be saved (ensure this directory exists) 
attachment_dir = os.getcwd() + '\\attachments'
# sets up the auth
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
# allows you to download attachments
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
#search for a particular email
def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data
#extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = auth(user,password,imap_url)
con.select('INBOX')

#result, data = con.fetch(b'10','(RFC822)')
#raw = email.message_from_bytes(data[0][1])
#print(get_body(raw))
#get_attachments(raw)


msgs = get_emails(search('FROM', input("Enter the mail address to be searcched:\n"), con))
for msg in msgs:
	cur_msg =get_body(email.message_from_bytes(msg[0][1])).decode('utf-8').split('--')[0].strip() # changed to remove signatures in mails.
	print(cur_msg)
	extractor = ee.data_extractor(cur_msg) # extract entities.
	data = extractor.extract_entities()
	extractor.pretty_print(data)
	#print(get_body(email.message_from_bytes(msg[0][1])))
    	#print(get_attachments(email.message_from_bytes(msg[0][1])))

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
from time import sleep
#account info
sleep(15)
to = $$$$@gmail.com'
gmail_user = '$$$$gmail.com'
gmail_password = 'paste ur gmail app password'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data=p.communicate()
split_data=data[0].split()
ipaddr=split_data[split_data.index(b'src')+1]
my_ip='Rpi ip today is %s' % ipaddr
msg=MIMEText(my_ip)
msg['Subject']= 'Pi IP address'
msg['From']= gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()

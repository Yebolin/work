import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import os
import socks


smtp_server='smtp.exmail.qq.com'
smtp_port=465
sender_email='baojing@1111111.com'
sender_pass='***yyy***'
receiver=['b****n@qq.com']

proxy_ip='172.26.**.**'
proxy_port=9999

socks.set_default_proxy(socks.HTTP, proxy_ip, proxy_port)
socks.wrap_module(smtplib)


def get_filename():
    DIR='/data/'
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if '.xlsx' in file:
                return (root, file)


client = smtplib.SMTP_SSL(smtp_server, smtp_port)
client.login(sender_email, sender_pass)

msg = MIMEMultipart()
#msg = MIMEText('测试内容', 'plain', 'utf-8')
msg['From'] = formataddr(["报表",sender_email])
#msg['To'] = formataddr(["FK", 'b***n@qq.com'])          
msg['Subject']="报表"

#正文
msg.attach(MIMEText('报表', 'plain', 'utf-8'))

# 附件处理
filename = os.path.join(*get_filename())
att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="'+ get_filename()[1] +'"'
msg.attach(att1)


client.sendmail(sender_email, receiver, msg.as_string())



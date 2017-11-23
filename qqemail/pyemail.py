import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.readConfig import TestReadConfigFile
def send_mail(sender,pwd,receiver, smtpserver,port, report_file):
    '''发送最新的测试报告内容'''
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化接口测试报告"
    msg["from"] = sender
    msg["to"] = pwd
    # 加上时间戳
    # msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    # 用户名密码
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('测试报告邮件已发送！')
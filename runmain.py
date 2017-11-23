from config.readConfig import TestReadConfigFile
from HTMLTestRunner3 import HTMLTestRunner
from qqemail.pyemail import send_mail
import time
import unittest
import os
path = os.getcwd()
def suite():
    dir_case = unittest.defaultTestLoader.discover(
        path + r'\testcase',
        pattern='*.py',
        top_level_dir=None
    )
    return dir_case
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time .localtime(time.time()))
def run_main():
    global filename
    filename = path + r'\report\Report_' + getNowTime() + '.html'
    re_open = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=re_open,
        title=u'自动化接口测试报告',
        description=u'自动化接口测试详情'
        )
    runner.run(suite())
    return filename
if __name__ == '__main__':
    run_main()
    email = TestReadConfigFile().get_email_info()
    smtp_server = email['smtp_server']
    port = email['port']
    sender = email['sender']
    pwd = email['pwd']
    receiver = email['receiver']
    new_report_file = filename
    send_mail(sender,pwd,receiver,smtp_server,port,new_report_file)
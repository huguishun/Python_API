import os
import configparser

current_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_path,'cfg.ini')
conf = configparser.ConfigParser()
conf.read(config_path,encoding="utf-8-sig")

class TestReadConfigFile:
    def get_email_info(self):
        email_dict = {}
        email_dict['smtp_server'] = conf.get('email','smtp_server')
        email_dict['port'] = conf.get('email', 'port')
        email_dict['sender'] = conf.get('email','sender')
        email_dict['pwd'] = conf.get('email','pwd')
        email_dict['receiver'] = conf.get('email','receiver')
        return email_dict

    def get_Excelsite(self):
        excelsite = conf.get('excel','excelsite')
        return excelsite

if __name__ == '__main__':
    test = TestReadConfigFile()
    print(test.get_email_info())
    print(test.get_Excelsite())
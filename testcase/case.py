import unittest
from config.readConfig import TestReadConfigFile
from HTMLTestRunner3 import HTMLTestRunner
from xl.read_Excel import readExcel
from api_wal.api import Response
class testTulin(unittest.TestCase):
	def setUp(self):
		print("接口测试开始")
	def tearDown(self):
		print("接口测试结束")
	def test_data(self):
		excel_site = TestReadConfigFile().get_Excelsite()
		excel = readExcel(excel_site)
		caseid = excel.getCaseid
		name = excel.getName
		api_url = excel.getApi
		data = excel.getData
		method = excel.getMethod
		code = excel.getCode
		rows = excel.getRows
		for i in range(0,rows-1):
			run_api = Response(method[i],api_url[i],data[i])
			apicode = run_api.getCode()
			if apicode['code'] == code[i] :
				print('{}、{}:测试成功。json数据为:{}'.format(i+1,name[i],apicode))
			else:
				print('{}、{}:测试失败'.format(i+1,name[i]))
if __name__ == '__main__':
	unittest.main(verbosity = 2)
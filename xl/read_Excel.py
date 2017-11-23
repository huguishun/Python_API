import xlrd
class readExcel(object):
	def __init__(self,path):
		self.path = path
	# 获取sheet
	@property
	def getSheet(self):
		try:
			book = xlrd.open_workbook(self.path)
		except Exception as e:
			print('路径不存在'),e
			return e
		else:
			sheet = book.sheet_by_index(0)
			return sheet
	# 获取行数
	@property
	def getRows(self):
		rows = self.getSheet.nrows
		return rows
	# 获取列数
	@property
	def getCol(self):
		col = self.getSheet.ncols
		return col
	# 每列值
	@property
	def getCaseid(self):
		TestCaseid = []
		for i in range(1,self.getRows):
			TestCaseid.append(self.getSheet.cell_value(i,0))
		return TestCaseid
	@property
	def getName(self):
		TestName = []
		for i in range(1,self.getRows):
			TestName.append(self.getSheet.cell_value(i,1))
		return TestName
	@property
	def getApi(self):
		TestApi = []
		for i in range(1,self.getRows):
			TestApi.append(self.getSheet.cell_value(i,2))
		return TestApi
	@property
	def getData(self):
		TestData = []
		for i in range(1,self.getRows):
			TestData.append(self.getSheet.cell_value(i,3))
		return TestData
	@property
	def getMethod(self):
		TestMethod = []
		for i in range(1,self.getRows):
			TestMethod.append(self.getSheet.cell_value(i,4))
		return TestMethod
	@property
	def getCode(self):
		TestCode = []
		for i in range(1,self.getRows):
			TestCode.append(self.getSheet.cell_value(i,5))
		return TestCode
import requests
import json
class Response(object):
	def __init__(self,method,api_url,data):
		self.method = method
		self.api_url = api_url
		self.data = data
	def getCode(self):
		try:
			if self.method == 'post':
				r =requests.post(self.api_url,data=json.dumps(eval(self.data)))
				code = r.status_code
				result = json.loads(r.text)
			elif self.method =='get':
				r =requests.get(self.api_url,params = self.data)
				code = r.status_code
				result = json.loads(r.text)
			return result
		except Exception as e:
			print(e)

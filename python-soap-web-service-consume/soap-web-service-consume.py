import http.client
import urllib.parse
import xml.dom.minidom

class soap_consumer:

	def __init__(self, msg, json=False):
		self.msg = msg
		self.json = json
	
	def envelope(self):
		if self.json:
			return self.msg
		else:
			doc = xml.dom.minidom.Document()
			env = doc.createElement('soap12:Envelope')
			env.setAttribute('xmlns:soap12', 'http://www.w3.org/2003/05/soap-envelope')
			env.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
			env.setAttribute('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
			
			#print(self.msg)
			
			#XML input request data
			rawdom = xml.dom.minidom.parseString(self.msg)		
			messagenode = rawdom.firstChild
			
			#Header
			header = doc.createElement('soap12:Header')
			env.appendChild(header)
			
			#Body
			body = doc.createElement('soap12:Body')
			body.appendChild(messagenode)
			
			env.appendChild(body)
			doc.appendChild(env)
			
			#print(doc.toxml('utf-8'))
			
			return doc.toxml('utf-8')
	
	def send_request(self, url, path, content_type, accept, https=True):
		data = self.envelope()
		
		#print(data)
		#print(len(data))
		
		headers = {"Content-type" : content_type, "Accept": accept, "Content-length": len(data)}
		conn = ''
		
		if https:
			conn = http.client.HTTPSConnection(url, 443)
		else:
			conn = http.client.HTTPConnection(url, 80)

		#print(conn)
		conn.request("POST", path, data, headers)
		
		response = conn.getresponse()
		resp_data = response.read()
		
		#print(resp_data)
		
		if response.status == 200:
			conn.close()
			return resp_data
		else:
			return 'Failed:' + str(response.status) + str(resp_data)

#XML request body
swsc = soap_consumer('<CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/"><Celsius>36</Celsius></CelsiusToFahrenheit>')
resp = swsc.send_request('www.w3schools.com', '/xml/tempconvert.asmx', 'application/soap+xml; charset=utf-8', 'text/xml')
print(resp)

#JSON request body
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
swsc = soap_consumer(params, True)
resp = swsc.send_request('bugs.python.org', '', 'application/x-www-form-urlencoded; charset=utf-8', 'text/plain')
print(resp)
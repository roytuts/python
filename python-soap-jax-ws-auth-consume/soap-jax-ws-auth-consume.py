import http.client
import xml.dom.minidom

class soap_consumer:

	def __init__(self, msg):
		self.msg = msg
	
	def envelope(self):
		doc = xml.dom.minidom.Document()
		env = doc.createElement('soapenv:Envelope')
		env.setAttribute('xmlns:soapenv', 'http://schemas.xmlsoap.org/soap/envelope/')
		env.setAttribute('xmlns:ser', 'http://service.authentication.ws.jax.roytuts.com/')
		
		#print(self.msg)
		
		#XML input request data
		rawdom = xml.dom.minidom.parseString(self.msg)		
		messagenode = rawdom.firstChild
		
		op = doc.createElement('ser:sayHello')
		op.appendChild(messagenode)
		
		#Header
		header = doc.createElement('soapenv:Header')
		env.appendChild(header)
		
		#Body
		body = doc.createElement('soapenv:Body')
		body.appendChild(op)
		
		env.appendChild(body)
		doc.appendChild(env)
		
		#print(doc.toxml('utf-8'))
		
		return doc.toxml('utf-8')
	
	def send_request(self, url, path, content_type, accept, user, pwd):
		data = self.envelope()
		
		#print(data)
		#print(len(data))
		
		headers = {"Content-type" : content_type, "Accept": accept, "Content-length": len(data), "username": user, "password": pwd}
		conn = http.client.HTTPConnection(url, 8888)

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

swsc = soap_consumer('<arg0>Soumitra</arg0>')
resp = swsc.send_request('localhost', '/jax-ws-auth/hello', 'text/xml; charset=utf-8', 'text/xml', 'user', 'pass')
print(resp)
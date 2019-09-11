from flask import Flask
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/rest-auth')
@auth.login_required
def get_response():
	return jsonify('You are an authenticate person to see this message')
	
@auth.verify_password
def authenticate(username, password):
	if username and password:
		if username == 'roy' and password == 'roy':
			return True
		else:
			return False
	return False
		
if __name__ == "__main__":
    app.run()
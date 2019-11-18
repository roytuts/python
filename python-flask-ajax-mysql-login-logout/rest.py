import dao
from app import app
from flask import jsonify, request, session
		
@app.route('/login', methods=['POST'])
def login():
	_json = request.json
	#print(_json)
	_username = _json['username']
	_password = _json['password']
	
	if _username and _password:
		user = dao.login(_username, _password)
		
		if user != None:
			session['username'] = user
			return jsonify({'message' : 'User logged in successfully'})

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})
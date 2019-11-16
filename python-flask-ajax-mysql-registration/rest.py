import dao
import json
from app import app
from flask import jsonify, request

@app.route('/signup', methods=['POST'])
def signup():
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_pwd = _json['password']
	
	if _email and _name and _pwd:
	
		user_exist = dao.user_exist(_email)
		
		if user_exist == True:
			resp = jsonify({'message' : 'User already registered'})
			resp.status_code = 409
			return resp
		else:		
			dao.register(_email, _name, _pwd)
			
			resp = jsonify({'message' : 'User registered successfully'})
			resp.status_code = 201
			return resp
	else:
		resp = jsonify({'message' : 'Bad Request - invalid parameters'})
		resp.status_code = 400
		return resp
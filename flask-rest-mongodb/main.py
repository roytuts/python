from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, flash, request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/add', methods=['POST'])
def add_user():
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_password = _json['pwd']
	# validate the received values
	if _name and _email and _password and request.method == 'POST':
		#do not save password as a plain text
		_hashed_password = generate_password_hash(_password)
		# save details
		id = mongo.db.user.insert({'name': _name, 'email': _email, 'pwd': _hashed_password})
		resp = jsonify('User added successfully!')
		resp.status_code = 200
		return resp
	else:
		return not_found()
		
@app.route('/users')
def users():
	users = mongo.db.user.find()
	resp = dumps(users)
	return resp
		
@app.route('/user/<id>')
def user(id):
	user = mongo.db.user.find_one({'_id': ObjectId(id)})
	resp = dumps(user)
	return resp

@app.route('/update', methods=['PUT'])
def update_user():
	_json = request.json
	_id = _json['_id']
	_name = _json['name']
	_email = _json['email']
	_password = _json['pwd']		
	# validate the received values
	if _name and _email and _password and _id and request.method == 'PUT':
		#do not save password as a plain text
		_hashed_password = generate_password_hash(_password)
		# save edits
		mongo.db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'pwd': _hashed_password}})
		resp = jsonify('User updated successfully!')
		resp.status_code = 200
		return resp
	else:
		return not_found()
		
@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
	mongo.db.user.delete_one({'_id': ObjectId(id)})
	resp = jsonify('User deleted successfully!')
	resp.status_code = 200
	return resp
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
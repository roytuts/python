import visitor
from app import app
from flask import jsonify	
	
@app.before_request
def do_something_when_a_request_comes_in():
	visitor.track_visitor()

@app.route('/')
def home():
	return jsonify({'msg' : 'hello'})

		
if __name__ == "__main__":
    app.run()
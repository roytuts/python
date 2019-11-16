import rest
from app import app
from flask import render_template

@app.route('/')
def home():
	return render_template('signup.html')
		
if __name__ == "__main__":
    app.run()
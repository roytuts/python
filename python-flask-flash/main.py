from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def app_session():
	#flash('This is a flash message')
	#flash('This is a flash error message', 'error')
	#flash('This is a flash success message', 'success')
	
	return render_template('template.html')


if __name__ == "__main__":
    app.run()
from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def app_session():	
	#session['msg'] = 'Hello'
	session.modified = True
	
	#session['msg'] = 'Hello, Soumitra'
	#print(session.get('msg'))
	
	#session.pop('msg')
	#print(session.get('msg'))
	
	#session['hi'] = 'Hi'
	#session['hello'] = 'Hello'
	
	#for key, val in session.items():
		#print(key + ' -> ' + val)
		#print(key, ' -> ', val)
		
	#session.clear()
	
	#itemArray = {'name' : 'Soumitra', 'email' : 'soumitra@roytuts.com', 'address' : 'Earth'}
	#session['item'] = itemArray
	
	#if 'item' in session:
	#	session['item'].pop('name')
	
	#session.pop('item')
	
	#if 'item' in session:
	#	for key, val in session['item'].items():
	#		print(key + ' -> ' + val)
	
	itemNestedArray = { 'key' : {'name' : 'Soumitra', 'email' : 'soumitra@roytuts.com', 'address' : 'Earth'}}
	session['item'] = itemNestedArray
	
	if 'item' in session:
		for item in session['item'].items():
			print(item)
	
	session['item'].pop('key')
	
	if 'item' in session:
		for item in session['item'].items():
			print(item)
	
	return render_template('template.html')


if __name__ == "__main__":
    app.run()
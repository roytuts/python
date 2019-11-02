from app import app
from flask import render_template
from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/testimonials')
def testimonials():
	return render_template('testimonials.html')
	
@app.route('/contact')
def contact():
	return render_template('contact.html')
	
@app.route('/products')
def products():
	return render_template('products.html')	
		
if __name__ == "__main__":
    app.run()
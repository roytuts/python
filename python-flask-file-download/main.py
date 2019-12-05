from app import app
from flask import Flask, send_file, render_template
	
@app.route('/')
def upload_form():
	return render_template('download.html')

@app.route('/download')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = "simple.docx"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run()
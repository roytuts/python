from app import app
from flask import jsonify, request, render_template
		
@app.route('/google-charts/pie-chart')
def google_pie_chart():
	data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
	#print(data)
	return render_template('pie-chart.html', data=data)
		
if __name__ == "__main__":
    app.run()
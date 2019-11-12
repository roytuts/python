from flask import request, session

DNT_TRACK = True #False
IGNORE_IPS = set(['127.0.0.1'])

def is_tracking_allowed():
	#print(request.headers)
	if 'DNT' in request.headers and request.headers['DNT'] == 1:
		return False
	if request.remote_addr in IGNORE_IPS:
		return False
	return True

def track_session():
	if 'track_session' in session and session['track_session'] == True:
		return True
	else:
		return False
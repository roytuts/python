import config
import pymysql
from db import mysql
from flask import request, session

def track_visitor():
	if not config.is_tracking_allowed():
		return
	else:		
		ip_address = request.remote_addr
		requested_url = request.url
		referer_page = request.referrer
		page_name = request.path
		query_string = request.query_string
		user_agent = request.user_agent.string
				
		if config.track_session():
			log_id = session['log_id'] if 'log_id' in session else 0
			no_of_visits = session['no_of_visits']
			current_page = request.url
			previous_page = session['current_page'] if 'current_page' in session else ''
			
			if previous_page != current_page:
				
				log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, no_of_visits)
		else:			
			conn = None
			cursor = None
			
			session.modified = True
			
			try:				
				conn = mysql.connect()
				cursor = conn.cursor()
				
				log_id = log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent)
				
				#print('log_id', log_id)
				
				if log_id > 0:				
					sql = 'select max(no_of_visits) as next from visits_log limit 1'
					
					conn = mysql.connect()
					cursor = conn.cursor(pymysql.cursors.DictCursor)
					
					cursor.execute(sql)
					row = cursor.fetchone()
					
					count = 0
					if row['next']:
						count += 1
					else:
						count = 1
					
					sql = 'UPDATE visits_log set no_of_visits = %s WHERE log_id = %s'
					data = (count, log_id,)
					
					cursor.execute(sql, data)
					
					conn.commit()
					
					session['track_session'] = True
					session['no_of_visits'] = count
					session['current_page'] = requested_url				
				else:
					session['track_session'] = False
			except Exception as e:
				print(e)
				session['track_session'] = False
			finally:
				cursor.close()
				conn.close()
				
def log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, no_of_visits=None):
	sql = None
	data = None
	conn = None
	cursor = None
	log_id = 0
	
	if no_of_visits == None:
		sql = "INSERT INTO visits_log(no_of_visits, ip_address, requested_url, referer_page, page_name, query_string, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s)"
		data = (no_of_visits, ip_address, requested_url, referer_page, page_name, query_string, user_agent,)
	else:
		sql = "INSERT INTO visits_log(ip_address, requested_url, referer_page, page_name, query_string, user_agent) VALUES(%s, %s, %s, %s, %s, %s)"
		data = (ip_address, requested_url, referer_page, page_name, query_string, user_agent,)
	
	try:				
		conn = mysql.connect()
		cursor = conn.cursor()
		
		cursor.execute(sql, data)
		
		conn.commit()
		
		log_id = cursor.lastrowid
		
		return log_id
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# -*- coding: UTF-8 -*-
import datetime, time
from datetime import date
import urllib, json
import io  
import os
import subprocess
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


debug = True
path=os.path.dirname(os.path.abspath(__file__))
print("work on:" + path)
def print_f(string):
	print encode_utf8(string)
def encode_utf8(string):
	return string.encode('utf-8')
 
def decode_utf8(string):
	return unicode(string, encoding='utf-8')


def time_in_range(start, end, x):
	"""Return true if x is in the range [start, end]"""
	if start <= end:
		return start <= x <= end
	else:
		return start <= x or x <= end

def starting_work():
	start = datetime.time(7, 51, 0)
	end   = datetime.time(8, 3, 0)
	current = datetime.datetime.now().time()
	return time_in_range(start, end, current)

def getting_off_work():
	start = datetime.time(17, 1, 0)
	end   = datetime.time(17, 13, 0)
	current = datetime.datetime.now().time()
	return time_in_range(start, end, current)

def idle_time_range():
	start = datetime.time(18, 0, 0)
	end   = datetime.time(23, 50, 0)
	current = datetime.datetime.now().time()
	return time_in_range(start, end, current)

def is_weekday(today):
	day = datetime.datetime.strptime(str(date.today()), '%Y-%m-%d').weekday()
	if (day<5):
		return True
	else:
		return False

def today_event():
	# from website
	#url = "http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000077-002"
	#response = urllib.urlopen(url)
	#data = json.loads(response.read())
	# form file
	data = json.load(io.open('./calendar.json','r', encoding='utf8'))
	current_time = datetime.datetime.now().strftime('%H:%M:%S')
	#dash(-) for Unix and hash(#) for Windows
	today = date.today().strftime('%Y/%#m/%#d')
	events = data['result']['records'];
	today_event = ''
	#today='2013/2/23' #補假
	#today='2013/2/28' #放假
	for event in events:
		if (event.get('date') == today):
			today_event = event
	return today_event

def is_working_day(event, today):
	if(event == ''):
		if(is_weekday(today)):
			return True
	else:
		if (event['isHoliday'] == u'是'):
			return False
		else:
			return True

while(True):
	current_time = datetime.datetime.now().strftime('%H:%M:%S')
	today = date.today().strftime('%Y/%m/%d')
	day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
	day = datetime.datetime.strptime(str(date.today()), '%Y-%m-%d').weekday()
	event =today_event()
	filename = date.today().strftime('%Y-%m-%d') + '.txt'
	log_file = open(path+'\\logs\\'+filename, "a")
	log_file.write('-----------------------\n')
	log_file.write(today+' '+day_name[day]+ ' '+current_time+'\n')
	if(event != ''):
		log_file.write(event['date']+' '+event['name']+'('+event['holidayCategory']+'):'+event['description']+'\n')
	if(is_working_day(event, today)):
		cmd=''
		if(starting_work()):
			log_file.write('Sign up for working.\n')
			cmd = path+r'\signup.bat '+path
		if(getting_off_work()):
			log_file.write('Sign out for leaving.\n')
			cmd = path+r'\leave.bat '+path
		if(idle_time_range()):
			log_file.write('Testing.\n')
			cmd = path+r'\test.bat '+path
		if (cmd !=''):
			log_file.write(cmd+'\n')
			subprocess.call(cmd.split())

	else:
		log_file.write('Today is holiday.\n')
	log_file.close()
	#30s~120s
	interval = 61*random.randint(7,8)
	print('robot running, waiting for ' + str(interval/60) +' mins ' + str(interval%60) + ' secs')
	time.sleep(interval)

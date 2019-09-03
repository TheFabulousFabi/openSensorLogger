import urllib.request, json, csv 
import os.path, re
import sched, time
import datetime
import threading

def get_data(ip):
	#get the Data
	url = urllib.request.urlopen('http://127.0.0.1:8085/data.json')
	return json.loads(url.read().decode())

def get_entries(dick):
	child = dick.get("Children")

	if(len(child) > 0):
		for i in range(0, len(child)):
			get_entries(child[i])
	else:
		if(dick.get("Value") != ""):
			sensorValues.append([dick.get("Text"),dick.get("Value")])

def transpose(dick):
	temp = []	
	outConv =[]
	# Transponieren 
	for i in range(len(sensorValues[0])):
		for j in range(len(sensorValues)):
			x = re.search(r"[0-9]+", sensorValues[j][i])
			if(x and  i != 0):
				temp.append(x.group())
				continue
			temp.append(sensorValues[j][i])
		outConv.append(temp)
		temp = []
	return outConv

def start():

	global sensorValues
	sensorValues=[]
	data = get_data(2)
	get_entries(data)
	
	outConv = transpose(sensorValues)

	pc_id = data.get("Children")[0].get("Text")
	now = datetime.datetime.now()
	filename = "{}_{}_{}_{}.csv".format(pc_id,now.year,now.month,now.day)

	#CSV header nur schreiben wenn der file neu erstellt wird
	if(os.path.isfile(filename)):
		outConv.pop(0)

	#fuck this shit
	with open(filename,"a",newline='') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=';')
		filewriter.writerows(outConv)
	#threading.Timer(1.0, start).start()

if __name__ == '__main__':
	start()

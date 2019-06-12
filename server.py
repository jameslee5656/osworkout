import socket
from _thread import *
import threading
import json

print_lock = threading.Lock() 

def addlist(addlist):
	with open('data.txt','r') as json_file:  
		try :
			data = json.load(json_file)
		except(TypeError, ValueError) as e:
			print(str(e))
			print('there is something wrong')
			pass
	index = list(data.keys())
	data[str(int(index[-1]) + 1)] = [{'string':addlist[1]}]
	with open('data.txt', 'w') as outfile:  
		json.dump(data, outfile)

def editlist(datalist):
	with open('data.txt','r') as json_file:  
		try :
			data = json.load(json_file)
		except(TypeError, ValueError) as e:
			print(str(e))
			print('there is something wrong')
			pass
	data[str(datalist[1])][0]['string'] = datalist[2]
	with open('data.txt', 'w') as outfile:  
		json.dump(data, outfile)

def threaded(c):
	while True:
		data = c. recv(1024)
		if not data:
			print('Bye')
			print_lock.release()
			break
		print('We catch it')
		data = data.decode("utf-8") 
		datalist = data.split(':')
		if datalist[0] == 'add':
			addlist(datalist)
		if datalist[0] == 'edit':
			editlist(datalist)
		c.send(b'We catch it')
	c.close()

def Main():
	host = ""
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to post", port) 
	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True:
		# establish connection with client 
		c, addr = s.accept() 
		# lock acquired by client 
		print_lock.acquire()
		print('Connected to :', addr[0], ':', addr[1]) 
		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 

	s.close()
if __name__ == '__main__': 
	data = {'1' : [{'string': "test"}]}
	with open('data.txt', 'w') as outfile:  
	    json.dump(data, outfile)
	Main() 
	
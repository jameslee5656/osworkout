import json
def addlist(addlist):
	with open('data.txt','r') as json_file:  
		try :
			data = json.load(json_file)
		except(TypeError, ValueError):
			print('there is something wrong')
			pass
	index = list(data.keys())
	data[str(int(index[-1]) + 1)] = {'string':addlist}
	with open('data.txt', 'a') as outfile:  
		json.dump(data, outfile)
 #    	

data = {'1' : {'string': "test"}}
with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
addlist('hello')


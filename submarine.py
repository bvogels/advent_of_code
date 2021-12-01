import queue

q = queue.Queue()


def loadData():
	with open('data', 'r') as data:
		lines = data.readlines()
		for line in lines:
			q.put(int(line))
			
def increases():
	inc = 0
	x = 0
	y = 0
	while q.empty() is False:
		if x == 0:
			x = q.get()
		y = q.get()
		if x < y:
			inc += 1
		x = y
	print("Increases: ", inc)




if __name__ == "__main__":
	loadData()
	increases()
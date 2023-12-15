class Queue:
	def __init__(self):
		self.values = []

	def enqueue(self,value):
		self.values.append(value)

	def dequeue(self):
		pop = self.values[0]
		self.values.remove(pop)
		return pop

	def peek(self):
		return self.values[0]

	def peeklast(self):
		return self.values[len(self.values)-1]

	def isEmpty(self):
		return len(self.values)==0

class POPQueue:
	def __init__(self):
		self.innerQueue = Queue()

	def enqueue(self,value):
		self.innerQueue.enqueue(value)

	def dequeue(self):
		pop = []
		while not self.innerQueue.isEmpty():
			pop.append(self.innerQueue.dequeue())
		return pop

	def peek(self):
		return self.innerQueue.peek()

	def peeklast(self):
		return self.innerQueue.peeklast()

	def isEmpty(self):
		return self.innerQueue.isEmpty()

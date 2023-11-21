class Queue:
	def __init__(self):
		self.values = []

	def enqueue(self,value):
		self.values.append(value)

	def dequeue(self):
		pop = self.values[0]
		# this only works under the assumption that
		# the objects we sort are all different
		# this is built for permutations of whole numbers
		self.values.remove(pop)
		return pop

	def peek(self):
		return self.values[0]

	def peeklast(self):
		return self.values[len(self.values)-1]

	def isEmpty(self):
		return len(self.values)==0

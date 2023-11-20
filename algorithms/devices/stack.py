from queue import LifoQueue

class Stack:
	def __init__(self):
		self.innerStack = LifoQueue(maxsize=100)

	def push(self, value):
		self.innerStack.put(value);

	def pop(self):
		return self.innerStack.get()

	def peek(self):
		value = self.innerStack.get()
		self.innerStack.put(value)
		return value

	def isEmpty(self):
		return self.innerStack.qsize()==0

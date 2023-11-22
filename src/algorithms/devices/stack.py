class Stack:
	def __init__(self):
		self.innerStack = []

	def push(self, value):
		self.innerStack.append(value)

	def pop(self):
		value = self.innerStack[len(self.innerStack)-1] 
		self.innerStack.remove(value)
		return value

	def peek(self):
		return self.innerStack[len(self.innerStack)-1] 

	def isEmpty(self):
		return len(self.innerStack)==0

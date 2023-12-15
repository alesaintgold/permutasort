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

class POPStack():
	def __init__(self):
		self.innerStack = Stack()

	def push(self, value):
		self.innerStack.push(value)

	def pop(self):
		pop_ = []
		while not self.innerStack.isEmpty():
			pop_.append(self.innerStack.pop())
		return pop_

	def peek(self):
		return self.innerStack.peek()

	def isEmpty(self):
		return self.innerStack.isEmpty()

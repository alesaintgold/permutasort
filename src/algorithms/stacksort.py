from .devices.stack import *

#stacksort
def S(P):
	output = []
	stack = Stack();
	for pi in P:
		while not stack.isEmpty() and stack.peek()<pi:
			output.append(stack.pop())
		stack.push(pi)
	while not stack.isEmpty():
		output.append(stack.pop())
	return output

#POP-stacksort
def PS(P):
	output = []
	stack = POPStack();
	for pi in P:
		if stack.isEmpty() or stack.peek()>pi:
			stack.push(pi)
		else:
			output = output + stack.pop()
			stack.push(pi)
	output = output+ stack.pop()
	return output
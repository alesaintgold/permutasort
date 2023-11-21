from src.algorithms.devices.stack import Stack

#stack-sort
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

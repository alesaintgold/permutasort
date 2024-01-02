from .devices.queue import *

#queue-sort
def Q(P):
	output = []
	queue = Queue()
	for pi in P:
		if queue.isEmpty() or queue.peeklast()<pi:
			queue.enqueue(pi)
		else:
			while not queue.isEmpty() and queue.peek()<pi:
				output.append(queue.dequeue())
			output.append(pi)
	# emtpy the queue in the output
	while not queue.isEmpty():
		output.append(queue.dequeue())
	return output

def PQ(P):
	output = []
	queue = POPQueue()
	for pi in P:
		if queue.isEmpty():
			queue.enqueue(pi)
		elif pi == int(queue.peeklast())+1:
			queue.enqueue(pi)
		elif int(queue.peek()) > int(pi):
			output.append(pi)
		else:
			output = output + queue.dequeue()
			queue.enqueue(pi)
	if not queue.isEmpty():
		output = output + queue.dequeue()
	return output
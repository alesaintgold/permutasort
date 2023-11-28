from src.algorithms.devices.queue import Queue 

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

class POPQueue():
	"""yet to implement"""
	def __init__(self, arg):
		self.arg = arg
		

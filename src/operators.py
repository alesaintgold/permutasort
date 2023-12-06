from src.algorithms.bubblesort import B
from src.algorithms.queuesort import Q
from src.algorithms.stacksort import S

#if implementing new operators, add them to the index
algorithmsIndex = {
 	"B": B,
 	"Q": Q,
 	"S": S
}

def compositionOf(op1,op2):
	return lambda P: op2(op1(P))

def getOperator(key):
	if len(key)==1:
		if key not in algorithmsIndex:
			print("ERROR: unsupported operator " + key)
			exit()
		return algorithmsIndex[key]
	return compositionOf(getOperator(key[:-1]), getOperator(key[-1]))
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
	return lambda P: op1(op2(P))


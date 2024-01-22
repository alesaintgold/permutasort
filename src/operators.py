from .algorithms.bubblesort import B
from .algorithms.queuesort import *
from .algorithms.stacksort import *

#if implementing new operators, add them to the index
algorithmsIndex = {
 	"B": B,
 	"Q": Q,
 	"S": S,
 	"PS": PS,
 	"PQ": Cons
}

def compositionOf(op1,op2):
	return lambda P: op1(op2(P))


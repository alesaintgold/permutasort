from src.algorithms.bubblesort import B
from src.algorithms.queuesort import Q
from src.algorithms.stacksort import S 
from src.algorithms.composition import compositionOf

#if implementing new operators, add them to the index
algorithmsIndex = {
 	"B": B,
 	"Q": Q,
 	"S": S
}

def getOperator(key):
	if len(key)==1:
		if key not in algorithmsIndex:
			print("ERROR: unsupported operator " + key)
			exit()
		else:
			return algorithmsIndex[key]
	else:
		return compositionOf(getOperator(key[0:1]), getOperator(key[1:]))
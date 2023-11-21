from src.algorithms.bubblesort import B
from src.algorithms.queuesort import Q
from src.algorithms.stacksort import S 
from src.algorithms.composition import compositionOf

algorithmsIndex = {
 	"B": B,
 	"Q": Q,
 	"S": S
}

def getOperator(key):
	if len(key) not in (1,2):
		print("ERROR: unknown operator\n\npython traceback:\n")	
		exit()
	elif len(key) == 2:
		return compositionOf(getOperator(key[0]), getOperator(key[1]))
	elif len(key) == 1:
		if key not in algorithmsIndex:
			print("ERROR: unknown operator\n\npython traceback:\n")
		else:
			return algorithmsIndex[key]
	else:
		print ("ERROR: unexpected error\n\npython traceback:\n")
import sys
from src.operators import *
from src.selector import select_permutations
from src.utils import printlist

if(len(sys.argv) != 3):
	print("ERROR: unexpected number of arguments")
	exit()

n = int(sys.argv[1])
op = sys.argv[2]

selector = select_permutations(n, getOperator(op))

sortable = selector.sortable_permutations()
unsortable = selector.unsortable_permutations()
outcomes = selector.outcomes()

print("\nThe following " + str(len(sortable)) +" "+str(n)+"-permutations are sortable with the operator "+op+":\n" + printlist(sortable))
print("The following " + str(len(unsortable)) +" "+str(n)+"-permutations are not sortable with the operator "+op+":\n" + printlist(unsortable))
print("The operator "+op+" can give the following "+ str(len(outcomes))+" results when applied to " + str(n) + "-permutations:\n" + printlist(outcomes))

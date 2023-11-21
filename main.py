import sys
from operators import *
from selector import SortOperatorSelect

if(len(sys.argv) != 3):
	print("ERROR: unexpected number of arguments")
	exit()

n = int(sys.argv[1])
op = sys.argv[2]

selector = SortOperatorSelect(n, getOperator(op))

sortable = selector.sortable_permutations()
unsortable = selector.unsortable_permutations()
oucomes = selector.outcomes()

def printlist(list):
	result = ""
	for item in list:
		result = result +(str(item) + "\t\t")
	result = result +("\n")
	return result

print("\nThe following " + str(len(sortable)) +" "+str(n)+"-permutations are sortable with the operator "+op+":\n" + printlist(sortable))
print("\nThe following " + str(len(unsortable)) +" "+str(n)+"-permutations are not sortable with the operator "+op+":\n" + printlist(unsortable))
print("\nThe operator "+op+" can give the following results when applied to " + str(n) + "-permutations:\n" + printlist(oucomes))


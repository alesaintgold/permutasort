import sys
from itertools import permutations

from src.operators import *
from src.utils import *

class selectorPermutations:
	def __init__(self,num,op):
		if num <=0:
			print("ERROR: was expecting a positive integer but got "  +str(num))
			exit()

		self.__sortable = []
		self.__unsortable = []
		self.__outcomes = []

		perms = list(permutations(range(1,num+1)))
		for P in perms:
			op_P_ = op(P)
			
			#adding outcome to the list
			if op_P_ not in self.__outcomes:
					self.__outcomes.append(op_P_)
			
			#adding permutations to the right list
			if op_P_==sorted(P):
				self.__sortable.append(P)
			else:
				self.__unsortable.append(P)
		
	def getSortable(self):
		return self.__sortable

	def getUnsortable(self):
		return self.__unsortable

	def getOutcomes(self):
		return self.__outcomes

if __name__ == '__main__':
	
	narg = len(sys.argv)
	
	if narg not in (1,3):
		print("ERROR: expected 2 arguments or none, but got these "+str(len(sys.argv)-1)+": " + str(sys.argv[1:]))
		exit()

	elif narg == 3:
		# command line
		n = sys.argv[1]
		op = sys.argv[2]

		ps = selectorPermutations(int(n), getOperator(op))

		sortable = ps.getSortable()
		unsortable = ps.getUnsortable()
		outcomes = ps.getOutcomes()

		sortable_str = "The following " + str(len(sortable)) +" "+str(n)+"-permutations are sortable with the operator "+op+":\n" + printlist(sortable)
		unsortable_str = "The following " + str(len(unsortable)) +" "+str(n)+"-permutations are not sortable with the operator "+op+":\n" + printlist(unsortable)
		outcomes_str = "The operator "+op+" can give the following "+ str(len(outcomes))+" results when applied to " + str(n) + "-permutations:\n" + printlist(outcomes)

		print('\n'+sortable_str)
		print(unsortable_str)
		print(outcomes_str)

		writeInFiles("./log/"+n+op+"sortable.txt", sortable_str)
		writeInFiles("./log/"+n+op+"unsortable.txt", unsortable_str)
		writeInFiles("./log/"+n+op+"outcomes.txt", outcomes_str)

	else:
		from src.gui import PermutaSortGUI
		PermutaSortGUI()


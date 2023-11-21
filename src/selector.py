import itertools

class select_permutations:
	def __init__(self,num,op):
		self.sortable = []
		self.unsortable = []
		self.possible_outcomes = []

		if num <=0:
			print("ERROR: was expecting a positive integer but got "  +str(num))
			exit()

		perms = list(itertools.permutations(range(1,num+1)))

		for P in perms:
			sorted_P = op(P)

			#adding outcome to the list
			if sorted_P not in self.possible_outcomes:
					self.possible_outcomes.append(sorted_P)

			#adding permutations to the right list
			if sorted_P == sorted(P):
				self.sortable.append(P)
			else:
				self.unsortable.append(P)

	def sortable_permutations(self):
		return self.sortable

	def unsortable_permutations(self):
		return self.unsortable

	def outcomes(self):
		return self.possible_outcomes

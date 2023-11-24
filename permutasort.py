import sys
import tkinter as tk

from src.operators import *
from src.selector import select_permutations
from src.utils import printlist

class PermutaSortGUI:
	def __init__(self):
		self.window = tk.Tk(	)
		self.window.geometry("300x200")

		label1 = tk.Label(text="Selecting which n-permutations\nare sortable or unsortable for the\nspecified sorting operator")
		label1.pack()

		n_frame = tk.Frame()
		n_label = tk.Label(master = n_frame, text = "\n\nn = ") 
		n_label.pack()
		self.n_box = tk.Entry(master = n_frame, width = 10)
		self.n_box.pack()
		n_frame.pack()

		o_frame = tk.Frame()
		o_label = tk.Label(master = o_frame, text = "operator: ")
		o_label.pack()
		self.o_box = tk.Entry(master=o_frame, width = 10)
		self.o_box.pack()
		o_frame.pack()

		button = tk.Button(text = "Calculate", width = 25, command = self.calculate)
		button.pack()

		self.window.mainloop()

	def calculate(self):
		n = self.n_box.get()
		op = self.o_box.get()

		ps = select_permutations(int(n), getOperator(op))

		sortable = ps.sortable_permutations()
		unsortable = ps.unsortable_permutations()
		outcomes = ps.outcomes()

		self.display(sortable, "The " +n+"-permutations sortable by "+op+" are the following "+str(len(sortable))+":")
		self.display(unsortable, "The " +n+"-permutations not sortable by "+op+" are the following "+str(len(unsortable))+":")
		self.display(sortable, "Applying "+op+" to " + n + "-permutations can generate the following outcomes:")

		#self.window.destroy()

	def display(self, list, message):
		new_window = tk.Toplevel(self.window)

		label = tk.Label(text=message + "\n")
		label.pack()
		str_list = tk.Label(text=printlist(list))
		str_list.pack()

		new_window.grab_set()

if __name__ == '__main__':
	narg = len(sys.argv)
	if narg not in (1,3):
		print("ERROR: unexpected number of arguments: " + str(sys.argv[1:]))
		exit()

	elif len(sys.argv) == 3:
		
		# command line
		
		n = sys.argv[1]
		op = sys.argv[2]

		ps = select_permutations(int(n), getOperator(op))

		sortable = ps.sortable_permutations()
		unsortable = ps.unsortable_permutations()
		outcomes = ps.outcomes()

		sortable_str = "The following " + str(len(sortable)) +" "+str(n)+"-permutations are sortable with the operator "+op+":\n" + printlist(sortable)
		unsortable_str = "The following " + str(len(unsortable)) +" "+str(n)+"-permutations are not sortable with the operator "+op+":\n" + printlist(unsortable)
		outcomes_str = "The operator "+op+" can give the following "+ str(len(outcomes))+" results when applied to " + str(n) + "-permutations:\n" + printlist(outcomes)

		print('\n'+sortable_str)
		print(unsortable_str)
		print(	outcomes_str)

		file_sortable = open("./log/"+n+op+"sortable.txt", "w")
		file_sortable.write(sortable_str)
		file_sortable.close()

		file_unsortable = open( "./log/"+n+op+"unsortable.txt","w")
		file_unsortable.write(unsortable_str)
		file_unsortable.close()

		file_outcome = open("./log/"+n+op+"outcome.txt","w")
		file_outcome.write(outcomes_str)
		file_outcome.close()

	else:
		PermutaSortGUI()


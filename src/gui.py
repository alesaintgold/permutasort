import tkinter as tk

from permutasort import selectorPermutations
from src.utils import *

class PermutaSortGUI:
	def __init__(self):
		self.__window = tk.Tk(	)
		self.__window.geometry("300x200")

		label1 = tk.Label(text="Selecting which n-permutations\nare sortable or unsortable for the\nspecified sorting operator")
		label1.pack()

		n_frame = tk.Frame()
		n_label = tk.Label(master = n_frame, text = "\nn = ") 
		n_label.pack()
		self.__n_box = tk.Entry(master = n_frame, width = 10)
		self.__n_box.pack()
		n_frame.pack()

		o_frame = tk.Frame()
		o_label = tk.Label(master = o_frame, text = "operator: ")
		o_label.pack()
		self.__o_box = tk.Entry(master=o_frame, width = 10)
		self.__o_box.pack()
		o_frame.pack()

		button = tk.Button(text = "Calculate", width = 25, command = self.calculate)
		button.pack()

		self.__window.mainloop()

	def calculate(self):
		n = self.__n_box.get()
		op = self.__o_box.get()

		ps = selectorPermutations(int(n), getOperator(op))

		sortable = ps.getSortable()
		unsortable = ps.getUnsortable()
		outcomes = ps.getOutcomes()

		sortable_str = "The " +n+"-permutations sortable by "+op+" are the following "+str(len(sortable))+":\n"+printlist(sortable)
		unsortable_str = "The " +n+"-permutations unsortable by "+op+" are the following "+str(len(unsortable))+":\n"+printlist(unsortable)
		outcomes_str = "Applying "+op+" to " + n + "-permutations can generate the following outcomes:\n"+printlist(outcomes)

		self.displayList(sortable_str)
		self.displayList(unsortable_str)
		self.displayList(outcomes_str)
		
		writeInFile("./log/"+n+op+"sortable.txt", sortable_str)
		writeInFile("./log/"+n+op+"unsortable.txt", unsortable_str)
		writeInFile("./log/"+n+op+"outcomes.txt", outcomes_str)

	def displayList(self, message):
		new_window = tk.Toplevel(self.__window)
		label = tk.Label(new_window, text=message)
		label.pack()
		new_window.grab_set()

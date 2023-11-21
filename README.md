# PermutaSort
This is a software that I built for my bechelor degree thesis in computer science.
Its purpose is to help analyzing the behavior of sorting operators 
  (e.g. bubblesort, stacksort, queuesort) with permutations of whole numbers.

This program take as arguments a whole number n and a sorting operators O and print 
the list and amount of:
  * n-permutations sortable by O
  * n-permutations not sortable by O
  * possible outcomes when applying O to every n-permutations

Note: this does not use sorting algorithms, but sorting operators, so for example,
  for the bubblesort algorithm we observe the operator B() representing only one
  iteration of the bubble sort algorithm such that:
  bubblesort(x) = B(...B(B(x))...)

HOW TO USE (from command line):
  #python main.py n O

At the moment the only operators supported are:
  * B: bubble-sort
  * Q: queue-sort
  * S: stack-sort
  * any combination of two of those (e.g QS(x) = Q(S(x)))

NEXT TO IMPLEMENT:
  * pop-container operators
  * print results on files 
  * combinations of more than two operators (...?)
  

# sortingOperatorsAnalysis
This is a software that I built for my bechelor degree thesis in computer science.
Its purpose is to help analyzing the behavior of a class of sorting operators 
  (e.g. bubblesort, stacksort, queuesort) with class patterns of whole numbers.

Note: this does not use sorting algorithms, but sorting operators, so for example,
  for the bubblesort algorithm we observe the operator B() representing only one
  iteration of the bubble sort algorithm such that:
  bubblesort(x) = B(...B(B(x))...)

HOW TO USE (from command line):
  #python main.py 3 Q

  3 can be any positive integer
  Q represent the sorting operator:
    at the moment are only supported:
      *B: bubble-sort
      *Q: queue-sort
      *S: stack-sort
      *any combination of two of those (e.g QS(x) = Q(S(x)))

NEXT TO IMPLEMENT:
  * pop-container operators
  * print results on files 
  * combinations of more than two operators (...?)
  

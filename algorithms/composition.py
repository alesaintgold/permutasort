def compositionOf(op1,op2):
	return lambda P: op1(op2(P))

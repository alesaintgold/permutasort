
def printlist(list):
	result = ""
	for item in list:
		result = result +(str(item) + "\n")
	return result

def getOperator(key):
	from src.operators import algorithmsIndex, compositionOf
	if len(key)==1:
		if key not in algorithmsIndex:
			print("ERROR: unsupported operator " + key)
			exit()
		return algorithmsIndex[key]
	return compositionOf(getOperator(key[:-1]),getOperator(key[-1]))

def writeInFile(name, content):
	file = open(name, 'w')
	file.write(str(content) + '\n')
	file.close()

def isPermutationSorted(P):
	n = 0
	for p in P:
		n = n + 1
		if int(p)!=n:
			return False
	return True

def printlist(list):
	result = ""
	for item in list:
		result = result +(str(item) + "\n")
	return result

def getOperator(key):
	from .operators import algorithmsIndex, compositionOf
	if len(key)==1 or (len(key)==2 and (key[0]=='P')):
		if key not in algorithmsIndex:
			print("ERROR: unsupported operator " + key)
			exit()
		return algorithmsIndex[key]
	else:
		if key[0]=='P':
			first_operator = key[:2]
			second_operator = key[2:]
		else:
			first_operator = key[:1]
			second_operator = key[1:]
		return compositionOf(getOperator(first_operator),getOperator(second_operator))

def writeInFile(name, content):
	file = open(name, 'w')
	file.write(str(content) + '\n')
	file.close()

def isIdentityPermutation(P):
	n = 0
	for p in P:
		n = n + 1
		if int(p)!=n:
			return False
	return True


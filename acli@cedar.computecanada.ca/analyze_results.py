n = 20
instance = "child"
inFile = open("results_final.txt")

mapFile = open("/home/andrewli/Documents/MINOBS-anc/data/mappings/" + instance + ".mapping")
mapping = dict()
rmapping = dict()

for i in range(n):
	var = mapFile.readline().strip()
	rmapping[i] = var
	mapping[var] = i



tmTotals = [0 for i in range(600)]
counts = [0 for i in range(600)]
models = [[] for i in range(600)]
feasible = [0 for i in range(600)]
totalSat = [0 for i in range(600)]


def model2network(model):
	network = [[0]*n for j in range(n)]

	for i in range(n):
		varStr = model[1:model.find("]")]
		model = model[model.find("]") + 1:]


		
		if (varStr.find("|") == -1):
			#print("Parents of var ", mapping[varStr], ": ", end="")
			#print("")
			continue

		else:
			var, rest = varStr.split("|")
			pars = rest.split(":")

			intPars = []

			#print("Parents of var ", mapping[var], ": ", end="")
			for par in pars:
				intPars.append(mapping[par])

				network[mapping[par]][mapping[var]] = 1
			intPars.sort()
			#print(" ".join(map(str, intPars)))

	return network


def hasDipath(a, b, network):
	if a == b:
		return True

	for i in range(n):
		if network[i][b] and hasDipath(a, i, network):
			return True

	return False


def numConstraintsSatisfied(consFile, model):
	model = model.strip()[1:-2]
	network = model2network(model)

	constraintsFile = open("/home/andrewli/Documents/MINOBS-anc/data/constraints/" + instance + "/" + consFile.strip())
	constraints = []
	for i in range(int(constraintsFile.readline())):
		a, b = map(int, constraintsFile.readline().split(" "))
		constraints.append( (a,b) )

	sat = 0
	for each in constraints:
		if hasDipath(each[0], each[1], network):
			sat += 1
	return sat
		


while True:
	line1 = inFile.readline()

	if (not line1 or line1.strip()==""):
		break

	line2 = inFile.readline()
	line3 = inFile.readline()
	line4 = inFile.readline()

	caseNum = int(line2.strip()[-1])
	ncs = numConstraintsSatisfied(line3, line4)


	tm = float(line1)

	line3 = line3[line3.index(".")+1:]
	line3 = line3[:line3.index("-")]

	cons = int(line3)

	counts[cons] += 1
	tmTotals[cons] += tm
	models[cons].append((line4, caseNum))

	if (ncs == cons):
		feasible[cons] += 1
	totalSat[cons] += ncs



for i in range(600):
	if counts[i] != 0:
		print("# Constraints:", i)
		print("# Models:", counts[i])
		print("Avg time:", tmTotals[i]/counts[i])
		print("% Feasible:", 100*feasible[i]/counts[i])
		print("% Constraints:",  100 if (i == 0) else 100*(totalSat[i] / (i * counts[i])))

		for each in models[i]:
			print("c(%s %d)," %(each[0].strip(), each[1]))


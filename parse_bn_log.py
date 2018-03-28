import argparse

parser = argparse.ArgumentParser(description="",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input_file")
parser.add_argument("output_file")
args = parser.parse_args()

inFile = open(args.input_file)
outFile = open(args.output_file, "a")

outFile.write("\"")

while True:
	line = inFile.readline().strip()
	if not line or line == "":
		break

	var = line[5:-2]

	pars = inFile.readline()[13:-3].strip().split(", ")

	outFile.write("[" + var)

#[asia][tub][smoke][lung|smoke][bronc|dysp][either|tub:lung][xray|either][dysp|either]
	if (len(pars) == 0 or (len(pars) == 1 and pars[0].strip() == "")):
		outFile.write("]")

	else:
		outFile.write("|"+pars[0])

		for each in pars[1:]:
			outFile.write(":" + each)
		outFile.write("]")



outFile.write("\",\n")
outFile.close()
import numpy

def load_data():
	f = open("data/Achilles_v2.9_training.gct")
	essentiality = readfile(f)
	f = open("data/CCLE_expression_training.gct")
	expression = readfile(f)
	f = open("data/CCLE_copynumber_training.gct")
	copynumber = readfile(f)

	return [essentiality, expression, copynumber]

			
def readfile(f):
	f.readline()
	dimensions = f.readline()
	dimensions = dimensions.split("\t")
	genes = int(dimensions[0])
	samples = int(dimensions[1])
	f.readline()
	mat = numpy.zeros(shape=(genes, samples))
	for i in range(0, genes):
		line = f.readline().split("\t")
		for j in range(0, samples):
			mat[i, j] = float(line[j+2])
	return mat



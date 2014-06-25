import numpy

def load_data():
	f = open("data/Achilles_v2.9_training.gct")
	essentiality = readfile(f)
	f = open("data/CCLE_expression_training.gct")
	expression = readfile(f)
	f = open("data/CCLE_copynumber_training.gct")
	copynumber = readfile(f)
	data = DreamData(essentiality[1], expression[0], copynumber[0], essentiality[0])
	data.normalize_data()
	return data

			
def readfile(f):
	f.readline()
	dimensions = f.readline()
	dimensions = dimensions.split("\t")
	genes = int(dimensions[0])
	samples = int(dimensions[1])
	f.readline()
	mat = numpy.zeros(shape=(genes, samples))
	labels = {}
	for i in range(0, genes):
		line = f.readline().split("\t")
		labels[line[0]] = i
		for j in range(0, samples):
			mat[i, j] = float(line[j+2])
	return [mat, labels]

class DreamData:
	def __init__(self, labels, expression, copynumber, essentiality):
		self.labels = labels
		self.expression = expression
		self.copynumber = copynumber
		self.essentiality = essentiality
		self.genes_to_rank = self.essentiality.shape[0]
		self.samples = self.essentiality.shape[1]
		self.copynumber_genes = self.copynumber.shape[0]
		self.expression_genes = self.expression.shape[0]
		#self.ranking = self.rank_genes()
	def normalize_data(self):
		oldshape = self.copynumber.shape
		copynumber_max = numpy.amax(self.copynumber, 0)
		expression_max = numpy.amax(self.expression, 0)
		assert(len(copynumber_max) == 45)
		samples = self.expression.shape[1]
		for i in range(0, samples):
			self.copynumber[:,i] = self.copynumber[:,i]*(1/copynumber_max[i])
			self.expression[:,i] = self.expression[:,i]*(1/expression_max[i])
		assert(self.copynumber.shape == oldshape)
		print("max copynumber = " + str(numpy.amax(self.copynumber, 0)[0]))
	
		
		
		

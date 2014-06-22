import operator

def writefile(data): 
	essentiality = data[0]
	copynumber = data[1]
	expression = data[2]

	max_copy_number = 100
	max_expression = 100
	out = open("svm-dream9-train.dat", "w")
	genes = len(essentiality)
	samples = len(essentiality[0])

	for i in range(0, genes):
		print("Gene " + str(i) + " written \n")
		for j in range(0, samples):
			line = ""
			line += str(essentiality[i][j])
			line += " qid:" + str(i)
			for k in range(0, max_copy_number):
				line = line + " " + str(k) + ":" + str(copynumber[k][j])
			for k in range(0, max_expression):
				line = line + " " + str(k + max_copy_number) + ":" + str(expression[k][j])
			#print(line)
			line = line + "\n"
			out.write(line)



def rank_training_cell_lines(data):
	essentiality = data[0]
	copynumber = data[1]
	expression = data[2]

	expression_sorted = []
	copynumber_sorted = []
	n_genes = len(essentiality)
	for i in range(0, n_genes):
		expression_sorted.append([])
		copynumber_sorted.append([])
		gene = essentiality[i]
		n_samples = len(gene)
		#create sorted index map for this gene
		m = dict(zip(range(0, n_samples), gene))
		#for index, cell_line in m.items():
		#	print(index)
		#	print(cell_line)
		m = sorted(m.iteritems(), key = operator.itemgetter(1))
		print(m)
		for index, essentiality in m:
			expression_sorted[i].append(expression[i][index])
			copynumber_sorted[i].append(copynumber[i][index])
		print(copynumber_sorted)
	return [copynumber_sorted, expression_sorted]
				
def rank_training_genes(data):
	essentiality = data[0]
	copynumber = data[1]
	expression = data[2]
	n_genes = len(essentiality)
	n_cell_lines = len(essentiality[0])
		
	
	#for i in range(0, n_cell_lines):
		
	#	for gene in essentiality:
			
		

def main():
	f = open("data/Achilles_v2.9_training.gct")
	essentiality = readfile(f)
	f = open("data/CCLE_expression_training.gct")
	expression = readfile(f)
	f = open("data/CCLE_copynumber_training.gct")
	copynumber = readfile(f)
	data = [essentiality, copynumber, expression]
	writefile(data)
	#rank_training_cell_lines(data)

			
if __name__ == "__main__":
    main()
	
	

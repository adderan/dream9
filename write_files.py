import dimension_reduction
import load_data

def write_svm_data(num_features, num_blocks):
	svm_train_file = open("svm_train_file.dat", "w")
	svm_test_file = open("svm_test_file.dat", "w")
	data = load_data.load_data()
	data.genes_to_rank = 3
	train_samples = 40
	features = dimension_reduction.choose_features(data, num_blocks, num_features)
	for s in range(0, data.samples):
		for g in range(0, data.genes_to_rank):
			line = ""
			line += str(int(data.ranking[g, s]))
			line += " qid:"
			line += str(int(s))
			for f in range(0, num_features):
				line += " "
				feature_index = features[g, f]
				line += str(int(feature_index))
				line += ":"
				if feature_index >= data.expression_genes:
					copynumber_index = feature_index - data.expression_genes
					line += str(data.copynumber[copynumber_index, s])
				elif feature_index < data.expression_genes:
					line += str(data.expression[feature_index, s])
			line += "\n"
			if s <= train_samples:
				svm_train_file.write(line)
			else:
				svm_test_file.write(line)
			
	svm_train_file.close()
	svm_test_file.close()					
	
	
def main():
	write_svm_data(10, 100)
	
if __name__ == "__main__":
	main()	
	
		

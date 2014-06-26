import numpy as np
import load_data

#X is matrix, y is list

expected_samples = 45

def ridge_regression(X, y):
	X = X.T #ridge regression used (samples, features)
	a = X.shape[0]
	b = X.shape[1]
	#print("X shape: " + str(X.shape))
	db = np.zeros((b,b), float)
	np.fill_diagonal(db, 1)
	x0 = X.T.dot(X) + db
	#print("X0 shape = " + str(x0.shape))
	x1 = np.linalg.inv(x0)
	#print("x1 shape = " + str(x1.shape))
	#print("y shape = " + str(y.shape))
	x2 = X.T.dot(y)
	beta = x1.dot(x2)
	#print("beta shape = " + str(beta.shape))
	return beta
def choose_features(data, blocks, num_features): 
	essentiality = data.essentiality
	expression = data.expression
	copynumber = data.copynumber
	
	genes_to_rank = data.genes_to_rank
	samples = data.samples
	
	copynumber_genes = data.copynumber_genes
	expression_genes = data.expression_genes
	#assert(expression.shape[1] == 45)
	
	Xall = np.concatenate([expression, copynumber])
	Xall = Xall[0:42000:1]
	blocksize = (Xall.shape[0])/blocks
	print("blocksize = " + str(blocksize))
	
	
	features = np.zeros(shape=(genes_to_rank, num_features))
	
	for i in range(0, genes_to_rank):
		y = essentiality[i,:]
		features_for_gene = choose_features_for_gene(Xall, y, blocks, blocksize, num_features)
		features[i,:] = features_for_gene
	return features
	
def choose_features_for_gene(Xall, y, blocks, blocksize, num_features):
	weight_vectors = []
	for b in range(0, blocks):
		start = b*blocksize
		stop = (b+1)*blocksize
		X = Xall[start:stop:1]
		weight_vectors.append(ridge_regression(X, y))
	#print(weight_vectors[0])
	total_input_features = Xall.shape[0]
	combined_weight_vector = np.zeros(shape=0)
	combined_weight_vector_no_abs = np.zeros(shape=0)
	for w in weight_vectors:
		assert(len(w) > 1)
		combined_weight_vector = np.hstack((combined_weight_vector, abs(w)))
		combined_weight_vector_no_abs = np.hstack((combined_weight_vector_no_abs, w))
	top_features = []
	#print("shape of combined_weight_vector: " + str(combined_weight_vector.shape))
	for f in range(0, num_features):
		feature_index = np.argmax(combined_weight_vector, 0)
		top_features.append(feature_index)
		print("value of selected feature: " + str(combined_weight_vector_no_abs[feature_index]))
		combined_weight_vector[feature_index] = 0	
	return top_features	
		 	
def main():
	data = load_data.load_data()
	features = choose_features(data, 100, 10)
	print(features)
	

if __name__ == "__main__":
	main()


	

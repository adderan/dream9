import dimension_reduction
import load_data

def write_data(num_features, num_blocks):
	data = load_data.load_data()
	features = dimension_reduction.choose_features(data, num_blocks, num_features)
	
	print(data.ranking)
	
def rank_genes(essentiality_for_sample):

	essentiality_tuples = []
	for i in range(0, self.genes_to_rank):
		essentiality_tuples.append((i, self.essentiality[i]))
	ranking = sorted(essentiality_tuples, key=lambda tup : tup[1])
	return ranking	
	
	
def main():
	write_data(10, 100)
	
if __name__ == "__main__":
	main()	
	
		

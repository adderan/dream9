import dimension_reduction
import load_data
import numpy
import random

def ranking_test():
	a = numpy.zeros(shape=(10,10)) #shape doesn't matter for this test
	b = numpy.zeros(shape=(10,10))

	essentiality = numpy.zeros(shape=(10,2))
	for i in range(0, 10):
		for j in range(0, 2):
			essentiality[i,j] = random.uniform(-1, 1)
			
	data = load_data.DreamData({}, a, b, essentiality)
	print(data.essentiality)
	print(data.ranking)
	
def main():
	ranking_test()

if __name__ == "__main__":
	main()	

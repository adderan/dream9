import numpy as np
import load_data

#X is matrix, y is list
def ridge_regression(X):
	a = X.shape[0]
	b = X.shape[1]
	print(a)
	print(b)

def main():
	data = load_data.load_data()
	essentiality = data[0]
	ridge_regression(essentiality)

if __name__ == "__main__":
	main()


	

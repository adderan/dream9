def main(): 
	f = open("data/Achilles_v2.9_training.gct")
	essentiality = readfile(f)
	print(essentiality)


def readfile(f):
	f.readline()
	dimensions = f.readline()
	dimensions = dimensions.split("\t")
	genes = 10 #int(dimensions[0])
	samples = 10 #int(dimensions[1])
	f.readline()
	mat = []
	for i in range(0, genes):
		mat.append([])
		line = f.readline().split("\t")
		for j in range(0, samples):
			mat[i].append(float(line[j+2]))
	return mat


			
if __name__ == "__main__":
    main()
	
	

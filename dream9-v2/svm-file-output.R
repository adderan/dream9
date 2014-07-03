write.svm.file <- function(cluster.assignments, essentiality, data, n.clusters) {
	features <- dim(data)[[1]] #number of features
	samples <- dim(data)[[2]]
	genes <- dim(essentiality)[[1]]

	for(g in 1:genes) {
		for(s in 1:samples) {
			means <- cluster.means(cluster.assignments, n.clusters, data, s)
			line <- ""
			line <- paste(essentiality[g, s], line, sep="")
			line <- paste(line, " qid:", sep="")
			line <- paste(line, g, sep="")
			for(i in 1:n.clusters) {
				line <- paste(line, " ", sep="")
				line <- paste(line, i, sep="")
				line <- paste(line, ":", sep="")
				line <- paste(line, means[i], sep="")
			}
		}
		cat(line, "\n")
	}
}

main <- function() {
	load("../dream9-training.RData")
	source("feature-cluster.R")
	n.clusters <- 100

	data <- normalize.data(expression, copy.number)
	cluster.assignments <- cluster.features(data, n.clusters)
	write.svm.file(cluster.assignments, essentiality, data, n.clusters)
}




	

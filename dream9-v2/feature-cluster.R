cluster.features <- function(data, n) {
	cat("dimension of data: ", dim(data), "\n")
	clusters <- kmeans(data, n)
	cluster.assignments <- clusters$cluster
	#print(cluster.assignments)
	cat("dimension of cluster: ", length(cluster.assignments), "\n")
	cat("sums of squares: ", clusters$withinss, "\n")
	cluster.means(cluster.assignments, n, data, 1)
	return(cluster.assignments)
	 
}
cluster.means <- function(cluster.assignments, n.clusters, data, sample) {
	means <- c(rep(0, n.clusters))
	for(i in 1:length(cluster.assignments)) {
		ca <- cluster.assignments[i]
		means[ca] <- means[ca] + data[i, sample]
	}
	means <- means / length(cluster.assignments)
	#cat("length of means: ", length(means), "\n")
	return(means)
}


normalize.data <- function(expression, copynumber) {
	expression_features <- dim(expression)[[1]]
	copynumber_features <- dim(copynumber)[[1]]

	samples <- dim(expression)[[2]]

	for(s in 1:samples) {
		expression_max <- 0
		copynumber_max <- 0
		for(i in 1:expression_features) {
			exp <- expression[i, s]
			if(exp > expression_max) {
				expression_max <- exp
			}
		}
		for(i in 1:copynumber_features) {
			copy <- copynumber[i, s]
			if(copy > copynumber_max) {
				copynumber_max <- copy
			}
		}
		expression[,s] <- expression[,s]/expression_max
		copynumber[,s] <- copynumber[,s]/copynumber_max
			
	}
	return(rbind(expression, copynumber))
}

main <- function() {
	load("../dream9-training.RData")
	cluster.features(essentiality, copy.number, expression)
	
}

	
	

			
	



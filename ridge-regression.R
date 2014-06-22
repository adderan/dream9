ridge.regression <- function() {
	library(MASS)
	load("data/dream9-training.RData")
	copy.number.norm <- norm(copy.number)
	expression.norm <- norm(expression)

	genes <- dim(essentiality)[[1]]
	copy.number.genes <- dim(copy.number)[[1]]
	expression.genes <- dim(expression)[[1]]
	samples <- dim(expression)[[2]]

	for(i in 1:copy.number.genes) {
		for(j in 1:samples) {
			copy.number[i, j] <- copy.number[i, j]/copy.number.norm[j]
		}
	}
	for(i in 1:expression.genes) {
		for(j in 1:samples) {
			expression[i, j] <- expression[i, j]/expression.norm[j]
		}
	}
	X <- t(rbind(copy.number, expression))
	cat("dimension of X: ", dim(X), "\n")

	for(i in 1:5) { #each gene is a separate problem
		a <- dim(X)[[1]]
		b <- dim(X)[[2]]
		Y <- essentiality[i,]
		lambda <- 1 

		x1 <- ginv(t(X) %*% X + lambda * diag(b))
		x2 <- t(X) %*% Y
		#print(x2)
		beta <- x1 %*% x2
		cat("length of beta: ", length(beta), "\n")
	}

}

norm <- function(m) {
	genes <- dim(m)[[1]]
	samples <- dim(m)[[2]]

	max <- c()
	for(j in 1:samples) {
		sample_max <- 0
		for(i in 1:genes) {
			if(m[i,j] > sample_max) {
				sample_max <- m[i,j]
			}
		}
		max[j] <- sample_max
	}
	return(max)
}


read.matrix <- function(filename, nameindex) {
	f <- file(filename, "rt")
	readLines(f, 1)

	dimensions <- strsplit(readLines(f, 1), '\t')[[1]]
	genes <- strtoi(dimensions[[1]])
	cell.lines <- strtoi(dimensions[[2]])

	Y <- matrix(rep(0, times = genes*cell.lines), genes, cell.lines)

	linenames <- strsplit(readLines(f, 1), '\t')[[1]]
	#print(linenames)
	cat("\n")
	linenames <- linenames[-1]
	linenames <- linenames[-1]
	#print(linenames)
	colnames(Y) <- linenames
	print(colnames(Y))

	rnames <- c()
	for(i in 1:genes) {
		line <- strsplit(readLines(f,1), '\t')[[1]]
		rnames[i] <- line[[nameindex]]
		for(j in 1:cell.lines) {
			Y[i, j] <- as.numeric(line[[j+2]])
		}
	}
	rownames(Y) <- rnames
	Y
}
write.data <- function() {
	essentiality <- read.matrix("data/Achilles_v2.9_training.gct",1)
	copy.number <- read.matrix("data/CCLE_copynumber_training.gct",1)
	expression <- read.matrix("data/CCLE_expression_training.gct",2)
	save(essentiality, copy.number, expression, file = "dream9-training.RData")

	copy.number <- read.matrix("data/CCLE_copynumber_leaderboard.gct",1)
	expression <- read.matrix("data/CCLE_expression_leaderboard.gct",2)
	save(copy.number, expression, file = "dream9-leaderboard.RData")

}



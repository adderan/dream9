make.file <- function(infile, outfile) {
	load(infile)
	f <- file("ranklibfile")

	genes <- dim(essentiality)[[1]]
	samples <- dim(essentiality)[[2]]
	expression.genes <- 10 #dim(expression)[[1]]
	copy.number.genes <- 10 #dim(copy.number)[[1]]
	#cat("test \n", file = f)
	for(i in 1:10) {
		#gene.name <- rownames(essentiality)[[i]]
		for(j in 1:samples) {
			#cat("gene is ", gene.name, "j = ", j, "\n")
			line <- ""
			paste(line, as.character(essentiality[i,j]), sep="")
			paste(line, "test", sep="")
			cat(line, "\n")
			#feature1 <- expression[gene.name, j]
			#feature2 <- copy.number[gene.name, j]
			for(k in 1:copy.number.genes) {
				paste(line, " ", sep="")
				paste(line, as.character(k), sep="")
				#cat(line, "\n")
				paste(line, ":", sep="")
				paste(line, as.character(copy.number[k, j]), sep="")
			}
			for(k in 1:expression.genes) {
				paste(line, " ", sep="")
				paste(line, as.character(k+copy.number.genes), sep="")
				paste(line, ":", sep="")
				paste(line, as.character(expression[k, j]), sep="")
			}
			cat(line, "\n")
			writeLines(line, f)

		}
	}
	close(f)
}




	



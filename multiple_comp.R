setwd("~/Downloads")
dataset<-read.csv("glm_bl.csv", header=TRUE)
p <- dataset$i.p.value
p.adjust(p, method = 'fdr', n=length(p))
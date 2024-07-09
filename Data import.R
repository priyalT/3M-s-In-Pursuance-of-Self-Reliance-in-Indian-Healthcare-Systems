if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.19")
BiocManager::install("biomaRt")
BiocManager::available()
BiocManager::install("GEOquery")
install.packages("tidyverse")
library(Biobase)
library(GEOquery)
library(tidyverse)

gse179252 <- getGEO(filename = "/Users/priyaltripathi/SIP(2023-24)/GSE179252_family.soft")
Meta(gse179252) #The metadata

gene_counts <- read.table("/Users/priyaltripathi/SIP(2023-24)/GSE179252_Raw_gene_counts_matrix.txt", header = TRUE, sep = "", row.names = 1)
x <- t(gene_counts) #Transposed genetic data
options(max.print=1000000)

gene_counts_1 <- read.table("/Users/priyaltripathi/SIP(2023-24)/GSE184336_Raw_gene_counts_matrix.txt", header = TRUE, sep = "", row.names = 1)
y <- t(gene_counts_1)


z <- rbind(x,y) #dataset with both the gene counts

#entire mapping the GENE IDs process 
library(biomaRt)
mart <- useMart(biomart = "ensembl", dataset = "hsapiens_gene_ensembl")

genes <- colnames(z)
mapping <- getBM(attributes = c("ensembl_gene_id", "hgnc_symbol"), 
                 filters = "ensembl_gene_id", 
                 values = genes, 
                 mart = mart)
colnames(z) <- mapping$hgnc_symbol[match(colnames(z), mapping$ensembl_gene_id)]

#Setting up the dataframe
df_r <- read.csv("/Users/priyaltripathi/SIP(2023-24)/Sample_Characteristics.csv") #The dataframe with the sample chars
colnames(dataframe)[ncol(dataframe)] <- colnames(df_r)[2] #Keep sample chars name same in the column
dataframe <- cbind(z, df_r[,"Sample_Characteristics"]) #Dataset that includes the sample characteristics with dataframe
write.csv(dataframe, "/Users/priyaltripathi/SIP(2023-24)/Dataframe.csv", row.names = FALSE) #Save the dataframe



#GC <- c("GACAT1", "FAM72D", "PPHLN1", "EMCN", "TACC1", "GACAT2", "SLC25A25-AS1", "SERF2", "EGFLAM-AS1", "RRP7A")
#df <- z[,colnames(z) %in% GC]
#df <- cbind(df, df_r[, 2])






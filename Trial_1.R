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

#Reading the gene counts into a table/dataframe
gene_counts <- read.table("/Users/priyaltripathi/SIP(2023-24)/GSE184336_Raw_gene_counts_matrix.txt", header = TRUE, sep = "", row.names = 1)
y <- t(gene_counts)

#using biomart to map gene expressions to gene symbols
library(biomaRt)
mart <- useMart(biomart = "ensembl", dataset = "hsapiens_gene_ensembl")
genes <- colnames(y)
mapping <- getBM(attributes = c("ensembl_gene_id", "hgnc_symbol"), 
                 filters = "ensembl_gene_id", 
                 values = genes, 
                 mart = mart)
#Turning the column names of dataframe to the gene symbols instead of their IDs
colnames(y) <- mapping$hgnc_symbol[match(colnames(y), mapping$ensembl_gene_id)]
y

#Adding the sample characteristics to a data frame
df <- read.csv("/Users/priyaltripathi/SIP(2023-24)/trial_sample_characters.csv") 
View(df)

dataframe <- cbind(y, df[match(rownames(y), df$Sample_ID), "Sample_Characteristics", drop = FALSE])

write.csv(dataframe, "/Users/priyaltripathi/SIP(2023-24)/trial_dataframe.csv", row.names = FALSE) #Save the dataframe

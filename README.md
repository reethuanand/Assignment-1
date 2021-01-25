
# Aim:
To analyze the differentially expressed genes from RNA-Seq data.
and Use of Machine Learning Algorithms like PCA (Principal Component Analysis) and use of GSVA (Gene Set Variation Analysis) algorithm in Docker to get specific insights

# Background:

A large number of computational methods have been recently developed for analyzing the differential 	gene expression (DE) in RNA-Seq data. 
This exercise uses  CmapR tool for data analysis.Pancreatic Adenocarcinoma (PAAD) is the third most common cause of death from cancer, with an overall 5-year survival rate of less than 5% .RNA-Seq (RNA sequencing), is a sequencing technique to detect the quantity of RNA in a biological sample at a given moment. Here we have a dataset of normalized RNA Sequencing reads for pancreatic cancer tumors​ . The measurement consists of ~20,000 genes for 185 pancreatic cancer tumors. The file format is ​ GCT , a tab-delimited file used for sharing gene expression data and metadata for samples.


## Data set: The measurement consists of ~20,000 genes for 185 pancreatic cancer tumors

## Exploratory Data Analysis:

Principal component analysis (PCA) is a statistical procedure that can be used for exploratory data analysis. PCA uses linear combinations of the original data (e.g. gene expression values) to define a new set of unrelated variables (principal components).

# Gene set enrichment (GSE) :
 
 Analysis is a popular framework for condensing information from gene expression profiles into a pathway or signature summary.

# Tools Used:
R statistical tool.

## Data Description 

 Data Frame : It has 183 columns (Samples) and 18465 rows (Gene ID).

# Data Processing
   Once after the stage of data cleaning check the distribution of gene expression across samples
   These 14098 rows represent Gene ID, and 183 columns represent 183 different samples.
   
# Phantasus tool Visualization has been used as open source online tool (Heat Map).

![data_gene](https://user-images.githubusercontent.com/36000962/75327868-17c63280-58a3-11ea-87b1-2d9e1b5ddfcf.png)


# gene expression distribution for all samples :

                   x-axis :  sample names
                   y-axis :  gene id
                   Range : 0 to 15
                   Colour :  Signififies the Distribution of Gene Expression 


# Gene distribution heat map 

![gene_distribution](https://user-images.githubusercontent.com/36000962/75326736-2875a900-58a1-11ea-9354-4d566826fdda.png)


# Removing  ​ Neuroendocrine​ tumors.

PCA for analysis (Dimensionality reduction )

Data has two groups  Exocrine Neuroendocrine :  2 different clusters of data points.

# Analysis :
  The two components seperation can be easily visualized . Seperated Groups of samples from Neuroendocrine and Exocrine.
# Visualization Plot:

![pca_plot](https://user-images.githubusercontent.com/36000962/75601309-d1114c00-5adf-11ea-90bc-9e5019b39346.png)








 

# Interferons in Pancreatic Adenocarcinoma:

Interferons (IFNs) are a group of signaling proteins made and released by host cells in response to the presence of several pathogens, such as viruses, bacteria, parasites, and also tumor cells. Type I interferons (IFNs) are a large subgroup of interferon proteins that help regulate the activity of the immune system. The genes responsible for type 1 Interferons is called ​ Type 1 IFN signature and consists of a set of 25 genes in homo sapiens and plotting the gene expression distribution as below .


### Image of the Type 1 IFN genes (25 genes) --> it's distribution across samples of Exocrine.

![gene_25]( https://drive.google.com/file/d/1wFY_IYZhyfpjeifLo0Y8ga6SCaICKLA1/view?usp=sharing)

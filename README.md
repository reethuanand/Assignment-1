

# Aim:
To analyze the differentially expressed genes from RNA-Seq data.

# Background:

A large number of computational methods have been recently developed for analyzing the differential 	gene expression (DE) in RNA-Seq data. 
This exercise uses  CmapR tool for data analysis.

## Data set: The measurement consists of ~20,000 genes for 185 pancreatic cancer tumors

## Exploratory Data Analysis:

Principal component analysis (PCA) is a statistical procedure that can be used for exploratory data analysis. PCA uses linear combinations of the original data (e.g. gene expression values) to define a new set of unrelated variables (principal components).

Gene set enrichment (GSE) analysis is a popular framework for condensing information from gene expression profiles into a pathway or signature summary.


# Tools Used:
R statistical tool.

## Context 

Pancreatic Adenocarcinoma (PAAD) is the third most common cause of death from cancer, with an overall 5-year survival rate of less than 5% .RNA-Seq (RNA sequencing), is a sequencing technique to detect the quantity of RNA in a biological sample at a given moment. Here we have a dataset of normalized RNA Sequencing reads for pancreatic cancer tumors​ . The measurement consists of ~20,000 genes for 185 pancreatic cancer tumors. The file format is ​ GCT , a tab-delimited file used for sharing gene expression data and metadata (details for each sample) for samples.

## Data Description 

- **data Frame :** It has 18465 rows (Gene ID) abd 183 columns (Sample Name/ID)

### **Data cleaning **
 Once after the stage of data cleaning check the distribution of gene expression across samples
 These 14098 rows represent Gene ID, and 183 columns represent 183 different samples.

### gene expression distribution for all samples :

x-axis :  sample names
y-axis :  gene id
Range : 0 to 15
Colour :  Signififies the Distribution of Gene Expression 

###  Phantasus tool Visualization has been used as open source online tool .(Heat Map)

![data_gene](https://user-images.githubusercontent.com/36000962/75327868-17c63280-58a3-11ea-87b1-2d9e1b5ddfcf.png)

### gene distribution heat map 

![gene_distribution](https://user-images.githubusercontent.com/36000962/75326736-2875a900-58a1-11ea-9354-4d566826fdda.png)


### Removing  ​ Neuroendocrine​ tumors.

PCA for analysis (Dimensionality reduction )

Data has two groups  Exocrine Neuroendocrine :  2 different clusters of data points.

###  PCA plot:
![pca_plot](https://user-images.githubusercontent.com/36000962/75601309-d1114c00-5adf-11ea-90bc-9e5019b39346.png)


We can see that most of the points are concentrated in the particular range of PC1 and PC2 values. So we can separate the samples from Neuroendocrine and Exocrine. The outliers are -100 > PC1 and PC1 > 100 . I choose this range as it is PC1 and more prominant feature. and other constraint is PC2 < 50. It will provide us to clearly seperate the outliers. So in next step, We'll remove the outlier samples from the dataframe.


### Understand the effect of Interferons in Pancreatic Adenocarcinoma:

Interferons (IFNs) are a group of signaling proteins made and released by host cells in response to
the presence of several pathogens, such as viruses, bacteria, parasites, and also tumor cells. Type I
interferons (IFNs) are a large subgroup of interferon proteins that help regulate the activity of the
immune system. The genes responsible for type 1 Interferons is called ​ Type 1 IFN signature and
consists of a set of 25 genes in homo sapiens.


Now, we know the samples, which fall in category of Pancreatic Adenocarcinoma, and we also know the genes responsible for type1 interferons (Type 1 IFN Signature).
These genes are a set of 25 genes in homosapians.
So To plot the gene expression, for pancreatic adenocarcinoma, We'll create a dataframe with these 25 genes as rows and the Sample name (Which is the index of the pp dataframe.) as columns.


### Image of the Type 1 IFN genes (25 genes) --> it's distribution across samples of Exocrine.

![gene_25](https://user-images.githubusercontent.com/36000962/75326741-2b709980-58a1-11ea-9891-5ef9725f59dc.png)

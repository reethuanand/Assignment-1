
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

![data_gene](https://github.com/reethuanand/Assignment-1-/blob/main/Capture-3.PNG)


# gene expression distribution for all samples :

                   x-axis :  sample names
                   y-axis :  gene id
                   Range : 0 to 15
                   Colour :  Signififies the Distribution of Gene Expression 


# Gene distribution heat map 

![distributionplot](https://github.com/reethuanand/Assignment-1-/blob/main/Capture-1.PNG)


# Removing  ​ Neuroendocrine​ tumors.

PCA for analysis (Dimensionality reduction )

Data has two groups  Exocrine Neuroendocrine :  2 different clusters of data points.

# Analysis :
  The two components seperation can be easily visualized . Seperated Groups of samples from Neuroendocrine and Exocrine.
# Visualization Plot:

![plot](https://github.com/reethuanand/Assignment-1-/blob/main/Capture-2.PNG)








 

# Interferons in Pancreatic Adenocarcinoma:

Interferons (IFNs) are a group of signaling proteins made and released by host cells in response to the presence of several pathogens, such as viruses, bacteria, parasites, and also tumor cells. Type I interferons (IFNs) are a large subgroup of interferon proteins that help regulate the activity of the immune system. The genes responsible for type 1 Interferons is called ​ Type 1 IFN signature and consists of a set of 25 genes in homo sapiens and plotting the gene expression distribution as below .


### Image of the Type 1 IFN genes and it's distribution across samples of Exocrine.

![capture 4](https://github.com/reethuanand/Assignment-1-/blob/main/Capture-4.PNG)






 Image of the Type 1 IFN genes and it's distribution across samples of Exocrine is visualized above from which the analysis include
 distribution of gene across different samples is like it has most values near 9 and 12, 
 colour of heatmap observed : near 9 to 12 and 
 The blue region with less frequency values : near 4 to 5


from GSVA import gsva, gmt_to_dataframe

# Some extras to look at the high dimensional data
from plotnine import *
from sklearn.manifold import TSNE
ifn1.to_csv('ifn1.csv')
!cp ifn1.csv 

'cp' is not recognized as an internal or external command,
operable program or batch file.

genesets_df = gmt_to_dataframe("C:\\Users\\Dell\\geneset.gmt")
genesets_df.head()

name	description	member
0	REACTOME_INTERFERON_GAMMA_SIGNALING	> Interferon gamma signaling	B2M
1	REACTOME_INTERFERON_GAMMA_SIGNALING	> Interferon gamma signaling	CAMK2A
2	REACTOME_INTERFERON_GAMMA_SIGNALING	> Interferon gamma signaling	CAMK2B
3	REACTOME_INTERFERON_GAMMA_SIGNALING	> Interferon gamma signaling	CAMK2D
4	REACTOME_INTERFERON_GAMMA_SIGNALING	> Interferon gamma signaling	CAMK2G
expression_df = pd.read_csv('ifn1.csv',index_col=0)
expression_df.iloc[0:5,0:5]
aab1-Primary solid Tumor	aab4-Primary solid Tumor	aab6-Primary solid Tumor	aab8-Primary solid Tumor	aab9-Primary solid Tumor
rid					
SLC35E2	7.45	8.1	7.2	8.0	7.65
A1BG	6.40	5.8	6.4	5.8	6.70
A2LD1	7.50	6.8	7.3	7.5	7.40
A2M	14.30	14.0	13.1	13.8	14.60
A4GALT	10.60	10.2	10.1	8.6	10.10
 
XV = TSNE(n_components=2).\
fit_transform(expression_df.T)
df = pd.DataFrame(XV).rename(columns={0:'x',1:'y'})
(ggplot(df,aes(x='x',y='y'))
+ geom_point(alpha=0.2)
)

#Plot(GSVA)

![](https://github.com/reethuanand/Assignment-1-/blob/main/Capture-5.PNG)

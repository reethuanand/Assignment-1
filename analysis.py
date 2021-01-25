!pip install cmapPy

import random
from cmapPy.pandasGEXpress.parse import parse
from matplotlib import colors as mcolors
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
notebook_path = os.path.abspath("PAAD.gct") 
notebook_path 
'C:\\Users\\Dell\\PAAD.gct'
data = parse("C:\\Users\\Dell\\PAAD.gct", convert_neg_666=True)
print(data)
GCT1.3
src: C:\Users\Dell\PAAD.gct
data_df: [18465 rows x 183 columns]
row_metadata_df: [18465 rows x 0 columns]
col_metadata_df: [183 rows x 124 columns]
data_df = data.data_df
row_metadata_df = data.row_metadata_df
col_metadata_df = data.col_metadata_df
#Get the 1st dataframe. It has RNA ID  and the Sample Name
data_df.head(6)

cid	aab1-Primary solid Tumor	aab4-Primary solid Tumor	aab6-Primary solid Tumor	aab8-Primary solid Tumor	aab9-Primary solid Tumor	aaba-Primary solid Tumor	aabe-Primary solid Tumor	aabf-Primary solid Tumor	aabh-Primary solid Tumor	aabi-Primary solid Tumor	...	aauh-Primary solid Tumor	aaui-Primary solid Tumor	aaul-Primary solid Tumor	a8t3-Primary solid Tumor	a8t5-Primary solid Tumor	a89d-Solid Tissue Normal	a89d-Primary solid Tumor	a8sy-Primary solid Tumor	a8lh-Primary solid Tumor	aapl-Primary solid Tumor
rid																					
SLC35E2	7.45	8.1	7.2	8.0	7.65	8.1	8.2	8.2	7.55	8.45	...	8.45	7.95	8.3	8.05	8.2	7.25	7.4	7.35	7.2	9.05
A1BG	6.40	5.8	6.4	5.8	6.70	6.6	6.3	6.5	5.70	6.30	...	7.10	7.10	6.7	7.00	6.9	7.10	7.3	7.90	6.0	6.90
A1CF	4.70	5.7	3.0	5.1	4.40	4.2	1.6	6.8	6.00	NaN	...	5.40	6.40	6.5	4.40	3.3	3.60	6.2	1.20	4.9	2.00
A2BP1	-1.00	1.1	NaN	NaN	0.10	NaN	NaN	1.7	0.40	-1.50	...	3.50	1.30	-0.3	NaN	2.1	2.00	0.0	NaN	2.0	NaN
A2LD1	7.50	6.8	7.3	7.5	7.40	6.6	7.1	6.8	8.00	5.80	...	6.50	7.30	6.1	6.70	6.5	6.70	6.7	6.50	6.9	6.70
A2ML1	6.40	NaN	10.8	4.1	9.30	9.8	6.2	3.8	2.30	10.10	...	0.10	3.40	3.7	-0.90	3.6	1.00	2.8	10.50	3.1	5.10
6 rows × 183 columns

# fetching the shape of data
print("Data Shape: {}".format(str(data_df.shape)))
Data Shape: (18465, 183)
new_data_df = data_df.dropna()# data preprocessing
print("Data Shape: {}".format(str(new_data_df.shape)))
Data Shape: (14098, 183)
# get gene names in the list "id" 
id = list(new_data_df.index.values.tolist()) 
print(id[:7])    
['SLC35E2', 'A1BG', 'A2LD1', 'A2M', 'A4GALT', 'AAAS', 'AACS']
# get sample names in the list "cid" 
cid = list(new_data_df.columns.values.tolist())
print(cid[:7])
['aab1-Primary solid Tumor', 'aab4-Primary solid Tumor', 'aab6-Primary solid Tumor', 'aab8-Primary solid Tumor', 'aab9-Primary solid Tumor', 'aaba-Primary solid Tumor', 'aabe-Primary solid Tumor']
gene_exp = new_data_df.values.tolist()
print('Length of gene_expression list : {}'.format(len(gene_exp)))
print('element length of gene_expression : {}'.format(len(gene_exp[0])))
Length of gene_expression list : 14098
element length of gene_expression : 183
#Applying exploratory dimensionality rediction data analysis
#Creating numpy array for further analysis. (We'll use PCA Technique for dimensionality reduction)
xx = new_data_df.values.T
xx.shape
(183, 14098)

scaler = StandardScaler()
xx = scaler.fit_transform(xx)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
yy = pca.fit_transform(xx)
 
#This is the variance of gene expression across all samples (Calculated using PCA.)
print(pca.explained_variance_ratio_)
yy.shape
[0.16429952 0.11939816]
(183, 2)
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]
sorted_names

c = ["orange", "purple", "violet", "crimson", "brown", "maroon", "black", "maroon", "orange", "lightyellow", "darkgreen", "deeppink", "royalblue", "darkred", "darkgray"]
histological_unique = [str(i) for i in list(col_metadata_df['histological_type_other'].unique())]
histological_unique

['invasive adenocarcinoma',
 'invasive, well-differentiated',
 'nan',
 'poorly differentiated adenocarcinoma',
 'neuroendocrine',
 'neuroendocrine carcinoma nos',
 '82463 neuroendocrine carcinoma nos',
 'neuroendocrine carcinoma',
 'adenocarcinoma, nos',
 'poorly differentiated pancreatic adenocarcinoma',
 'not specified',
 'intraductal tubulopapillary neoplasm',
 'ductal and micropapillary',
 'adenocarcinoma- nos',
 'moderately differentiated ductal adenocarcinoma 60% + neuroendocrine 40%']
 
color_dictionary = dict()
for label, c in zip(histological_type_other_unique, c):
    color_dictionary[label] = c
    
color_dictionary
{'invasive adenocarcinoma': 'orange',
 'invasive, well-differentiated': 'purple',
 'nan': 'violet',
 'poorly differentiated adenocarcinoma': 'crimson',
 'neuroendocrine': 'brown',
 'neuroendocrine carcinoma nos': 'maroon',
 '82463 neuroendocrine carcinoma nos': 'black',
 'neuroendocrine carcinoma': 'maroon',
 'adenocarcinoma, nos': 'orange',
 'poorly differentiated pancreatic adenocarcinoma': 'lightyellow',
 'not specified': 'darkgreen',
 'intraductal tubulopapillary neoplasm': 'deeppink',
 'ductal and micropapillary': 'royalblue',
 'adenocarcinoma- nos': 'darkred',
 'moderately differentiated ductal adenocarcinoma 60% + neuroendocrine 40%': 'darkgray'}
labels = [color_dictionary[str(i)] for i in list(col_metadata_df['histological_type_other'])]
plt.scatter(yy[:,0], yy[:,1], c=labels)
<matplotlib.collections.PathCollection at 0xe8e42c2220>

import pandas as pd
p = pd.DataFrame(yy, columns=['PC1', 'PC2'], index=cid)
p.head()

PC1	PC2
aab1-Primary solid Tumor	23.225199	-14.563444
aab4-Primary solid Tumor	4.242102	-14.212575
aab6-Primary solid Tumor	28.721006	-27.624325
aab8-Primary solid Tumor	-0.725020	-24.624243
aab9-Primary solid Tumor	0.321681	2.133418

import os
path = os.path.abspath("type1_IFN.txt") 
path
'C:\\Users\\Dell\\type1_IFN.txt'
# knowing the category of Pancreatic Adenocarcinoma, the genes responsible for type1 interferons (Type 1 IFN Signature) A dataframe with these 25 genes as rows and the Sample name (Which is the index of the pp dataframe.) as columns.
import pandas as pd
pp = pd.DataFrame(yy, columns=['PC1', 'PC2'], index=cid)
pp.head()
PC1	PC2
aab1-Primary solid Tumor	23.225199	-14.563444
aab4-Primary solid Tumor	4.242102	-14.212575
aab6-Primary solid Tumor	28.721006	-27.624325
aab8-Primary solid Tumor	-0.725020	-24.624243
aab9-Primary solid Tumor	0.321681	2.133418
##Removing outliers

index_Name = pp[ (pp['PC1'] < -100) | (pp['PC1'] > 100) | (pp['PC2'] > 50)].index
index_Name
Index(['aabv-Primary solid Tumor', 'aaqm-Primary solid Tumor',
       'a9ij-Primary solid Tumor', 'a9il-Primary solid Tumor',
       'a9in-Primary solid Tumor', 'a9io-Primary solid Tumor',
       'a9ir-Primary solid Tumor', 'a9is-Primary solid Tumor',
       'a9iv-Primary solid Tumor', '6880-Primary solid Tumor',
       'a45n-Solid Tissue Normal', 'a7ol-Primary solid Tumor',
       'a7op-Primary solid Tumor', '8519-Primary solid Tumor',
       '7897-Primary solid Tumor', 'a75w-Primary solid Tumor'],
      dtype='object')
print('No of Neuroendocrine Tumors are: {}'.format(len(indexNames)))
No of Neuroendocrine Tumors are: 16
 
 
def configure_plotly_browser_state():
    '''It enables to display the plotly graphs'''
    import IPython
    display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-1.5.1.min.js?noext',
            },
          });
        </script>
        '''))
        
!pip install plotly
#Plotly Express is the easy-to-use, high-level interface to Plotly, 
#which operates on a variety of types of data and produces easy-to-style figures.
#With px.imshow,each value of the input array or data frame is represented as a heatmap pixel.
Requirement already satisfied: plotly in c:\users\dell\anaconda3\lib\site-packages (4.14.3)
Requirement already satisfied: retrying>=1.3.3 in c:\users\dell\anaconda3\lib\site-packages (from plotly) (1.3.3)
Requirement already satisfied: six in c:\users\dell\anaconda3\lib\site-packages (from plotly) (1.15.0)
configure_plotly_browser_state()
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()

fig = go.Figure(data=go.Heatmap(
                   z=gene_exp[0:100],
                   x=cid[0:100],
                   y=id[0:100],
                   hoverongaps = False))
fig.show()

## visualization of gene expression values across all samples
import os
notebook_path = os.path.abspath("type1_IFN.txt")
 notebook_path
'C:\\Users\\Dell\\type1_IFN.txt'
with open('C:\\Users\\Dell\\type1_IFN.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
# content contains 25 genes
 
new_data_df = data_df.dropna()# data preprocessing
ifn1 = new_data_df.loc[content]  ##.loc is primarily label based, but may also be used with a boolean array. .loc will raise KeyError when the items are not found. Allowed inputs are:
 
## Doing reindexing inorder to avoid key error 
#The idiomatic way to achieve selecting potentially not-found elements is via .reindex()
ifn1 = new_data_df.reindex()           
## Reindexing being done due to rise of keyerror
## reindexing : https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#deprecate-loc-reindex-listlike%22
 
ifn1.shape
(14098, 183)
indexNames = pp[ (pp['PC1'] < -100) | (pp['PC1'] > 100) | (pp['PC2'] > 50)].index
indexNames
Index([], dtype='object')
pp.drop(indexNames, inplace=True)
pp.info()
<class 'pandas.core.frame.DataFrame'>
Index: 167 entries, aab1-Primary solid Tumor to aapl-Primary solid Tumor
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   PC1     167 non-null    float32
 1   PC2     167 non-null    float32
dtypes: float32(2)
memory usage: 7.6+ KB
indexNames = indexNames.to_list()
indexNames 
[]

ifn1 = ifn1.drop(indexNames, axis=1)
ifn1.shape
(14098, 183)
configure_plotly_browser_state()     ## For each heatmap, the color is defined by the z1 values
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()

fig = go.Figure(data=go.Heatmap(
                   z=ifn1.values,
                   x=ifn1.columns,
                   y=ifn1.index,
                   hoverongaps = False))
fig.show()
## Image of the Type 1 IFN genes and it's distribution across samples of Exocrine is visualized above from which the analysis include

# distribution of gene across different samples is like it has most values near 9 and 12, 
#  colour of heatmap observed : near 9 to 12 and 
# The blue region with less frequency values : near 4 to 5



print("Number of Misssing: {}".format(data_df.shape[0] - new_data_df.shape[0]))
Number of Misssing: 4367
!pip install GSVA
!pip install plotnine
#### Workflow example - Go from an expression-based tSNE plot to a pathway-based tSNE plot in a Jupyter notebook

# Here we will convert a per-sample pe

r-gene expression matrix to a per-sample per-pathway enrichment matrix.
#We will plot the values using tSNE.


import pandas as pd
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

<ggplot: (62414665780)>
##The default command runs without verbose message output. but take notice, 
## that genes that are not part of the `expression_df` are dropped from the analysis, 
## and depending on your choice of GSVA method, 
## genes for which there is not enough expression (i.e. all zero expression) will be dropped.

'''pathways_df = gsva(expression_df,genesets_df)
pathways_df.iloc[0:5,0:5]'''
''' YV = TSNE(n_components=2).\
fit_transform(pathways_df.T)
pf = pd.DataFrame(YV).rename(columns={0:'x',1:'y'})
(ggplot(pf,aes(x='x',y='y'))
+ geom_point(alpha=0.2)
)'''

import pandas as pd

# Import data
bsrn = pd.read_csv('../data/BSRN_GOB_2019-10.csv',index_col=0,parse_dates=True)

bsrn.head()

#%% THis divides a .py into a cell.
# This a comment
url = 'https://raw.githubusercontent.com/environmental-data-science/eds-217/main/data/AS00601.csv'
# Some species data 
mack_verts = pd.read_csv(url)


# %%
import dask.dataframe as dd

# %%

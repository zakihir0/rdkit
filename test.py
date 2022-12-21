# %%
import pandas as pd
from rdkit import rdBase, Chem

dataset = pd.read_csv("csv/molecules_with_boiling_point.csv", index_col=0)
dataset = dataset.reset_index(drop=True)
# %%

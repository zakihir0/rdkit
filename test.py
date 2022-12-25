# %%
import pandas as pd
import streamlit as st
from PIL import Image

from rdkit import Chem, rdBase
from rdkit.Chem import Draw
#%%
dataset = pd.read_csv("csv/molecules_with_boiling_point.csv", index_col=0)
dataset = dataset.reset_index(drop=True)

mols = [Chem.MolFromSmiles(i) for i in dataset['SMILES']]
Drawing = Draw.MolsToGridImage(mols)
#%%
Drawing = Draw.MolsToImage(mols)
st.image(Drawing)
# %%

import numpy as np
import pandas as pd
import os

'''
Count	
Tradelist Count	
Name	
Edition	
Condition -> por extenso: "Near Mint"
Language
Foil -> "foil" ou "etched"
Tags -> empty
Last Modified -> "2023-03-30 03:03:46.243000"
Collector Number	
Alter -> "FALSE"	
Proxy -> "FALSE"	
Purchase Price -> empty
''''

df_ligamagic = pd.read_csv(os.path.dirname(__file__) + "/padrao_liga.csv",  encoding='latin-1')

print(df_ligamagic.head())
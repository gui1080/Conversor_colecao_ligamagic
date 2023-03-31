import numpy as np
import pandas as pd
import os

'''
> MOXFIELD
Count -> 1 -> quantas cartas dessa vc tem?
Tradelist Count	-> 1
Name	
Edition	-> Sigla
Condition -> por extenso: "Near Mint"
Language -> English, Portuguese
Foil -> "foil" ou "etched"
Tags -> empty
Last Modified -> "2023-03-30 03:03:46.243000"
Collector Number -> id da carta, integer
Alter -> "FALSE"	
Proxy -> "FALSE"	
Purchase Price -> empty
'''

df_ligamagic = pd.read_csv(os.path.dirname(__file__) + "/padrao_liga.csv",  encoding='latin-1')

print("Colunas do formato da Ligamagic")
print(list(df_ligamagic.columns))

'''
> LIGAMAGIC
Edicao (PTBR)
Edicao (EN)
Edicao (Sigla)
Card (PT)
Card (EN)
Quantidade
Qualidade (M NM SP MP HP D)
Idioma (BR EN DE ES FR IT JP KO RU TW)
Raridade (M R U C)
Cor (W U B R G M A L) 
Extras
Card #
Comentario
'''
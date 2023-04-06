import numpy as np
import pandas as pd
from datetime import datetime
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

colunas_moxfield = ["Count", "Tradelist Count", "Name", "Edition", "Condition", 
                    "Language", "Foil", "Tags", "Last Modified", "Collector Number", 
                    "Alter", "Proxy", "Purchase Price"]

df_moxfield = pd.DataFrame([], columns=colunas_moxfield)

cartas = 0

for index, row in df_ligamagic.iterrows():
    
    edicao = str(row["Edicao (Sigla)"])
    name = str(row["Card (EN)"])
    count = str(row["Quantidade"])

    # qualidade tem que passar de sigla pra extenso
    qualidade_liga = str(row["Qualidade (M NM SP MP HP D)"])

    if qualidade_liga == "M":
        qualidade = "Mint"
    elif qualidade_liga == "NM":
        qualidade = "Near Mint"
    elif qualidade_liga == "SP":
        qualidade = "Slightly Played"
    elif qualidade_liga == "MP":
        qualidade = "Moderately Played"
    elif qualidade_liga == "HP":
        qualidade = "Heavily Played"
    elif qualidade_liga == "D":
        qualidade = "Damaged"
    else:
        qualidade = "Near Mint"

    # na coluna de "Extras" da ligamagic
    # pode ser que a carta seja "Foil" ou "Etched Foil"
    # isso entra na coluna do moxfield "Foil"
    # como "foil" ou "etched"

    liga_extra = str(row["Extras"]).lower()

    if "etched" in liga_extra:
        foil = "etched"
    elif "foil" in liga_extra:
        foil = "foil"
    else:
        foil = ""


    colec_num = str(row["Card #"])

    tag = ""
    alter = "False"
    proxy = "False"
    purchase_price = ""
    tradelist = "1"

    # idioma
    # de sigla para extenso no moxfield

    idioma_liga = str(row["Idioma (BR EN DE ES FR IT JP KO RU TW)"])

    if idioma_liga == "BR":
        idioma = "Portuguese"
    elif idioma_liga == "EN":
        idioma = "English"
    elif idioma_liga == "ES":
        idioma = "Spanish"
    elif idioma_liga == "DE":
        idioma = "Spanish"
    elif idioma_liga == "FR":
        idioma = "Spanish"
    elif idioma_liga == "IT":
        idioma = "Spanish"
    elif idioma_liga == "JP":
        idioma = "Japanese"
    elif idioma_liga == "KO":
        idioma = "Korean"
    elif idioma_liga == "RU":
        idioma = "Russian"
    elif idioma_liga == "TW":
        idioma = "Korean"
    else:
        idioma = "English"

    # ultima modificacao = tempo no formato correto
    # "2023-03-30 03:03:46.243000"
    now = datetime.now()
    date_time = str(now.strftime("%Y-%m-%d %H:%M:%S.%f"))
    cartas += 1

    df_moxfield.loc[len(df_moxfield)] = [count, tradelist, name, edicao, qualidade, idioma, foil, tag, date_time, colec_num, alter, proxy, purchase_price]

print("\n--------------------\n\nFIM!\nCartas processadas - " + str(cartas) + "\n--------------------\n\n")

print("\n\nNomes\n")

print(df_moxfield["Name"])

print("\n\nNúmeros de coleção\n")

print(df_moxfield["Collector Number"])

print("\n--------------------\n\n")

print(df_moxfield.info())

print("\n--------------------\n\n")

# exporta dados para CSV

df_moxfield.to_csv("liga_moxfield_export"+date_time+".csv", encoding='utf-8', index=False)

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
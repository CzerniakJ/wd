import xlrd
import openpyxl
import pandas as pd
import numpy as np

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

for row in df.itertuples():
    if row.Liczba > 1000:
        print(row.Rok,row.Imie,row.Liczba)

for row in df.itertuples():
    if row.Imie == "JAKUB":
        print(row.Rok,row.Imie,row.Liczba)

print(df['Liczba'].sum())

for row in df.itertuples():
    if row.Rok >= 2000 and row.Rok <= 2005:
        print(row.Rok,row.Imie,row.Liczba)


print(df.groupby('Plec')['Liczba'].sum())

print(df.groupby(['Rok', 'Plec'])['Liczba'].max())

print(df.groupby(['Plec'])['Liczba'].max())
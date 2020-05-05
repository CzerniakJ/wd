import xlrd
import openpyxl
import pandas as pd
import numpy as np

df = pd.read_csv('zad3.scv',sep = ';')

for Sprzedawca in df['Sprzedawca'].unique():
    print(Sprzedawca)

print(df.nlargest(5, ['Utarg'])) 

print(df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))

print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))

print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg': ['sum']}).tail(1))

print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg': ['mean']}))
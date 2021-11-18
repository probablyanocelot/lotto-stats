import os
import pandas as pd

for file in os.listdir('./sheets/'):
    if file.endswith(".csv"):
        df = pd.read_csv('./sheets/' + file)
        df['Filename'] = file
        df.to_csv('./sheets/' + file, index=False)
    if file.endswith(".xlsx"):
        df = pd.read_excel('./sheets/' + file)
        df['Filename'] = file

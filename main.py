import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

EFTs=pd.read_csv("ETFs.csv")

print(EFTs.head())

print(EFTs.info())

print(EFTs.columns)

print(EFTs.index)

print(EFTs.head(5))

MFunds=pd.read_csv("Mutual Funds.csv", low_memory=False)

print(MFunds.head())
print(MFunds.shape)
print(MFunds.info)







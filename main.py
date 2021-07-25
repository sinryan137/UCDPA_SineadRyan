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

[col for col in EFTs.columns if EFTs[col].isnull().any()]
[col for col in MFunds.columns if MFunds[col].isnull().any()]

EFTs[EFTs.duplicated()]
MFunds[MFunds.duplicated()]





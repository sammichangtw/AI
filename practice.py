import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('data/train.csv')
df2 = pd.read_csv('data/test.csv')

df = df1.append(df2)

df = df.reset_index()




print(df)
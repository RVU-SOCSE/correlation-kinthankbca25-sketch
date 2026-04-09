import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df2 = pd.read_csv(r"C:/Users/kinth/OneDrive/Scans/laptop.csv")
sns.heatmap(df2.corr(numeric_only=True),annot=True)

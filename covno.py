import pandas as pd
from scipy.stats import chi2_contingency
df=pd.read_csv('nom_corr.csv')
print(df)
print()
df=pd.read_csv('nom_corr.csv')
contingency_table=pd.crosstab(df['a'],df['b'])
print(contingency_table)
chi2,p,dof,expected=chi2_contingency(contingency_table)
print("chi2 values is: ",chi2)
print("pvalue is: ",p)
print("degree of freedom: ",dof)
print("expected freqency: ",expected)
alpha=0.05
if p<alpha:
       print("a &b are correlated")
else: 
       print("there is no correlation")                                                                                         

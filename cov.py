import pandas as pd 
import numpy as np
import statistics as st
csv_file="cov.csv"
df=pd.read_csv(csv_file)
data=df.values.tolist()
row1,row2=[],[]
for i in data:
        row1.append(i[0])
        row2.append(i[1])
row1_mean=np.mean(row1)
row2_mean=np.mean(row2) 
row1_std=st.stdev(row1)
row2_std=st.stdev(row2)
correlation=0.00
covariance=0.00
n=len(data)
for i in range(n):
        correlation=correlation+((row1[i]-row1_mean)*(row2[i]-row2_mean)/((n-1)*(row1_std)*(row2_std)))
        covariance=covariance+((row1[i]-row1_mean)*(row2[i]-row2_mean)/n)
        covariance=correlation*((row1_std)*(row2_std))
print("correlation: ",correlation)
print("covariance: ",covariance)  

if correlation==0:
       print("no correlation")
elif correlation>0:
       print("positive correlation")
elif correlation<0:
       print("negative correlation")
value=np.corrcoef(row1,row2)
print("correlation coefficient using function: ",value[0,1])
val=np.cov(row1,row2)      
print("covariance using function: ",val[0,1])

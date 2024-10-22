import csv
def nominal_dissimilarity(data,dissim):
          for i in range(len(data)):
                         temp=[]
                         for j in range(i+1):
                                 if(data[i]==data[j]):
                                         temp.append(0)
                                 else:
                                     temp.append(1)
                         dissim.append(temp)
          dissimilarity_matrix('nominal',dissim)
          
def numeric_dissimilarity(data,dissim):
    datarange=max(data)-min(data)
    for i in range (len(data)):
         temp=[]
         for j in range(i+1):
                    man_dist=(abs(data[i]-data[j]))/datarange
                    temp.append(round(man_dist,2))
         dissim.append(temp)
    dissimilarity_matrix('Numeric',dissim)

def mixed_dissimilarity(num_dissim,nom_dissim,dissim):
       for i in range(len(nom_dissim)):
              temp=[]
              for j in range(i+1):
                    temp.append(round((num_dissim[i][j]+nom_dissim[i][j])/2,2))
              dissim.append(temp)
       dissimilarity_matrix('mixed',dissim)                                                                        

def dissimilarity_matrix(type,dissim):
       print()
       print(type,'dissimilarity matrix\n')
       for i in dissim:
             print(i)
       print()
datafile=open('disdata.csv','r')
reader=csv.reader(datafile)
nominal_data=[]
numeric_data=[]
for row in reader:
          nominal_data.append(row[0])
          numeric_data.append(int(row[1]))
print('nominal data',nominal_data)
print('numeric data',numeric_data)
nom_dissim=[]
num_dissim=[]
mixed_dissim=[]
nominal_dissimilarity(nominal_data,nom_dissim)
numeric_dissimilarity(numeric_data,num_dissim)
mixed_dissimilarity(num_dissim,nom_dissim,mixed_dissim)
datafile.close()                        
                    

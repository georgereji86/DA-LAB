import numpy as np

with open("statdata.csv", "r") as f:
    f1 = f.read()

x = f1.split(",")
y = [int(i) for i in x]
y.sort()
z = np.array(y)

d = {}
for i in y:
    d[i] = y.count(i)

a = max(d.values())
mode = [i for i in d if d[i] == a]

if len(mode) == 1:
    mode_type = "Unimodal"
elif len(mode) == 2:
    mode_type = "Bimodal"
elif len(mode) == 3:
    mode_type = "Trimodal"
elif len(mode) == len(y):
    mode_type = "No mode"
else:
    mode_type = "Multimodal"


q0 = np.quantile(y, 0.0)
q1 = np.quantile(y, 0.25)
q2 = np.quantile(y, 0.5)
q3 = np.quantile(y, 0.75)
q4 = np.quantile(y, 1.0)

print("Quartiles")
print("Q0:", q0)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)
print("Q4:", q4)

iqr = q3 - q1

lo = q1 - 1.5 * iqr
uo = q3 + 1.5 * iqr

print("Original Values:", y)

filtered_values = [i for i in y if lo <= i <= uo]
outliers = [i for i in y if i < lo or i > uo]

print("After removing outliers:", filtered_values)
print("Outliers:", outliers)
mean = np.mean(filtered_values)
median = np.median(filtered_values)
print("Mean:", mean)
print("Median:", median)
print("Mode type:", mode_type)
print("Mode:", mode)

var = np.var(filtered_values)
sd = np.sqrt(var)
print("Standard Deviation:", sd)
print("max: ",q0)
print("min: ",q4)


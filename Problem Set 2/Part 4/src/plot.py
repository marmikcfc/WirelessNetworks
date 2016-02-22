from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
    # Build X/Y arrays from file 1
f1 = open('heurestic_one.txt')
f2 = open('heurestic_two.txt')
f3 = open('heurestic_three.txt')

lines = f1.readlines()
x = []
y1 = []
y2=[]
y3=[]

i=1
for line in lines:
    line = line.replace("\n", "")
    vals = line.split(" ")
    x.append(float(i))
    y1.append(float(vals[1]))
    i+=1

lines = f2.readlines()
for line in lines:
    line = line.replace("\n", "")
    vals = line.split(" ")
    y2.append(float(vals[1]))
    i+=1

lines = f3.readlines()
for line in lines:
    line = line.replace("\n", "")
    vals = line.split(" ")
    y3.append(float(vals[1]))
    i+=1
    # Run regression
gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y1)
print (gradient, intercept, r_value, p_value, std_err)
# plt.scatter(x, y)
# plt.plot((y, (gradient*x + inter)cept))
#plt.scatter(x,y)


best=[np.mean(y1),np.mean(y2),np.mean(y3)]
xBest=[1,2,3]
plt.plot(xBest,best)
plt.ylabel('Number of Access Points')
plt.xlabel('Heurestic')
plt.show()
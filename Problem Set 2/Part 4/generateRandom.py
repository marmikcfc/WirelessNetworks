from random import randint

#Starts with 0,0
#Pics up a random point from outside the coverage range from access point at that point
#and adds it to the list

xCoverage, yCoverage = 0, 0
finalPoints = list()
for i in range(10):
	point = {(randint(xCoverage,xCoverage+2),randint(yCoverage,yCoverage+2))}
	finalPoints.append(point)
	for j in range(10):
		point = {(randint(xCoverage+1,xCoverage+2),randint(yCoverage+1,yCoverage+2))}
		finalPoints.append(point)
		yCoverage= yCoverage+2
	xCoverage, yCoverage=xCoverage+2, 0

print (finalPoints)

print("#################################################")

for i in range(len(finalPoints)):
	point = {(randint(0,20),randint(0,20))}
	finalPoints.append(point)

print (len(finalPoints))


from random import randint

##################################################################################
# Part 1                                                                         #
##################################################################################

#Starts with 0,0
#Picks up a random point from outside the coverage range from access point at that point
#and adds it to the list

xCoverage, yCoverage = 0, 0
finalPoints = list()
for i in range(10):
	point = [randint(xCoverage,xCoverage+2)]
	point.append(randint(yCoverage,yCoverage+2))
	finalPoints.append(point)
	for j in range(10):
		point = [randint(xCoverage+1,xCoverage+2)]
		point.append(randint(yCoverage+1,yCoverage+2))
		finalPoints.append(point)
		yCoverage= yCoverage+2
	xCoverage, yCoverage=xCoverage+2, 0

print (finalPoints)

print("#################################################")
# adds m more points
for i in range(len(finalPoints)):
	point = [randint(0,20),randint(0,20)]
	finalPoints.append(point)

print (finalPoints)

##################################################################################
# Part 2                                                                         #
##################################################################################

# Heurestic One:
# Start with empty list
# While(currentCoverage != TotalCoverage ) 
# add point from M
# CurrentCoverage +=200 



def heurestic_ONE():
	finalList = finalPoints.sort
	apList = list()
	x=finalPoints[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+2, x[1]+2
	xpt = x[0]
	
	for i in range(len(finalPoints)):
		x=finalPoints[i]
		if x[1] -2 <=YCoverage and x not in apList and YCoverage<20 and x[1]>YCoverage:
			YCoverage = YCoverage + 2
			apList.append(x)

	while XCoverage <20:
		YCoverage = 2
		for i in range(len(finalPoints)):
			x = list(finalPoints[i])
			if(x[0]-2 <=XCoverage and x not in apList and x[0]>XCoverage and XCoverage<20):
				XCoverage = x[0] + 2
				YCoverage = x[1] + 2
				apList.append(x)

		for i in range(len(finalPoints)):
			x=list(finalPoints[i])
			if(x[1]-2 <= YCoverage and x[1] > YCoverage  and x not in apList and YCoverage<20):
				YCoverage = YCoverage+2
				apList.append(x)



	print("################################")
	print(len(apList))
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print(sorted(apList))


def heurestic_ONE_with():

	apList = list()
	x=finalPoints[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+2, x[1]+2

	while(XCoverage < 20):
		xpt=-1
		YCoverage = 2
		for i in range(len(finalPoints)):
			x=list(finalPoints[i])
			if(x[0]-2 <= XCoverage):
				XCoverage+=2
				YCoverage+=2
				xpt = x[0]
				apList.append(x)

		for i in range(len(finalPoints)):
			x=list(finalPoints[i])
			if(x[1]-2 <= YCoverage and x not in apList and x[0] == xpt and YCoverage<20):
				YCoverage +=2
				apList.append(x)

	print("################################")
	print(len(apList))


def heurestic_TWO():
	print("################################")
	finalList = finalPoints
	finalList.sort()
	print(finalList)
	apList = list()
	X_Coverage = 2
	apList.append(finalList[0])
	i=1
	Y_Coverage = 2
	while X_Coverage <20 and i<len(finalList):
		if(finalList[i] - 2 >=X_Coverage):
			apList.append(finalList.i)
			X_Coverage =X_Coverage+2
			Y_Coverage = Y_Coverage+2




heurestic_ONE()
heurestic_ONE_with()
heurestic_TWO()

from random import randint
import threading
import time
import sys

##################################################################################
# Part 1                                                                         #
##################################################################################

#Starts with 0,0
#Picks up a random point from outside the coverage range from access point at that point
#and adds it to the list
#Time Complexity O(n)



def generateData():
	xCoverage, yCoverage = 0, 0
	finalPoints = []
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
	return finalPoints

##################################################################################
# Part 2                                                                         #
##################################################################################

# Heurestic One:
# Start with empty list
# While(currentCoverage != TotalCoverage ) 
# add point from M
# CurrentCoverage +=200 
# Time Complexity O(n^2)


def heurestic_ONE():
	finalPoints = generateData()
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
	text_file = open("heurestic_one.txt", "a")
	text_file.write("\n %s" % len(apList))
	text_file.close()
	



# Heurestic Two:
# Sort the list
# Start with empty list
# While(currentCoverage != TotalCoverage ) 
# add point from M
# CurrentCoverage +=200 
# Time Complexity O(nlogn + n^2)


def heurestic_TWO():
	finalPoints = generateData()
	print("################heurestic_TWO################")
	finalList = finalPoints
	finalList = sorted(finalPoints)
	apList = list()
	x=finalList[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+2, x[1]+2
	xpt = x[0]
	for i in range(1,len(finalList)):
		x = finalList[i]
		if(YCoverage < 20 and x not in apList and x[1] -3 == YCoverage and x[1]>YCoverage):
			YCoverage = YCoverage +2
			apList.append(x)

	while XCoverage <20:
		YCoverage = 2
		for i in range(len(finalList)):
			x = list(finalList[i])
			if(x[0]-2 <=XCoverage and x not in apList and x[0]>XCoverage and XCoverage<20):
				XCoverage = x[0] + 2
				YCoverage = x[1] + 2
				apList.append(x)

		for i in range(len(finalList)):
			x=list(finalList[i])
			if(x[1]-2 <= YCoverage and x[1] > YCoverage  and x not in apList and YCoverage<20):
				YCoverage = YCoverage+2
				apList.append(x)


	print("################################")
	text_file = open("heurestic_two.txt", "a")
	text_file.write("\n %s" % len(apList))
	text_file.close()
	

# Heurestic Three:
# Sorts the list
# traverses the Sorted list by adding 400 to the coverage
# to find exactly the minimum number of AP required
# Time Complexity O(nlogn + n^2)
#


def heurestic_THREE():
	finalPoints = generateData()
	finalList = sorted(finalPoints)
	apList = list()
	x=finalList[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+3, x[1]+3
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
	text_file = open("heurestic_three.txt", "a")
	text_file.write("\n %s" % len(apList))
	text_file.close()

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        # Get lock to synchronize threads
        if(self.threadID == 1):
        	for i in range(1,100):
        		print(i)
	        	heurestic_ONE()
        if self.threadID == 2:
        	for i in range(1,100):
	        	heurestic_TWO()
        if self.threadID == 3:
        	for i in range(1,100):
	        	heurestic_THREE()
        # Free lock to release next thread


#thread1 = myThread(1)
#thread2 = myThread(2)
thread3 = myThread(3)

#thread1.start()
#thread2.start()
thread3.start()



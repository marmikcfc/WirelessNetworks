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



# def generateData():
# 	xCoverage, yCoverage = 0, 0
# 	finalPoints = []
# 	for i in range(1000):
# 		point = [randint(xCoverage,xCoverage+200)]
# 		point.append(randint(yCoverage,yCoverage+200))
# 		finalPoints.append(point)
# 		for j in range(1000):
# 			point = [randint(xCoverage+100,xCoverage+200)]
# 			point.append(randint(yCoverage+100,yCoverage+200))
# 			finalPoints.append(point)
# 			yCoverage= yCoverage+200
# 		xCoverage, yCoverage=xCoverage+200, 0

# 	print (finalPoints)

# 	print("#################################################")
# 	# adds m more points
# 	for i in range(len(finalPoints)):
# 		point = [randint(0,2000),randint(0,2000)]
# 		finalPoints.append(point)

# 	print (finalPoints)
# 	return finalPoints



xCoverage, yCoverage = 0, 0
finalPoints = []
for i in range(1000):
	point = [randint(xCoverage,xCoverage+200)]
	point.append(randint(yCoverage,yCoverage+200))
	finalPoints.append(point)
	for j in range(1000):
		point = [randint(xCoverage+100,xCoverage+200)]
		point.append(randint(yCoverage+100,yCoverage+200))
		finalPoints.append(point)
		yCoverage= yCoverage+200
	xCoverage, yCoverage=xCoverage+200, 0

print (finalPoints)

print("#################################################")
	# adds m more points
for i in range(len(finalPoints)):
	point = [randint(0,2000),randint(0,2000)]
	finalPoints.append(point)

print (finalPoints)

text_file = open("data.txt", "a")
text_file.write("\n Length %s" % finalPoints)
text_file.close()
	


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
#	finalPoints = generateData()
	apList = list()
	x=finalPoints[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+200, x[1]+200
	xpt = x[0]
	
	for i in range(len(finalPoints)):
		x=finalPoints[i]
		if x[1] -200 <=YCoverage and x not in apList and YCoverage<2000 and x[1]>YCoverage:
			YCoverage = YCoverage + 200
			apList.append(x)

	while XCoverage <2000:
		YCoverage = 200
		for i in range(len(finalPoints)):
			x = list(finalPoints[i])
			if(x[0]-200 <=XCoverage and x not in apList and x[0]>XCoverage and XCoverage<2000):
				XCoverage = x[0] + 200
				YCoverage = x[1] + 200
				apList.append(x)

		for i in range(len(finalPoints)):
			x=list(finalPoints[i])
			if(x[1]-200 <= YCoverage and x[1] > YCoverage  and x not in apList and YCoverage<200):
				YCoverage = YCoverage+200
				apList.append(x)



	print("################################")
	text_file = open("heurestic_one.txt", "a")
	text_file.write("\n Length %s" % len(apList))
	text_file.close()
	



# Heurestic Two:
# Sort the list
# Start with empty list
# While(currentCoverage != TotalCoverage ) 
# add point from M
# CurrentCoverage +=200 
# Time Complexity O(nlogn + n^2)


def heurestic_TWO():
#	finalPoints = generateData()
	print("################heurestic_TWO################")
	finalList = finalPoints
	finalList = sorted(finalPoints)
	apList = list()
	x=finalList[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+200, x[1]+200
	xpt = x[0]
	for i in range(1,len(finalList)):
		x = finalList[i]
		if(YCoverage < 2000 and x not in apList and x[1] -300 == YCoverage and x[1]>YCoverage):
			YCoverage = YCoverage +200
			apList.append(x)

	while XCoverage <2000:
		YCoverage = 200
		for i in range(len(finalList)):
			x = list(finalList[i])
			if(x[0]-200 <=XCoverage and x not in apList and x[0]>XCoverage and XCoverage<2000):
				XCoverage = x[0] + 200
				YCoverage = x[1] + 200
				apList.append(x)

		for i in range(len(finalList)):
			x=list(finalList[i])
			if(x[1]-200 <= YCoverage and x[1] > YCoverage  and x not in apList and YCoverage<2000):
				YCoverage = YCoverage+200
				apList.append(x)


	print("################################")
	text_file = open("heurestic_two.txt", "a")
	text_file.write("\n Length %s" % len(apList))
	text_file.close()
	

# Heurestic Three:
# Sorts the list
# traverses the Sorted list by adding 400 to the coverage
# to find exactly the minimum number of AP required
# Time Complexity O(nlogn + n^2)
#


def heurestic_THREE():
#	finalPoints = generateData()
	finalList = sorted(finalPoints)
	apList = list()
	x=finalList[0]
	apList.append(x)
	XCoverage, YCoverage = x[0]+300, x[1]+300
	xpt = x[0]
	
	for i in range(len(finalPoints)):
		x=finalPoints[i]
		if x[1] -300 <=YCoverage and x not in apList and YCoverage<2000 and x[1]>YCoverage:
			YCoverage = YCoverage + 300
			apList.append(x)

	while XCoverage <2000:
		YCoverage = 300
		for i in range(len(finalPoints)):
			x = list(finalPoints[i])
			if(x[0]-300 <=XCoverage and x not in apList and x[0]>XCoverage and XCoverage<2000):
				XCoverage = x[0] + 300
				YCoverage = x[1] + 300
				apList.append(x)

		for i in range(len(finalPoints)):
			x=list(finalPoints[i])
			if(x[1]-300 <= YCoverage and x[1] > YCoverage  and x not in apList and YCoverage<2000):
				YCoverage = YCoverage+300
				apList.append(x)


	print("################################")
	text_file = open("heurestic_three.txt", "a")
	text_file.write("\n Length %s" % len(apList))
	text_file.close()

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        # Get lock to synchronize threads
        if(self.threadID == 1):
#        	for i in range(1,100):
       		print(i)
        	heurestic_ONE()
        if self.threadID == 2:
#        	for i in range(1,100):
	        heurestic_TWO()
#        if self.threadID == 3:
#        	for i in range(1,100):
	        heurestic_THREE()
        # Free lock to release next thread


thread1 = myThread(1)
thread2 = myThread(2)
thread3 = myThread(3)

thread1.start()
thread2.start()
thread3.start()


print("############### HEURESTIC ONE  #################")
heurestic_ONE()

print("############### HEURESTIC TWO  #################")

heurestic_TWO()

print("############### HEURESTIC THREE  #################")

heurestic_THREE()

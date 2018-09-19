"""
Closest pair problem - The closest pair of points problem or closest pair problem
is a problem of computational geometry: given n points in metric space,
find a pair of points with the 
smallest distance between them.
"""
import math

p1=(1,1)
p2=(0,0)


# Returns the distance of two points in R^2
def getDistance(p1,p2):
	return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**.5



# I will try a brute force method first, and see if I can come up with something better

pointList=[(0,0),(5,5),(100,100),(4,4),(10,10),(100.5,100.5)]


def closestPair(pointList):
	min = (pointList[0],pointList[1])
	mindistance = getDistance(pointList[0],pointList[1])

	for i in range(0,len(pointList)):
		for j in range(0,len(pointList)):
			print(i)
			print(j)
			if (i==j):
				print("ding")
				break
			if (getDistance(pointList[i],pointList[j]) < mindistance):
				min = (pointList[i],pointList[j])
				print(min)
				mindistance = getDistance(pointList[i],pointList[j])

	return min

print(closestPair(pointList))




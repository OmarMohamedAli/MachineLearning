# Example of kNN implemented from Scratch in Python

import math
import operator


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
#		print(distances)
	distances.sort(key=operator.itemgetter(1))
#	print(distances)
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


trainingset=[[2,2,2,'a'],[4,4,4,'b']]
testinstance=[5,5,5]
k=1
neighbors=getNeighbors(trainingset, testinstance, k)
print(neighbors)

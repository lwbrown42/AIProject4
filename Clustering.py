import sys
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial import distance

MAX_ITERATIONS = 100

#def kmeans(pointArray, numClusters):
def kmeans(xArray, yArray, numClusters):
    centroids = []
    oldCentroids = []
    iterations = 0

    #choose random centroids
    for i in range(numClusters):
        newCentroidNum = random.randint(0, len(xArray)-1)
    
        newCentroid = [xArray[newCentroidNum], yArray[newCentroidNum]]
        centroids.append(newCentroid)

    print(centroids)

    # keep going til we found the thing or went too long
    while oldCentroids != centroids and iterations < MAX_ITERATIONS:
    
        iterations += 1
        clusterGroup = []
        newCentroids = []
        spotCount = []
        for i in range(numClusters):
            newCentroids.append([0,0])
            spotCount.append(0)

        #find the shortest distance for each point
        for i in range(len(xArray)):
            cluster = findShortest(xArray[i], yArray[i], centroids, numClusters)
            clusterGroup.append(cluster)

#        print(clusterGroup, end = "")
#        print(len(clusterGroup))
#        print(xArray, end = "")
#        print(len(xArray))
#        print(yArray, end="")
#        print(len(yArray))

        #reassign clusters
        for i in range(len(xArray)):
            clusterSpot = clusterGroup[i]
            newCentroids[clusterSpot][0] += xArray[i]
            newCentroids[clusterSpot][1] += yArray[i]
            spotCount[clusterSpot] += 1

        #average the thing
        for i in range(numClusters):
            if spotCount != 0:
                newCentroids[i][0] = newCentroids[i][0]/spotCount[i]
                newCentroids[i][1] = newCentroids[i][1]/spotCount[i]

        oldCentroids = centroids
        centroids = newCentroids
            
        print(newCentroids)
            
    return centroids
        
def findShortest(x, y, centroids, numClusters):
    
    currentX = x
    currentY = y
    
    best = []
    bestDistance = 1000000000000

    #find the smallest one?
    for j in range(len(centroids)):
        if currentX != centroids[j][0] and currentY != centroids[j][1]:
            distance = getDistance(currentX, currentY, centroids[j])
            
            if distance < bestDistance:
                bestDistance = distance
                best = centroids[j]
            
    return centroids.index(best)
                
                    
def getDistance(x, y, centroid):

    a = (x,y)
    b = (centroid[0], centroid[1])
    return distance.euclidean(a,b)

def main(argv):

#    pointArray = []
    xArray = []
    yArray = []
    numClusters = int(argv[1])
    
    if (len(argv) == 3):

        infile = open(argv[2], "r")
        
        for line in infile:
            tempLine = line.split()
        
            #pointArray.append((int(tempLine[0]),int(tempLine[1])))
            
            xArray.append(int(tempLine[0]))
            yArray.append(int(tempLine[1]))

#        kmeans(pointArray,  numClusters)
        finalCentroids = kmeans(xArray, yArray, numClusters)
        
        plt.scatter(xArray, yArray)

        for i in range(len(finalCentroids)):
            plt.plot(finalCentroids[i][0], finalCentroids[i][1], '^')

        plt.show()

    else:
        print("Not enough command line arguments.")

main(sys.argv)

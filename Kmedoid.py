#Kmedoid Program Complete



import wradlib as wrl
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances as pdist

file_path = "C:\\Users\\manan\\OneDrive\\Desktop\\data\\BHP190610110229.MAXSU60"
fcontent = wrl.io.read_iris(file_path)
print(fcontent['data'][0][0])
data = fcontent['data'][0][0]

points = []
k=3

for indx,x in enumerate(data[200:]):
    for indy,y in enumerate(x[:520]):
        if y!=95.5 and y!=-32:
            points.append(list([indx,indy]))

def plotpoints(data,labels,centroids,k,r=1):
    color = ['red','blue','green','yellow','black','purple','grey']
    plt.figure(figsize = (10,10))
    for i in range(k):
        x = data[labels==i][:,0]
        y = data[labels==i][:,1]
        plt.scatter(x,y,s=1,c=color[i])

    for i in centroids:
        plt.scatter(i[0],i[1],s=5*r,c='orange')
    
    plt.show()

data = np.array(points)

np.random.seed(0)

previous_centroids = data[np.random.choice(len(data), k, replace=False)]
current_seeds = []
labels = []

def cost_function(cluster, data, labels):
    index = np.argmin(np.sum(pdist(data[labels==cluster], metric='euclidean'), axis=1))
    points = data[labels==cluster]
    return points[index]

while True:
    labels = np.array([np.argmin(np.sqrt(np.sum((previous_centroids - data[i])**2, axis=1))) for i in range(len(data))])
    plotpoints(data,labels,previous_centroids,k)
    print(previous_centroids)
    current_centroids = np.array([cost_function(j,data,labels) for j in range(k)])
    '''
    for ind,centroid in enumerate(current_centroids):
        for i,val in enumerate(centroid):
            current_centroids[ind][i] = int(val)
    '''
    if np.all(previous_centroids == current_centroids):
        print('Final')
        print(current_centroids)
        plotpoints(data,labels,previous_centroids,k,3)
        break;
    previous_centroids = current_centroids

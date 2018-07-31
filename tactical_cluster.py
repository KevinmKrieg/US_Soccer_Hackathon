import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster as skCluster
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as RandomizedPCA
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans
from scipy.spatial.distance import cdist,pdist
from matplotlib import cm
from sklearn.cluster import KMeans
import numpy as np
from scipy.cluster.vq import kmeans
from scipy.spatial.distance import cdist,pdist
from sklearn import datasets
from sklearn.decomposition import RandomizedPCA
from matplotlib import pyplot as plt
from matplotlib import cm

def normData(X):
    X_norm = (X - X.min())/(X.max() - X.min())
    return X_norm
def pca(X_norm):
    pca = RandomizedPCA(n_components=3).fit(X_norm) #3-dimensional PCA
    transformed = pca.transform(X_norm)
    return transformed
def clusterTest(Y,number):
    ##### cluster data into K=1..number clusters #####
    from sklearn.cluster import KMeans
    Ks = range(1, number)
    km = [KMeans(n_clusters=i) for i in Ks]
    score = [(km[i].fit(Y).score(Y)) for i in range(len(km))]

    fig = plt.figure()
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    plt.grid(True)
    plt.plot(Ks, score,'b*-')
    plt.xlabel('Number of clusters')
    plt.ylabel('Percentage of variance explained (%)')
    plt.title('Sessions: Elbow for KMeans clustering')
    plt.xticks()
    plt.show()
    return score


def clusters(Y, number, s):
    KM = KMeans(n_clusters=number).fit(Y)
    for i in range(0, Y.shape[0]):
        if KM.labels_[i] == 0:
            c1 = plt.scatter(Y[i,0],Y[i,1],c='r',marker='+')
        elif KM.labels_[i] == 1:
            c2 = plt.scatter(Y[i,0],Y[i,1],c='g', marker='o')
        elif KM.labels_[i] == 2:
            c3 = plt.scatter(Y[i,0],Y[i,1],c='b', marker='*')
        elif KM.labels_[i] == 3:
            c4 = plt.scatter(Y[i,0],Y[i,1],c='y', marker='^')
        elif KM.labels_[i] == 4:
            c5 = plt.scatter(Y[i,0],Y[i,1],c='c', marker='<')
    plt.savefig(str(s) +'.tiff')
    plt.show()
    h = pd.DataFrame(KM.labels_,columns=['label']) 
    return h,KM.labels_

import urllib.request
df = pd.read_csv('Hackathon Files\Hackathon Raw Files\FIFA 18 Ratings.csv')

tactical = ['Crossing', 'Short Passing', 'Dribbling','Long Passing',
        'Interceptions', 'Marking', 'Weak Foot Rating', 'Skill Moves',
        'Vision']
for i in tactical:
    df[i] = pd.to_numeric(df[i], errors='coerce')
tactical = ['Name','Crossing', 'Short Passing', 'Dribbling','Long Passing',
        'Interceptions', 'Marking', 'Weak Foot Rating', 'Skill Moves',
        'Vision']
tacticalDf = df[tactical].dropna()
normTacticalDf = normData(tacticalDf[tactical[1:]])
pcaTacticalDf = pca(normTacticalDf)
clusterTest(pcaTacticalDf, 30)
h, labels = clusters(pcaTacticalDf, 5,'TacticalClusterPlot')
tacticalDf['Cluster'] = labels

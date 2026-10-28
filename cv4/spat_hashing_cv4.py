from math import *
from time import *
from matplotlib.pyplot import *
from numpy import * 
from collections import defaultdict
from sklearn.neighbors import KDTree
import datetime
from numpy.linalg import *



def loadPoints(file):
    #Load file
    X, Y, Z = [], [], [] ;
    
    with open(file) as f:
        
        for line in f:
            x, y, z = line.split('\t')
            
            X.append(float(x))
            Y.append(float(y))
            Z.append(float(z))
    
    return X, Y, Z


def getNN(xq, yq, zq, X, Y, Z):
    #Find nearest point and its distance
    dmin = inf
    xn, yn, zn = X[0], Y[0], Z[0]
    
    for i in range(len(X)):
        #Compute distance
        dx, dy, dz = xq - X[i], yq - Y[i], zq - Z[i]
        d = (dx*dx + dy*dy + dz * dz)**0.5
        
        #Actualize minimum: distance + coordinates
        if d < dmin and d > 0:
            dmin = d
            xn, yn, zn = X[i], Y[i], Z[i]
    return xn, yn, zn, dmin


def drawPoints(X, Y, Z, bx, transp = 0.2):
    # Create figure
    fig = figure()
    ax = axes(projection = '3d')
    ax.set_aspect('equal')

    #Compute sphere scale: 1 pix = 25.4 mm
    scale = 1
    if bx > 0:
        scale = int(bx * bx * 40 * 40)
        
    #Plot points
    ax.scatter(X, Y, Z, s=scale, alpha = transp)

    show()

    
def drawVoxels(x_min, y_min, z_min, dx, dy, dz, V):
    # Create figure
    fig = figure()
    ax = axes(projection = '3d')
    ax.set_aspect('equal') 
    
    #Create meshgrid
    xedges = linspace(x_min, x_min + dx, n_r+1)
    yedges = linspace(y_min, y_min + dy, n_r+1)
    zedges = linspace(z_min, z_min + dz, n_r+1)
    
    VX, VY, VZ = meshgrid(xedges, yedges, zedges,  indexing="ij") 
    
    #Draw voxels
    ax.voxels(VX, VY, VZ, V, edgecolor='k')
    
    show()
    

#Load points
#X, Y, Z = loadPoints('s:/K155/Public/155YGEI/cv12/tree_18.txt')
X, Y, Z = loadPoints('tree_18.txt')

#Draw points
drawPoints(X, Y, Z, 0, 0.2)



class KDNode:

    def __init__(self, point=None, axis=None, left=None, right=None, point_indices=None):
    
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right
        self.point_indices = point_indices
        
        
class KDTree:

    def __init__(self, data):
        
        self.data = array(data)  # Ensure data is a NumPy array
        self.root = None
        
    def _build_tree(self, idxs, depth):
        pass

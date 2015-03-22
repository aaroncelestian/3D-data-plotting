#import glob
#import os  # presumable I can use this to enable me to run this from any dir
import pandas as pd
import numpy as np
#from pylab import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.cm as cm
#from mpl_toolkits.mplot3d import Axes3D


### Import the saved pickled pandas

X = pd.read_pickle('X.pkl')
Y = pd.read_pickle('Y.pkl')
#Z = pd.read_pickle('Z.pkl')


numFiles = len(Y.columns)
Z = pd.DataFrame(range(0,(numFiles),1))

XX = X
YY = Y
ZZ = Z


X, Z = np.meshgrid(X, Z)

Y = Y.T

#################################
### Start plotting figures ######
#################################

fig = plt.figure()


ax = fig.add_subplot(1,1,1, projection='3d')
ax1 = fig.add_subplot(1,1,1, projection='3d')


for i in Z:
    
    ax1.plot(XX, YY[i], ZZ.index[i], c='k', linewidth=0.08) 

## chart labels
ax1.set_title('Y into Zorite')    
ax1.set_xlabel('Raman Shift')
ax1.set_ylabel('Intensity')
ax1.set_zlabel('File Number')

#
ax1.view_init(azim=-90, elev=120)    


minZ = 0
maxZ =75


colormap = 'hot'   #good options are: jet, bone, coolwarm, hot
#ax2 = CS.add_subplot(111)#, projection='3d')

n_levels = 100
ax=plt.contourf(X, Z, Y, n_levels, cmap=colormap, vmin=minZ, vmax=maxZ)


plt.title('Raman Analysis')
plt.xlabel('Raman Shift')
plt.ylabel('Spectrum Number')
plt.xlim(100,1000)
#plt.ylim(0,20)


plt.show()
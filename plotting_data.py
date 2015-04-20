#import glob
#import os  # presumable I can use this to enable me to run this from any dir
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

### version 0.0.3

### Import the saved pickled pandas

X = pd.read_pickle('X.pkl')
Y = pd.read_pickle('Y.pkl')
#Z = pd.read_pickle('Z.pkl')


numFiles = len(Y.columns)
Z = pd.DataFrame(range(0,(numFiles),1))

# these store the orignal data in a serpeate var, just in case I need it later
XX = X
YY = Y
ZZ = Z


X, Z = np.meshgrid(X, Z)

Y = Y.T

#################################
### Start plotting figures ######
#################################


fig = plt.figure()

# Edit the values below to make the plot how you like it
maxYvalue = 20 + max(Y.index.values)
minZ = 0
maxZ = 60
contour_levels = 150         # higher values = better resolution
surface_rstride = 100         # lower values = better resolution
surface_cstride = 100         # lower values = better resolution
colormap = 'jet'             #good options are: jet, bone, gnuplot2, afmhot, add _r to reverse colors
Xlimit = (50, 1800)
Ylimit = (0, maxYvalue)

################################################
################################################

## Contour plot only (the best IMHO)
#
ax2 = plt.figure()
ax2 = fig.add_subplot(111)#, projection='3d')
ax2=plt.contourf(X, Z, Y, contour_levels, cmap=colormap, vmin=minZ, vmax=maxZ)
#
plt.title('Raman Analysis')
plt.xlabel('Raman Shift')
plt.ylabel('Spectrum Number')
plt.colorbar(orientation='vertical', shrink=0.8)
#plt.xlim(100,1000)
#plt.ylim(0,20)


################################################
################################################


## Surface and contour plot  ONLY USE FOR SMALL DATA SETS
# uncomment below to use it 


#ax1 = fig.add_subplot(111, projection='3d')
#ax1.plot_surface(X, Z, Y, rstride=surface_rstride, cstride=surface_cstride, cmap=colormap, alpha=1, linewidth=0.0)#//
#
#ax1.view_init(azim=-90, elev=35)  
#ax1.set_title('Y into Zorite')    
#ax1.set_xlabel('Raman Shift')
#ax1.set_ylabel('File Number')
#ax1.set_zlabel('Intensity')
##ax1.set_ylim(Ylimit) 
##ax1.contour(X, Z, Y, zdir='x', offset=3, cmap=cm.hsv)#// Choose any of these three
##ax1.contour(X, Z, Y, zdir='y', offset=3, cmap=cm.prism)#//
#ax1.contourf(X, Z, Y, contour_levels, zdir='z', offset=maxYvalue, cmap=colormap, alpha=.4, vmin=minZ, vmax=maxZ)#//
#

################################################
################################################

## 3D line line plot
## uncomment below to use it


#ax3 = fig.add_subplot(111, projection='3d')
#
#for i in ZZ.index:    
#    ax3.plot(XX, YY[i], i, c='k', linewidth=0.08) 
#
#### chart labels
##ax3.set_title('Y into Zorite')    
#ax3.set_xlabel('Raman Shift')
#ax3.set_ylabel('Intensity')
#ax3.set_zlabel('File Number')
#
##ax.set_xlim(200,400)
#
#ax3.view_init(azim=-90, elev=120)  


  
plt.show()  #you always need this to show the plot each time you run
#fig.show()

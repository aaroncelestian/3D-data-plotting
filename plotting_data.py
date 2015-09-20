#import glob
#import os  # presumable I can use this to enable me to run this from any dir
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

### version 09.20.2015
### pandas version tested under 0.15.2

### Import the saved pickled pandas

X = pd.read_pickle('X.pkl')
Y = pd.read_pickle('Y.pkl')
#Z = pd.read_pickle('Z.pkl')


numFiles = len(Y.columns)
Z = pd.DataFrame(range(0,(numFiles),1))

# these store the orignal data in a serpeate var, just in case I need it later
# I will us these variables below to change the data range becuase line plots look poor when zoomed in

linePlotStart = 100
linePlotStop = 700
XX = X[linePlotStart:linePlotStop]
YY = Y[linePlotStart:linePlotStop]
ZZ = Z




X, Z = np.meshgrid(X, Z)

Y = Y.T

#################################
### Start plotting figures ######
#################################


fig = plt.figure()


minZ = 0
maxZ =200
maxYvalue = 20 + max(Y.index.values)
contour_levels = 200          # higher values = better resolution
surface_rstride = 25         # lower values = better resolution
surface_cstride = 25        # lower values = better resolution
colormap = 'jet'             #good options are: jet, bone, coolwarm, hot
Xlimit = (50, 1800)
Ylimit = (0, maxYvalue)

################################################
################################################

## Contour plot only
#
#plt.figure()
#fig.add_subplot(211)#, projection='3d')
#plt.contourf(X, Z, Y, contour_levels, cmap=colormap, vmin=minZ, vmax=maxZ)
#
#plt.title('Raman Analysis')
##plt.xlabel('Raman Shift')
#plt.ylabel('Spectrum Number')
#plt.xlim(100,500)
#plt.ylim(0,60)
#
#fig.add_subplot(212)#, projection='3d')
#plt.contourf(X, Z, Y, contour_levels, cmap=colormap, vmin=minZ, vmax=maxZ)
#
##plt.title('Raman Analysis')
#plt.xlabel('Raman Shift')
#plt.ylabel('Spectrum Number')
#plt.xlim(500,1000)
#plt.ylim(0,60)


################################################
################################################


# Surface and contour plot

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


################################################
################################################

#3D line line plot
## Modify XX and YY above to change the "Zoom" properties of this graph

ax3 = fig.add_subplot(111, projection='3d')

for i in ZZ.index:    
    ax3.plot(XX, YY[i], -i, c='k', linewidth=0.08) 

### chart labels
#ax3.set_title('title here')    
ax3.set_xlabel('Raman Shift')
ax3.set_ylabel('Intensity')
ax3.set_zlabel('File Number')


ax3.view_init(azim=-90, elev=110)  
  
#plt.show()
fig.show()

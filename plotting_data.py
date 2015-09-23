#import glob
#import os  # presumable I can use this to enable me to run this from any dir
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *


### version 09.23.2015




### Import the saved pickled pandas

X = pd.read_pickle('X.pkl')
Y = pd.read_pickle('Y.pkl')
#Z = pd.read_pickle('Z.pkl')


numFiles = len(Y.columns)
Z = pd.DataFrame(range(0,(numFiles),1))

# these store the orignal data in a serpeate var, just in case I need it later
#XX = X
#YY = Y
#ZZ = Z


X, Z = np.meshgrid(X, Z)

Y = Y.T

#################################
### Start plotting figures ######
#################################


fig = plt.figure()

maxYvalue = max(Y.index.values)
minIntensity = -10  #min intensity value
maxIntensity = 63.7071 #max intensity value
contour_levels = 150         # higher values = better resolution
surface_rstride = 10         # lower values = better resolution
surface_cstride = 10         # lower values = better resolution
colormap = 'jet'             #good options are: jet, bone, gnuplot2, afmhot, add _r to reverse colors
Xlimit = (55, 1500)      #stand and stop values for wavenumbers, or 2-theta
Ylimit = (0, maxYvalue) #start and stop of spectral range plotting.  Use maxYvalue to plot the last frame

# to normalize the intensities ...
# first, find max intesity value for each spectrum

#maxYlist = [] #makes an empty list to append data
#for i in Y:
#    maxYlist.append(max(Y[i].values)

################################################
################################################

## Contour plot only
#
#ax = plt.figure()
ax = fig.add_subplot(111)# , projection='3d'
#fig, ax = plt.subplots()
ax=plt.contourf(X, Z, Y, contour_levels, cmap=colormap, vmin=minIntensity, vmax=maxIntensity) 
#
plt.title('plot title')    # put the title of your data in here
plt.xlabel('x axis title')
plt.ylabel('y axis title')
plt.colorbar(orientation='vertical', shrink=0.8)   ## comment this out if you don't want a color bar
plt.xlim(Xlimit)  #wavenumber/2-theta display range
plt.ylim(Ylimit)  #spectral range to plot




################################################
################################################


### Surface and contour plot  ONLY USE FOR SMALL DATA SETS, or make this a line-plot with a filled contour plot...

#ax1 = fig.add_subplot(111, projection='3d')
#ax1.plot_surface(X, Z, Y, rstride=surface_rstride, cstride=surface_cstride, cmap=colormap, alpha=1, linewidth=0.0)#//
#
#ax1.view_init(azim=-90, elev=35)  
#ax1.set_title('title')    
#ax1.set_xlabel('x axis title')
#ax1.set_ylabel('y axis title')
#ax1.set_zlabel('z axis title')
##ax1.set_ylim(Ylimit) 
##ax1.contour(X, Z, Y, zdir='x', offset=3, cmap=cm.hsv)#// Choose any of these three
##ax1.contour(X, Z, Y, zdir='y', offset=3, cmap=cm.prism)#//
#ax1.contourf(X, Z, Y, contour_levels, zdir='z', offset=maxYvalue, cmap=colormap, alpha=.4, vmin=minZ, vmax=maxZ)#//
#

################################################
################################################

## 3D line line plot, this work 'ok'
#
#ax3 = fig.add_subplot(111, projection='3d')
#
#for i in ZZ.index:    
#    ax3.plot(XX, YY[i], i, c='k', linewidth=0.08) 
#
#### chart labels
##ax3.set_title('graph title')    
#ax3.set_xlabel('x axis title')
#ax3.set_ylabel('y axis title')
#ax3.set_zlabel('z axis title')
#
##ax.set_xlim(200,400)
#
#ax3.view_init(azim=-90, elev=120)  


  
plt.show()

# now I'm trying to work on converting this matplotlib plot into plotly....

#mpl_fig1 = plt.gcf()
#py_fig1 = tls.mpl_to_plotly(mpl_fig1, verbose=True)

#fig.show()

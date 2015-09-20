import glob
#import os  # presumable I can use this to enable me to run this from any dir
import pandas as pd
import numpy as np
#from pylab import *
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

## Version 09.20.2015



filelist = pd.read_csv('your_data_path_here.CSV')  #imports a CSV file into pandas, I need a non-empty pandas to append things to
##### how to I read just any file?  It shouldn't matter which file since they all have the same X values
##### it would be nice to just run this code and then select a file....
##### and also set the working directory???


df1_x_name = filelist.columns.values[0]  #finds the column header for the [0]
df1_y_name = filelist.columns.values[1]  #finds the colunm header for the [1]

filelist=filelist.rename(columns={df1_x_name:'X'}) # renames [0] to 'X'
filelist=filelist.rename(columns={df1_y_name:'Y'}) # renames [1] to 'Y'

filelist = filelist.drop('Y', 1)  # now we delete the y column because we are going to read again below
                                  # I can probably just do this set above, but it shows what I'm trying to do  
Xfilelist = filelist.drop('X', 1)


###
### ok, now I start building a large pandas with all the data in it.  
### Each new column will be the Y column of each imported csv data file
###

for counter, files in enumerate(glob.glob("*.CSV")):  #finds all CSV files in the current working folder
    
    newfile = pd.read_csv(files)          # Read a CSV file, presumable the first in alpha/numerical order
    #print newfile
    #print counter
    numFiles = counter                      # total number files itterated, scaler
    df1_y_name = newfile.columns.values[1]  # finds column header name for [1]
    df1_x_name = newfile.columns.values[0]
    
    newfile=newfile.rename(columns={df1_y_name:counter})  # renames column header to current counter #
    #newfile=newfile.rename(columns={df1_x_name:counter})
    
    filelist = filelist.join(newfile[counter], how='right', rsuffix='a') # joins 'counter #' column to the main pandas list
    Xfilelist = Xfilelist.join(filelist[counter], how='right', rsuffix='x')  # here I want to make a pandas for the X values
                                                                        #with the same number of columns as the Y values.  why?  I don't know yet
    
    
#filelist.to_csv('./other_files/AllData.CSV')  # uncomment to save the filelist csv file
                                               # pandas saved below



X = filelist['X'].values  # the X values are the values in Raman Shift in cm-1
X = pd.DataFrame(X)   #convert it to a pandas


Y = filelist[0::]            # Y is already a panda, y values are the intensity data for each data file
Y = Y.drop('X', 1)           # now I delete the 'X' because those values are in the xx varible

#Z = range(0,(numFiles),1)    #makes a list of from 0 to numFiles as a z scaler, need this to itterate over
#Z = pd.Series(Z)             #convert it to a pandas

X.to_pickle('X.pkl')
Y.to_pickle('Y.pkl')
#Z.to_pickle('Z.pkl')

# what are the minimun and maximum intensities in the files?, need some code here...

    

print ""
print "SUCCESS: You have pickled the pandas."
print "Number of file imported ", len(Y.columns)
print "Data X range is from      ", min(X.values) ,"to ", max(X.values)


### plotting has been moved to another py file

import glob
import os  
import pandas as pd
import numpy as np
import wx


### version 11/10/2015

def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


abspath = os.path.abspath(get_path('*.csv')) #prompts user to go find the file
dname = os.path.dirname(abspath) # gets the directory of that file
os.chdir(dname) # changes working directory to where the file was grabbed from

print ""
print os.getcwd()
print abspath
print ""

filelist = pd.read_csv(abspath)






df1_x_name = filelist.columns.values[0]  #finds the column header for the [0]
df1_y_name = filelist.columns.values[1]  #finds the colunm header for the [1]

filelist=filelist.rename(columns={df1_x_name:'X'}) # renames [0] to 'X'
filelist=filelist.rename(columns={df1_y_name:'Y'}) # renames [1] to 'Y'

filelist = filelist.drop('Y', 1)  # now we delete the y column because we are going to read again below
                                  # I can probably just do this set above, but it shows what I'm trying to do  
Xfilelist = filelist.drop('X', 1)


##
### ok, now I start building a large pandas with all the data in it.  
### Each new column will be the Y column of each imported csv data file
###

numFiles = 0 # reset the counter for the number of files processed (numFiles)
for counter, files in enumerate(glob.glob("*.CSV")):  #finds all CSV files in the current working folder
    
    newfile = pd.read_csv(files)          # Read a CSV file, presumable the first in alpha/numerical order
    #print newfile
    #print counter
    numFiles = counter                      # total number files itterated, scaler
    df1_y_name = newfile.columns.values[1]  # finds column header name for [1]
    df1_x_name = newfile.columns.values[0]
    #if 
    
    newfile=newfile.rename(columns={df1_y_name:counter})  # renames column header to current counter #
    #newfile=newfile.rename(columns={df1_x_name:counter})
    
    filelist = filelist.join(newfile[counter], how='right', rsuffix='a') # joins 'counter #' column to the main pandas list
    #Xfilelist = Xfilelist.join(filelist[counter], how='right', rsuffix='x')  # here I want to make a pandas for the X values
                                                                        #with the same number of columns as the Y values.  why?  I don't know yet
    
    
#filelist.to_csv('./other_files/AllData.CSV')  # uncomment to save the filelist csv file
                                               # pandas saved below



X = filelist['X'].values  # the X values are the values in Raman Shift in cm-1
X = pd.DataFrame(X)   #convert it to a pandas


Y = filelist[0::]            # Y is already a panda, y values are the intensity data for each data file
Y = Y.drop('X', 1)           # now I delete the 'X' because those values are in the xx varible


def stringCheck(df):
    # Check to see if there are missing values if the dataframe... 
    #'#NaN' is used with the Thermo DXR raman microscope
    HowManyOjects = 0
    for col in df:
        if df[col].dtypes == object:
            HowManyOjects = HowManyOjects + 1
            #print HowManyOjects
            
        elif df[col].dtypes != object:
            HowManyOjects = HowManyOjects + 0

            
    # now we figure out if there are any strings, aka objects        
    if HowManyOjects > 0:
        return True
    else:
        return False
            
    
        

if stringCheck(Y) == True:
    print ""
    print "Warning, there are strings in your data."
    print "This is likely because of some missing values during the original saving process on your instrument."
    print "I will try to correct this, but you should check your Y.pkl file to be sure."
    print ""
    # If there are NaN or #NaN entries, then this will fix it
    # If I decide to use this with more than one type of data, I should make a python list of things to replace
    Y2 = Y.replace('#NaN',0)
    Y2.to_pickle('Y.pkl') 
else:
    print ""
    print "The data looks good.  No missing values are seen."
    print ""
    Y.to_pickle('Y.pkl')
    


X.to_pickle('X.pkl')
#Z.to_pickle('Z.pkl')   #This isn't needed here, I make a new instance of Z when plotting data

maxYlist = []
for i in Y.columns:
    maxYlist.append(max(Y[i].values))

# check to see if the user input the correct file-extension format.  

if max(Y[:].columns) < 1:
    print "Something went wrong. Not all the data was written successfully."
    print "You should check the case-sensitive file extensions of your files."
    print "Change the *.CSV to *.csv in the code (or vis-versa), or
    print "change the filename extensions to have a *.CSV or *.csv extension"
else:    
    print ""
    print "SUCCESS: X.pkl and Y.pkl created in the working directory."
    print "Number of files proccessed: ", numFiles+1 #max(Y.index.values)
    print "Data range X axis:          ", min(X.values), " to", max(X.values)
    print "Max intensity:              ", max(maxYlist)
    print ""
    


### plotting has been moved to another py file...  plotting_data.py

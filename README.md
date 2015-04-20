# 3D-plotting-Raman-XRD-series
take times series data, e.g. Raman or XRD, and plots in 3D and contour.
It's a mostly automated way of grabbing data and formatting it into a way python can plot it.  It definitely beats excel!

In the future, I'll be working on...(and need help with)
1. Doing some basic statistics 
2. Calculating rates, or at least finding the positions when changes the patterns happen
3. Finding a faster way to plot surfaces
4. Integrating the results from XRD data and Raman data from identical experiments, that is, as an example: comparing difference curves and rate change curves for the exact same experiment.  There are other reasons as well...


If at any point you need help, just ask :)  I can supply some data if you need it.


## Data format
1. All data needs to be in a CSV format.

2. The format of the CSV should be X,Y pairs (e.g. 2-theta vs. intensity, or Raman Shift (cm^-1) vs. intensity

3. Also, make sure that the X values don't change from file, to file, to file.  That is, all the X-value measurements should be exactly the same in all files.  This is usually the case if you do a single experiment where all the data is collected using the same conditions.  The reason why you need to have all the X values the same is because this code only grabs the X-values from the first file that's imported.  If the X-values change from file to file, then your data just won't look right.  I can probably add a bit of code to output if your data matches the correct X-value format or not. 

4. Also, make sure that the filenames are in a good format.  You don't want filenames like, 1.csv, 2.csv, ... 20.csv, etc.  That's because when you run this script, some of the files will be out of order.  You should rename the files to be something XRD_Data_Run_01_00001.csv -- where the 00001 part in the incremented number.  How you do that will depend on your system, but it's something to keep in mind when you're writing the files from the experiment to begin with.

## Grab all your data and put them into Pandas
1. First, edit the Import_CSV_files_into_pandas.py  You'll have to manually type in the first input file name in the python code.  The comments in the code will tell you where to do this.

2. Second, run the Import_CSV_files_into_pandas.py from the directory where your data is located.  In the Canopy IDE (which is what I use, this is pretty easy.  From the Python working window, just click on the "change working directory ..." and select the directory that has all the data.

3. Run it, and if successful you see a "sucess" in the text.  If it's not successful you'll get a bunch of errors.

## Now plot all the data

I put the defualt plotting as a filled contour, but you can use the other ones (by uncommenting them) or add others as you like.

1. While still in the working directory above, you'll now have a few more files called X.pkl, Y.pkl, Z.pkl (the pickled pandas). No need to edit these, but you may want to make backup copies.

2. There are three options on how to plot the data here: 1) 3D line plot, 2) filled contour plot, 3) surface plot + filled contour plot.  NOTE: if you have a lot of data (e.g. 200 diffraction files with 2000+ lines each), then the 3D line plot and the surface plots are going to bog your system.  I wish I knew of a way to make it faster, but I don't.

3. Anyway, The contour plot is the best in my mind.  The 3D plots are hard to get view angle right without distortion, and for scientific purposes, you want to know if the peaks in the XRD or Raman move to the left or right anyway.  The best way to see peak movment is with a contour plot.  Luckily, the contour plots are much faster to render.

4. You'll need to edit some parameters manually to make the figures look to your specifications.  I put all the figure editing properties together in one area to make this simpler (I think it does...)  see the "Start Figure Plotting" section in the code for the things you can easily change.


end.

 


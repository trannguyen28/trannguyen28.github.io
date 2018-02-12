# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
  
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') 
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none') 
ax[4].imshow(img, interpolation='none')
ax[0].plot(45, 35, 'ro')
ax[0].set_xlim(35, 100)
ax[0].set_ylim(40, 5)
ax[1].set_xlim(35, 80)
ax[1].set_ylim(70, 50)
ax[2].set_xlim(35, 45)
ax[2].set_ylim(60, 30)
ax[3].set_xlim(65, 100)
ax[3].set_ylim(70, 50)
ax[4].set_xlim(35, 100)
ax[4].set_ylim(20, 5)
# Show the figure on the screen
fig.show()
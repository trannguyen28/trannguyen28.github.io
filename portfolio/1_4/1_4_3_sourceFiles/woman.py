'''
JDoe_JSmith_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

###
# Change a region if condition is True
###
  
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] 
for r in range(415, 468):
    for c in range(132, 165):
        if sum(img[r][c])>370: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,255,255] 
for r in range(790, 820):
    for c in range(250, 280):
        if sum(img[r][c])>200: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,255,0] 
for r in range(457, 494):
    for c in range(231, 354):
        if sum(img[r][c])>450: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,255,0] 
for r in range(300, 400):
    for c in range(140, 460):
        if sum(img[r][c])<250: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,0] 
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen

fig.show()
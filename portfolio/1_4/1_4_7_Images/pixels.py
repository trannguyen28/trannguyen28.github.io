import matplotlib.pyplot as plt
import os.path
import numpy as np
  
   
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'pngs/pink.png')
img = plt.imread(filename)


height = len(img)
width = len(img[0])

print ('width= ',width)
print ('height= ',height)

for row in range(height):
        for col in range(width):
            if (sum(img[row][col]))%5 == 0:
                img[row][col] = [row, col, 125,]
                
for r in range(height):
    for c in range(width):
        if sum(img[r][c])>100: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] 
            
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen

fig.show()
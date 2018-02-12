import matplotlib.pyplot as plt
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    
    for row in range(rows):
        for column in range(columns):
            if (row-column)/stripe_width % 3 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [0,255,column, 100]
            elif (row-column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255,0,row, 100] 
            elif (column+row)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [227, 28, 121, 255]  
              
            else:
                # Odd stripe
                image[row][column] = [0, 49, 60, 255]
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,10)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()            
               
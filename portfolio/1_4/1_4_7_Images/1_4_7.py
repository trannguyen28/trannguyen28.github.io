from PIL import Image, ImageFilter
import os


# convert images to .png
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png') or f.endswith('.gif'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))

##################################

# Resize images
size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png') or f.endswith('.gif'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))

##################################

# Rotate images

#All
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png') or f.endswith('.gif'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.rotate(90).save('mod/{}_90{}'.format(fn, fext))

# Sepatately 
image1 = Image.open('highland.JPG')
image1.rotate(180).save('mod/highland_rotated.JPG')

##################################

# Blurred Images

#All
for f in os.listdir('.'):
    if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png') or f.endswith('.gif'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.filter(ImageFilter.GaussianBlur(15)).save('blur/{}_blur{}'.format(fn, fext))
    
# Sepatately 
image1 = Image.open('vict.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('mod/vict_blurred.jpg')


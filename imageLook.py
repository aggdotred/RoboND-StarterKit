import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#%matplotlib inline

filename = 'sample.jpg'
image = mpimg.imread(filename)
plt.imshow(image)
plt.show()


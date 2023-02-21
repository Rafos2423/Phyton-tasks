import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time

plt.rcParams['figure.figsize'] = (20, 12)
image = io.imread('input.jpg')
labels = plt.axes(xticks=[], yticks=[])
labels.imshow(image)

rows = image.shape[0]
cols = image.shape[1]

image = image.reshape(rows*cols, 3)

start_time = time.time()
repeat_count = 1

for i in range(repeat_count):
  kmeans = KMeans(n_clusters=128)
  kmeans.fit(image)

end_time = time.time()
print((end_time - start_time) / repeat_count)

compressed_image = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = np.clip(compressed_image.astype('uint8'), 0, 255)

compressed_image = compressed_image.reshape(rows, cols, 3)

io.imsave('output.jpg', compressed_image)
io.imshow(compressed_image)
io.show()
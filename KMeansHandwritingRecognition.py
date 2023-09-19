import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
print(digits)
print(digits.DESCR)
print(digits.data)
print(digits.target)

plt.gray() 
plt.matshow(digits.images[100])
plt.show()

print(digits.target[100])

# Figure size (width, height)

fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images

for i in range(64):

    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position

    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value

    ax.text(0, 7, str(digits.target[i]))

plt.show()

model = KMeans(n_clusters=10, random_state=42)

model.fit(digits.data)
fig = plt.figure(figsize=(8, 3))

fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
[0.00,0.00,0.23,2.21,1.68,0.08,0.00,0.00,0.00,0.00,5.26,7.62,7.62,3.51,0.00,0.00,0.00,0.85,7.62,4.42,7.09,6.41,0.38,0.00,0.00,2.14,7.62,1.83,2.29,7.62,2.90,0.00,0.00,2.29,7.62,1.53,0.08,7.09,4.50,0.00,0.00,2.14,7.62,3.43,1.68,7.63,3.59,0.00,0.00,0.08,6.18,7.62,7.63,7.55,1.15,0.00,0.00,0.00,0.30,2.52,3.81,1.38,0.00,0.00],
[0.00,0.15,3.58,4.12,4.57,4.57,4.12,0.23,0.00,0.54,7.40,6.86,6.86,6.25,7.55,4.42,0.00,0.00,0.00,0.00,2.67,5.19,7.47,5.11,0.00,0.00,0.00,2.06,7.62,7.40,4.88,0.76,0.00,0.00,0.00,0.69,5.65,7.62,2.67,0.00,0.00,0.00,0.08,0.76,1.83,7.55,4.58,0.00,0.00,0.00,2.82,7.62,7.62,7.40,2.44,0.00,0.00,0.00,0.46,2.29,2.21,0.84,0.00,0.00],
[0.00,0.00,0.08,2.82,3.81,2.59,0.00,0.00,0.00,0.00,4.19,7.62,7.24,7.63,2.89,0.00,0.00,0.00,6.86,6.25,0.69,7.40,4.27,0.00,0.00,0.00,4.88,7.62,7.24,7.62,5.11,0.00,0.00,0.00,0.08,3.13,3.81,6.33,6.71,0.00,0.00,0.00,0.00,0.00,0.00,3.66,7.62,0.92,0.00,0.00,0.00,0.00,0.00,2.21,7.62,1.83,0.00,0.00,0.00,0.00,0.00,0.69,6.56,1.52],
[0.00,0.23,2.52,2.97,0.61,0.00,0.00,0.00,0.00,4.66,7.62,7.62,6.33,0.08,0.00,0.00,0.00,0.92,1.68,3.13,7.62,2.90,0.00,0.00,0.00,0.00,0.00,0.00,6.79,5.34,0.00,0.00,0.00,0.00,0.00,4.20,7.62,3.59,0.00,0.00,0.00,0.00,3.66,7.62,7.63,6.18,2.90,0.00,0.00,0.00,2.90,5.34,5.26,4.58,1.98,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')


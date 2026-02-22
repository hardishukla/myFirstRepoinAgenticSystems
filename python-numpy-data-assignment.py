"""Your program must:

Set a random seed for reproducibility.


Generate a 2D NumPy array representing a dataset with:

Rows as samples
Columns as features
Compute the mean and standard deviation per feature using axis-aware operations.

Normalize the dataset using broadcasting:

normalized = (data - mean) / std
Slice the normalized array to:

Extract the first 80% of samples as a training set
Extract the remaining samples as a test set
Modify a sliced value intentionally and observe its effect on the original array (to demonstrate view behavior).

Print:

Original data shape
Mean and standard deviation shapes
Training and test set shapes
A brief message explaining what changed due to slicing
Requirements:

Use NumPy vectorized operations only (no Python loops for math)
Use .shape, slicing, broadcasting, and random generation
Use clear variable names and clean structure
Demonstrate understanding of views vs copies
Sample Output (example):

Original data shape: (100, 3)
Mean shape: (3,)
Training data shape: (80, 3)
Test data shape: (20, 3)
Note: Modifying the slice affected the original array"""

import numpy as np
import numpy.random as rand

ran=rand.seed(42)
data=np.zeros([100,3])
shape=np.shape(data) #data.shape()=[100,3]
print("Orignal data shape:",shape)
mean=np.mean(data,axis=0,dtype=float)
print("Mean shape:",np.shape(mean))
train=data[:80]
train_shape=np.shape(train)
test=data[80:]
test_shape=np.shape(test)
print(f"Train data shape: {train_shape}\nTest data shape:",test_shape)
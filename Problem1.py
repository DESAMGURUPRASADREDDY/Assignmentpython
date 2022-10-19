import numpy as np
import random

array = np.array(random.sample(range(1, 20), 15))
print("Np Array: ", array)

reshaped1 = array.reshape((3, 5))
print("Reshaped array Shape: ", reshaped1.shape)
print("Reshaped Array: \n ", reshaped1)

for i in reshaped1:
    max_value = np.max(i)
    index = np.where(i == max_value)
    i[index] = 0

print("Reshaped Max removed: \n ", reshaped1)
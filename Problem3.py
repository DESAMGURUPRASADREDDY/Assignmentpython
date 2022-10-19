import matplotlib.pyplot as plt
import numpy as np

y = np.array([22.2,17.6,8.8,8,7.7,6.7])
labels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
data = [0.1,0.0,0.0,0.0,0.0,0.0]

plt.pie(y,autopct='%1.1f%%', labels = labels, explode = data, shadow = True)
# plt.legend()
plt.show()
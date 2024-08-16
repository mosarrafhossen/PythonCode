import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([5, 2, 4, 9])

#plt.bar(x, y)
plt.bar(x, y, color = 'r')
#plt.pie()

plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("title", loc = "right")
plt.show()
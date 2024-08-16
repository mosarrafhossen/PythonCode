import matplotlib.pyplot as plt
import numpy as np

y = np.array([23, 10, 28, 40])
xxlabel = ("Apple", "Banana", "Blueberry", "Mango")
myexplode =[.2, 0, 0, 0]
mycolor =["Red", "Green", "hotpink", "#CCFF00"]

plt.pie(y, labels=xxlabel, startangle=90, explode=myexplode, shadow=True, colors=mycolor)
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("This is title bar", loc="left")
plt.legend(title="Fruits")

plt.show()
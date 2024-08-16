# import sys
#
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
# matplotlib.use("Agg")
#
# print(matplotlib.__version__)
# print(matplotlib.__version_info__)
#
# xpoint = np.array([0, 6])
# ypoint = np.array([0, 250])
# plt.plot(xpoint, ypoint)
# plt.show()
#
# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, 'k')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 9, 6, 12])
yp = np.array([3, 5, 2, 6, 8])
plt.subplot(2, 1, 1)
plt.plot(ypoints, color = 'hotpink', lw = '5.5')
plt.plot(yp, color = "b")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("title", loc = "right")
plt.grid(axis='y', color= "r", ls = ':', lw = "2.5")
plt.subplot(2, 1, 2)
plt.plot(yp,color= "b", ls = ':', lw = "3.5" )
plt.plot(ypoints, color = 'hotpink', lw = '5.5')
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("title", loc = "right")

plt.suptitle("My Super Title")
#plt.show()
#
#
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#
# plt.scatter(x, y)



plt.show()
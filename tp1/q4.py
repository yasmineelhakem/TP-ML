import matplotlib.pyplot as plt
import numpy as np
x = np.array(["MPI", "RT", "IIA", "IMI"])
y = np.array([16.5, 15.8, 14.9, 13.7])
plt.bar(x,y)
plt.show()

frequencies = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21]
range = (0, 100)
bins = 10
plt.hist(frequencies, bins, range, color = 'green', histtype = 'bar', rwidth =0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Freq_Histogram')
plt.show()
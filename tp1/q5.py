import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["MPI", "RT", "IMI", "IIA"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four classes:", loc=2)
plt.show()
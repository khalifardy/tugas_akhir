import numpy as np
import matplotlib.pyplot as plt

history = np.array([3.461777446924412e-05, 3.468311386891845e-05, 3.4707057185219855e-05, 3.4707057185219855e-05, 3.470847591827118e-05, 3.470847591827118e-05, 3.470908062084392e-05, 3.470908062084392e-05, 3.470908062084392e-05, 3.470908062084392e-05])



plt.plot([i+1 for i in range(len(history)) ],history)
plt.xlabel('generasi')
plt.ylabel('fitness_value')
plt.title(f'KMA n = {5}, iterasi{10}')
plt.show()
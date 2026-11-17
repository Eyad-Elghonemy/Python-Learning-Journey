import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Sample Date
x = np.linspace(0, 10, 100)

# Create Subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].plot(x, np.sin(x), 'r')
axs[0,0].set_title('Sine Wave')

axs[0, 1].plot(x, np.cos(x), 'b')
axs[0,1].set_title('Cosine Wave')

axs[1, 0].plot(x, np.tan(x), 'g')
axs[1,0].set_title('Tangent Wave')

axs[1, 1].plot(x, -np.sin(x), 'm')
axs[1,1].set_title('Negative Sine Wave')

for ax in axs.flat:
    ax.set(xlabel='X Axis', ylabel='Y Axis')
    ax.grid(True)
    
plt.tight_layout()
plt.show()
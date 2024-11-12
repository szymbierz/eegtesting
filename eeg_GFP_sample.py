#%%

import numpy as np
import random

from IPython.core.pylabtools import figsize

"""Time [s]"""
T = 1000
"""Data sampling sampling_rate"""
sampling_rate = 100
"""Samplin_rate gives number of samples per s"""
n_samples = T*sampling_rate
"""Define the N of electrodes = N of iterations"""
N = 32
"""Shape of the matrix is Electodes X n_samples """
np.random.seed(42)
x = np.random.rand(32,100000)
#%%
GFP = np.sum(x**2,axis=0)/x.shape[0]
#%%
import matplotlib.pyplot as plt
time = np.linspace(0,T,n_samples)
fig,ax=plt.subplots(figsize=(15,3))
ax.plot(time,GFP,label='GFP',color='blue')
ax.set_xlabel('Time [s]')
ax.set_ylabel('GFP')
ax.legend()
plt.show()
#%%

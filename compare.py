#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
R = [6.513596e-04, 7.104874e-03, 4.468560e-02, 3.390393e-01, 3.702221e+00, 3.839906e+01, 3.952626e+02]
Julia = [0.000011, 0.000090, 0.000875, 0.008738, 0.090432,  0.874878, 8.756736]
Python = [0.0013747215270996094,
 0.010357141494750977,
 0.08188533782958984,
 0.8130302429199219,
 8.1210355758667,
 91.52449250221252,
 753.7016830444336]
pythonnjit = [0.000, 0.000, 0.000, 0.00826, 0.08840, 0.8845, 8.81435]
X = [10**i  for i in range(4,11)]


R_Julia = [R[i] / Julia[i] for i in range(1,7)]
Python_Julia = [Python[i] / Julia[i] for i in range(1,7)]
Python_R = [Python[i] / R[i] for i in range(1,7)]
Python_Julia_njit = [pythonnjit[i] / Julia[i] for i in range(4,7)]



plt.plot(X, Julia, 'r') # plotting t, a separately 
#plt.plot(X, Python_Julia, 'b') # plotting t, b separately 
#plt.plot(X, Python_R, 'g') # plotting t, c separately 
plt.show()

# %%
X
# %%

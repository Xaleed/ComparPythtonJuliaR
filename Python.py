# %%
def S(n):
    #v = [1/i for i in range(1,n+1)]
    s = 0.0
    for i in range(1, n+1):
        s += 1/i
    return(s)

# %%
%time S(10**8)
#%%
import time
T = []
for i in range(4,11):
    start = time.time()
    S(10**(i))
    end = time.time()
    T.append(end - start)
# %%
T
# %%
2**2
# %%
# %%
# %%
from numba import njit
# %%
from numba import njit
@njit
def S1(n):
    #v = [1/i for i in range(1,n+1)]
    s = 0
    for i in range(1, n+1):
        s += 1/i
    return(s)
S1(2)
T1 = []
for i in range(4,11):
    start = time.time()
    S1(10**(i))
    end = time.time()
    T1.append(end - start)

# %%

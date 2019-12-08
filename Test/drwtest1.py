import numpy as np
from math import factorial
from math import gamma

# for n in range(1,20):
#     print(n-1, n*(np.pi)**(n/2) / gamma(n/2+1))

# for k in range(10):
#     print(2*k, (2*k+1)*2*factorial(k+1)*(4*np.pi)**k / factorial(2*k+1))
#     print(2 * k + 1, (2*k+2)*np.pi ** (k+1) / factorial(k + 1))

# V
# for k in range(10):
#     print(2*k, np.pi ** k / factorial(k))
#     print(2 * k + 1, 2*factorial(k)*(4*np.pi)**k / factorial(2*k+1))


# for n in range(20):
#     print(n, (np.pi)**(n/2) / gamma(n/2+1))

A = np.array([[1,0.3,0],[0.3,1,0.4],[0,0.4,1]])
L = np.linalg.cholesky(A)
print(L)
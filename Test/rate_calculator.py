from sympy.solvers import solve
from sympy import Symbol
from sympy import N
x = Symbol('x', real=True, positive=True)
#sol = solve(x**2 - 1, x)

principle = 400000
n_term = 60
#n_term = 3
expr = -principle
principle_left = principle
for ii in range(n_term):
    interest=900
    ret_principle=6666
    if ii == 0:
        ret_principle=6706
    if ii==n_term-1:
        ret_principle=principle_left
    principle_left -= ret_principle
    expr += (interest+ret_principle)*x**(ii+1)

import numpy as np


for n in range(3, 61):
    coeff=[0 for _ in range(n+2)]
    coeff[0] += 7566+(400000-40-6666*n)
    coeff[1] += -(400000-40-6666*n)
    coeff[-3] += 40
    coeff[-2] += (-7566-40-400000)
    coeff[-1] += 400000
    #print(coeff)
    rate = (1/np.roots(coeff)[-1].real)**12-1
    print("n:{}, rate:{:.2%}".format(n, rate))
#expr = 7566*(x**(n+1)-x)+40*x*(x-1)+(400000-40-6666*n)*(x-1)*x**n-400000*(x-1)
#print(expr)
#sol = solve(expr,quick=True)
#print(N(sol[-1]))

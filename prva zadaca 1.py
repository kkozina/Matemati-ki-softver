
# coding: utf-8

# # KRIVULJE
# 
# __Krivulja__ (parametrizirana krivulja) c u $\mathbb{R}^n$ je glatko preslikavanje s otvorenog intervala $I=<a,b> \subset\mathbb{R}$ u $\mathbb{R}^n$
# \\[\boxed{c:<a,b> \rightarrow\mathbb{R}^n}\\]
# 
# Sada ćemo pokazati neke primjere krivulja, krenimo od najjednostavnijih.
# 
# ### PRAVAC
# 
# Eksplicitna jednadžba pravca dana je s $y=ax + b \ , \ a,b \in\mathbb{R}$, gdje $a$ označava koeficijent smjera, a $b$ odsječak na osi ordinata.
# 

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 7))

x = np.arange(-5, 5)
ax.plot(x, x, 'g', label=r'$y=x$')
ax.plot(x, -x, color='orange', label=r'$y=-x$')
ax.plot(x, x+2, 'r', label=r'$y=x+2$')
ax.plot(x, x-2, 'b', label=r'$y=x-2$')
ax.legend(loc=6)


# Funkcija sjeciste nam daje informaciju sijeku li se zadani pravci. Ukoliko se sijeku daje nam točku sjecišta.

# In[11]:


import numpy as np
from sympy import *
from sympy.abc import x
from sympy import init_printing
init_printing()


def sjeciste(*p):

    for i in range(len(p)):
        for j in range(i+1, len(p)):
            eq = Eq(p[i], p[j])
            r = solve(eq, x)
            if(r == []):
                print("Pravaci {} i {} se ne sijeku!".format(p[i], p[j]))
            else:
                t = p[i].subs(x, r[0])
                print("Pravaci {} i {} se sijeku".format(p[i], p[j]))
                print("u točki ({}, {})".format(r[0], t))
sjeciste(x+2, -x)


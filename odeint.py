#!/usr/bin/env python
# coding: utf-8

# Project: Refer to《数学建模》Chapter 5.1 SIR Model
# In[37]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# In[38]:


def model(y,t,lamda,mu):
    i=y[0]
    s=y[1]
    didt=lamda*s*i-mu*i
    dsdt=-lamda*s*i
    return [didt,dsdt]


# In[39]:


#define initial conditions
i0=0.02
s0=0.98
y0=[i0,s0]

#define time point with x-axis
t=np.linspace(0,20,100)


# In[40]:


#solve odes
lamda1=5
mu1=0.3
y1=odeint(model,y0,t,args=(lamda1,mu1,))

lamda2=1
mu2=1.5
y2=odeint(model,y0,t,args=(lamda2,mu2,))

lamda3=0.5
mu3=1.5
y3=odeint(model,y0,t,args=(lamda3,mu3,))


# In[41]:


plt.plot(t,y1[:,0],'r*',label='i(t)')
plt.plot(t,y1[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda1=5,mu1=0.3')
plt.show()


# In[42]:


plt.plot(t,y2[:,0],'r*',label='i(t)')
plt.plot(t,y2[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda2=1,mu2=1.5')
plt.show()
print(y2[:,0])
print(y2[:,1])


# In[43]:


plt.plot(t,y3[:,0],'r*',label='i(t)')
plt.plot(t,y3[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda3=0.5,mu3=1.5')
plt.show()
print(y3[:,0])
print(y3[:,1])


# In[ ]:





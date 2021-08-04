#!/usr/bin/env python
# coding: utf-8

# Migrated from Online Jupyter tool: https://cocalc.com/projects/72d61fec-dd0b-4937-8a22-436ce298f6cd  
# The case is from chapter 5.1 of <Math Modelling> SIR model & SIS model



# In[1]:


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# In[2]:


#SIR Model: Applicable for the scenario: Infected samples after recovery have anti-infection effect afterwards
def SIRmodel(y,t,lamda,mu):
    i=y[0]
    s=y[1]
    didt=lamda*s*i-mu*i
    dsdt=-lamda*s*i
    return [didt,dsdt]
#Note:'lamda' means infected individuals by each infected sample everyday. The meaining of 'lamda' keeps unchanged afterwards in this project.
#Note:'mu' means percentage of recovered individuals everyday on top of all infected samples.The meaining of 'mu' keeps unchanged afterwards #in this project.


# In[3]:


#Define initial conditions
i0=0.02
s0=1.0-i0
y0=[i0,s0]

#Define time point with x-axis
t=np.linspace(0,20,100)


# In[4]:


#Solve odes
lamda1=5
mu1=0.3
y1=odeint(SIRmodel,y0,t,args=(lamda1,mu1,))

lamda2=0.6
mu2=0.9
y2=odeint(SIRmodel,y0,t,args=(lamda2,mu2,))

lamda3=0.6
mu3=0.6
y3=odeint(SIRmodel,y0,t,args=(lamda3,mu3,))


# In[5]:


plt.plot(t,y1[:,0],'r*',label='i(t)')
plt.plot(t,y1[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda1=5,mu1=0.3')
plt.show()


# In[6]:


plt.plot(t,y2[:,0],'r*',label='i(t)')
plt.plot(t,y2[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda2=0.6,mu2=0.9')
plt.show()
#print(y2[:,0])
#print(y2[:,1])


# In[7]:


plt.plot(t,y3[:,0],'r*',label='i(t)')
plt.plot(t,y3[:,1],'g--',label='s(t)')
plt.legend()
plt.title('lamda3=0.6,mu3=0.6')
plt.show()
#print(y3[:,0])
#print(y3[:,1])


# In[ ]:





# In[8]:


#SIS Model: Applicable for the scenario: Infected samples after recovery have NO anti-infection effect afterwards
def SISmodel(i,t,lamda,mu):
    didt=-lamda*i*(i-(1-1/(lamda/mu)))
    return didt


# In[9]:


#Define initial conditions
i0=0.1

#Define i with x-axis
i=np.linspace(0,1,100)


# In[10]:


#Plot function diagram:didt vs i with Scenario 1:lamda1=5,mu1=0.3
lamda1=5
mu1=0.3
didt1=lambda i:-lamda1*i*(i-(1-1/(lamda1/mu1)))
plt.plot(i,didt1(i),'b*',label='lamda1=5,mu1=0.3')

#Plot function diagram:didt vs i with Scenario 2:lamda2=0.6,mu2=0.9
lamda2=0.6
mu2=0.9
didt2=lambda i:-lamda2*i*(i-(1-1/(lamda2/mu2)))
plt.plot(i,didt2(i),'g--',label='lamda2=0.6,mu2=0.9')

#Plot function diagram:didt vs i with Scenario 3:lamda3=0.6,mu3=0.6
lamda3=0.6
mu3=0.6
didt3=lambda i:-lamda3*i*(i-(1-1/(lamda3/mu3)))
plt.plot(i,didt3(i),'r-',label='lamda3=0.6,mu3=0.6')

plt.legend()
plt.xlabel('i')
plt.ylabel('di/dt')
plt.show()


# In[11]:


#Define time point with x-axis
t=np.linspace(0,20,1000)


# In[12]:


#Solve ODE
lamda1=3
mu1=0.3
y1=odeint(SISmodel,i0,t,args=(lamda1,mu1,))

lamda2=0.6
mu2=0.9
y2=odeint(SISmodel,i0,t,args=(lamda2,mu2,))

lamda3=0.6
mu3=0.6
y3=odeint(SISmodel,i0,t,args=(lamda3,mu3,))


# In[13]:


#print(y1,y2,y3)
plt.plot(t,y1,'b*',label='lamda1=3,mu1=0.3')
plt.plot(t,y2,'g--',label='lamda2=0.6,mu2=0.9')
plt.plot(t,y3,'r-',label='lamda3=0.6,mu3=0.6')
plt.xlabel('t')
plt.ylabel('i(t)')
plt.legend()
plt.show()


# In[ ]:






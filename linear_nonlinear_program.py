#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nonlinear_programming.py
#  
#  Copyright 2021 yuncwang <yuncwang@N-20N3PF1Y4QS0>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.




#### Linear Program Modeling ####
# Question 1:

from scipy import optimize as op
import numpy as np
import math

a=[1.25,8.75,0.5,5.75,3,7.25]
b=[1.25,0.75,4.75,5,6.5,7.25]
x=[5,2]
y=[1,7]
c=[]

#计算距离
for j in range(0,2):
    for i in range(0,6):
        c.append(math.sqrt((a[i]-x[j])**2+(b[i]-y[j])**2))
	
c=np.array(c)

#不等式约束
A=np.zeros((2,12))
A=np.array([[1,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,1,1]])
#不等式约束向量
B=[20,20]

#等式约束
Aeq=np.zeros((6,12))
for i in range(0,6):
    Aeq[i,i]=1
    Aeq[i,i+6]=1

#等式约束向量
Beq=np.array([3,5,4,7,6,11])

#每个变量限制范围
X11=(0,3)
X12=(0,5)
X13=(0,4)
X14=(0,7)
X15=(0,6)
X16=(0,11)
X21=(0,3)
X22=(0,5)
X23=(0,4)
X24=(0,7)
X25=(0,6)
X26=(0,11)

res=op.linprog(c,A,B,Aeq,Beq,bounds=(X11,X12,X13,X14,X15,X16,X21,X22,X23,X24,X25,X26))
print(res)



#### Nonlinear Program Modeling ####
# Question 2:
# Note: The code below is still under debugging

from scipy import optimize as op
import numpy as np
import math
#六个补给点的坐标位置
a=[1.25,8.75,0.5,5.75,3,7.25]
b=[1.25,0.75,4.75,5,6.5,7.25]

#设置A/B供应点X轴坐标[xa,xb]初始值
xa=1
xb=1
#设置A/B供应点Y轴坐标[ya,yb]初始值
ya=1
yb=1

#从A/B供应点运输到六个补给点的重量
x1=[0,0,0,0,0,0]
x2=[3,5,4,7,6,11]

#定义计算从供应点到补给点的距离公式
def distance(x,y,x0,y0):
    dis=math.sqrt((x-x0)**2+(y-y0)**2)
    return dis    

#定义目标函数，方便后面获取最小值
def fun(xa,xb,ya,yb,x1,x2):
    objective=0
    for i in range(0,6):
        objective=objective+distance(a[i],b[i],xa,ya)*x1[i]+distance(a[i],b[i],xb,yb)*x2[i]
    return objective

#设置约束条件
def constraint1(x1):
    sum_good1=20
    for i in range(0,6):
        sum_good1=sum_good1-x1[i]
    return sum_good1

def constraint2(x2):
    sum_good2=20
    for i in range(0,6):
        sum_good2=sum_good2-x2[i]
    return sum_good2    

def constraint3(x1,x2):
    return x1[0]+x2[0]-3

def constraint4(x1,x2):
    return x1[1]+x2[1]-5

def constraint5(x1,x2):
    return x1[2]+x2[2]-4

def constraint6(x1,x2):
    return x1[3]+x2[3]-7

def constraint7(x1,x2):
    return x1[4]+x2[5]-6

def constraint8(x1,x2):
    return x1[5]+x2[5]-11


#设置六个补给点变量限制范围
bnds=((0,10),(0,10),(0,10),(0,10),(0,3),(0,5),(0,4),(0,7),(0,6),(0,11),(0,3),(0,5),(0,4),(0,7),(0,6),(0,11))

#设置约束条件
con1=({'type':'ineq','fun':constraint1},\
    {'type':'ineq','fun':constraint2})
con2=({'type':'eq','fun':constraint3},\
    {'type':'eq','fun':constraint4},\
    {'type':'eq','fun':constraint5},\
    {'type':'eq','fun':constraint6},\
    {'type':'eq','fun':constraint7},\
    {'type':'eq','fun':constraint8})
cons=[con1,con2]

#设置初始值
x0=[0,0,0,0,0,0,0,0,0,0,3,5,4,7,6,11]

res=op.minimize(fun,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(res)



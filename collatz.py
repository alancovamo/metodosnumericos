# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:12:03 2021

@author: Alan
"""
import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    a=[x]
    if x==1:
        return a
    else:
        while x!=1:
            
            if (x%2) == 0:
                x=x/2
                a.append(x)
            else:
                x=3*x+1
                a.append(x)
    return a            
k=10
plt.figure(0)
for i in range(1,k):        
    n=len(f(i+1))
    m=np.arange(0,n,1)
    
    plt.plot(m,f(i+1),label='%d' %(i+1))
    
    plt.legend()
    plt.show()

#plt.figure(1)   
#for i in range(1,k):        
    #n=len(f(i+1))
    #m=np.arange(0,n,1)
    
    #plt.plot(m,np.log(f(i+1)),label='%d' %(i+1))
    
    #plt.legend()
    #plt.show()
#for i in range(1):
 #   n=len(f(i+1))
  #  m=np.arange(0,n,1)
   # plt.scatter(m,f(i))
    #plt.show()



from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:38:36 2018

@author: jameslowe1995
"""


"""
2D Ising model v1.1

Modified
Version 1.0: Thu Nov  9 17:34:37 2017
version 1.1: Sun Jan 22 18:54:34 2018

@author: jameslowe1995

"""
#libraries


import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand
import numpy

def Magvtemp(T):
    sweeps = 0
    M1 = numpy.zeros(MonteCarloSweeps)
    Time = numpy.zeros(MonteCarloSweeps)
    while sweeps < MonteCarloSweeps:
        M = 0           
        for x in range(0,L):
            for y in range(0,L):
                s =  lattice[x, y]
                energy = 0
                                    #boundary condition 1
                if y == 0:
                    if x == 0:
                        Eflip = lattice[(x+1)%L,y] + lattice[x,(y+1)%L] + lattice[(L-1)%L,y] + lattice[x,(L-1)%L]                
    
                #boundary condition 2
                if y == 0:
                    if x < L-1:
                        if x != 0:
                            Eflip = lattice[(x+1)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y] + lattice[x,(L-1)%L]      
    
                #boundary condition 3  
                if y == 0:
                    if x == L-1:
                        Eflip = lattice[(0)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y] + lattice[x,(L-1)%L]  
    
                #boundary condition 4  
                if y > 0:
                    if x == 0:
                        Eflip = lattice[(x+1)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y]+lattice[(L-1)%L,y]
    
                #boundary condition 5        
                if y > 0:
                    if y != L-1:
                        if x == L-1:
                            Eflip = lattice[(x-1)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y]+lattice[(0)%L,y]
    
                #boundary condition 6
                if y == L-1:
                    if x == 0:
                        Eflip = lattice[(x+1)%L,y] + lattice[x,(0)%L] + lattice[(L-1)%L,y]+lattice[x,(y-1)%L]
    
                #boundary condition 7                      
                if y == L-1:
                    if x < L-1:
                        if x != 0:
                            Eflip = lattice[(x+1)%L,y] + lattice[x,(0)%L] + lattice[(x-1)%L,y]+ lattice[x,(y-1)%L]                            
    
                #boundary condition 8            
                if y == L-1:
                    if x == L-1:
                        Eflip = lattice[(0)%L,y] + lattice[x,(L-1)%L] + lattice[(x-1)%L,y]+ lattice[x,(y-1)%L]
    
                #boundary condition 9                      
                if y < L-1:
                    if y > 0:
                        if x < L-1:
                            if x > 0:
                                Eflip = lattice[(x+1)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y]+ lattice[x,(y-1)%L]
                Eflip2 = 2*s*Eflip
    
                if Eflip2 < 0:
                    s = s*-1 #flip the value
    
                elif rand() < np.exp(-Eflip2*(1/T)):
                    s = s*-1 #flip the value
               
                lattice[x,y] = s                 
                                             
        sweeps = sweeps + 1
        value = lattice[x,y]

        magnetism = np.sum(lattice)
        
        M = M + magnetism
                    
        magnetism = 0
        
        M1[sweeps-1] = (M/(L*L))
        Time[sweeps-1] = sweeps
    
    T = T + Tinterval 
                    
    plt.figure(3,figsize=(10, 10))
    plt.ylim([-1.1,1.1])
    plt.xlim([0,MonteCarloSweeps])
    plt.tick_params(labelsize=30)
    plt.plot(Time, M1, 'k-')
    plt.xlabel("Time",fontsize=30)
    plt.ylabel("Magnetization",fontsize=30)
    plt.title("Magnetization vs Time",fontsize=30)
    
    plt.show()          

                      

#Adjustable Varibles
H = 1   # Initializng lattice: 1 = all +1s, 2 = all -1s, 3 = random +1s and -1s
Tfinal = 5 #Final temperature
Tinterval = .1 # Intervals between temperature points
L = 10 #Lattice array L*L
MonteCarloSweeps = 1000 #Monte Carlo Sweeps
T = 1

#Fixed variables
i = 1
j = 1
r = 0
m = 0
#Kb = 1.38064852e-23 #Boltzmanns constant
TempRange = Tfinal - T

if H == 1:

    #Initialize lattice all +1s
    lattice = numpy.zeros((L, L))+1

if H == 2:

    #Initialize lattice all -1s
    lattice = numpy.zeros((L, L))-1

if H ==3:
    #Initialize lattice random +1s and -1s
    lattice = 2*np.random.randint(2, size=(L,L))-1
 
Magvtemp(1.5)
Magvtemp(2)
Magvtemp(2.25)
Magvtemp(4)



  
                        
          
   
    
       
    


@author: jameslowe1995


#libraries
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import numpy



def IsingModel(T,Tinterval,Tfinal,L,MonteCarloSweeps,lattice):
    while T <= Tfinal:
    
        sweeps = 0
        x = 0
        y = 0
        z = 0
        energy = 0
        magnetism =0
        E = 0
        M = 0
        Esquared = 0
        deltaEsquared = 0
        C = 0
    
        while sweeps < MonteCarloSweeps:
              while z == 0:
                    if x < (L):
                        if y < (L):
                            s =  lattice[x, y]
                            energy = 0
                            if y == 0:
                                if x == 0:
                                    Eflip = lattice[(x+1),y] + lattice[x,(y+1)] + lattice[(L-1),y] + lattice[x,(L-1)]                
                            
                            #boundary condition 2
                            if y == 0:
                                if x < L-1:
                                    if x != 0:
                                        Eflip = lattice[(x+1),y] + lattice[x,(y+1)] + lattice[(x-1),y] + lattice[x,(L-1)]      
                            
                            #boundary condition 3  
                            if y == 0:
                                if x == L-1:
                                    Eflip = lattice[(0),y] + lattice[x,(y+1)] + lattice[(x-1),y] + lattice[x,(L-1)]  
                            
                            #boundary condition 4  
                            if y > 0:
                                if y < L-1:
                                    if x == 0:
                                        Eflip = lattice[(x+1),y] + lattice[x,(y+1)] + lattice[(x-1),y]+lattice[(L-1),y]
                            
                            #boundary condition 5        
                            if y > 0:
                                if y != L-1:
                                    if x == L-1:
                                        Eflip = lattice[x,(y-1)] + lattice[x,(y+1)] + lattice[(x-1),y]+lattice[0,y]
                            
                            #boundary condition 6
                            if y == L-1:
                                if x == 0:
                                    Eflip = lattice[(x+1),y] + lattice[x,(0)] + lattice[(L-1),y]+lattice[x,(y-1)]
                            
                            #boundary condition 7                      
                            if y == L-1:
                                if x < L-1:
                                    if x != 0:
                                        Eflip = lattice[(x+1),y] + lattice[x,0] + lattice[(x-1),y]+ lattice[x,(y-1)]                            
                            
                            #boundary condition 8            
                            if y == L-1:
                                if x == L-1:
                                    Eflip = lattice[(0),y] + lattice[x,(L-1)] + lattice[(x-1),y]+ lattice[x,(y-1)]
                            
                            #boundary condition 9                      
                            if y < L-1:
                                if y > 0:
                                    if x < L-1:
                                        if x > 0:
                                            Eflip = lattice[(x+1),y] + lattice[x,(y+1)] + lattice[(x-1),y]+ lattice[x,(y-1)]    
                       
                            Eflip2 = 2*s*Eflip
                            #print((np.random.uniform(0, 1)))
                            if Eflip2 <= 0:
                                s = s*-1 #flip the value
                            
                            
                            elif np.random.uniform(0, 1) < np.exp(-Eflip2/(T)):
                                s = s*-1 #flip the value
                           
                        lattice[x,y] = s                 
        
                        if y <= L-1:
                            x = x + 1
        
                            if x == L:
                                x = 0
                                y = y + 1
        
                        if y == L:
                            x = 0
                            y = 0
                            sweeps = sweeps + 1
                            Mx = np.sum(lattice)
                            M = M + Mx
        
                        value = lattice[x,y]
                        energy = Eflip*(value)
                        
                        
        
                        energy = energy/4
                        E = E + energy
                                            
                        Esquared = Esquared + energy*energy
                        
                        energy = 0
                        magnetism = 0
        
                        
                        if sweeps == MonteCarloSweeps:
                            z = 1                      
                
                    
        E1 = (E/(MonteCarloSweeps*L*L))*-2
        #print(M)
        M1 = (M/(MonteCarloSweeps*L*L))   
       # print(M1)   
        Esquared = (Esquared/(MonteCarloSweeps*L*L))
        E2 = ((E/(MonteCarloSweeps*L*L)))
        E2 = E2*E2
        deltaEsquared =  (Esquared - E2)
        C = (deltaEsquared/(T*T))  
    
        plt.figure(1,figsize=(20, 20))
        plt.xticks((0,1,2,3,4,5), ('0', '1','2','3','4','5'), color='k', size=30)
        plt.yticks((-2, -1, 0), ('-2','-1','0'), color='k', size=30)
        plt.ylim([-2,0])
        plt.xlim([0,5])
        plt.plot(T, E1,marker,markersize = 15.0)
        plt.xlabel("Temperature",size=30)
        plt.ylabel("Energy per Spin",size=30)
        plt.title("Thermal average of the energy versus temperature",size=30)
    
        plt.figure(2,figsize=(20, 20))
    
        plt.plot([6,0], [0,0], 'k--', lw=2)
        plt.xticks((0, 1,2,3,4,5), ('0', '1','2','3','4','5'), color='k', size=30)
        plt.yticks((0, 0.5, 1), ('0','0.5','1'), color='k', size=30)
        plt.ylim([-0.1,1.01])
        plt.xlim([0,5])
        plt.plot(T, M1, marker ,markersize = 15.0)
        plt.xlabel("Temperature",size=30)
        plt.ylabel("Magnetization ",size=30)
        plt.title("Spontaneous magnetization as a function of temperature",size=30)
    
        plt.figure(3,figsize=(20, 20))
        plt.ylim([0,1.5])
        plt.xlim([0,5])
        plt.xticks((0, 1,2,3,4,5), ('0', '1','2','3','4','5'), color='k', size=30)
        plt.yticks((0, 0.5, 1,1.5), ('0','0.5','1','1.5'), color='k', size=30)
        plt.plot(T, C*33, marker ,markersize = 15.0)
        plt.xlabel("Temperature",size=30)
        plt.ylabel("Specific heat per spin",size=30)
        plt.title("Specific heat capacity",size=30)

        
        print(T)
        
        T = T + Tinterval
        T = round(T,1)

#Adjustable Varibles
Tfinal = 5 #Final temperature
Tinterval = .1 # Intervals between temperature points
T = 1 #Starting temperature
L = 100 #Lattice array L*L
MonteCarloSweeps = 1000 #Monte Carlo Sweeps

#Initialize lattice all +1s
lattice = numpy.zeros((L, L))+1
marker = 'bo'
IsingModel(T,Tinterval,Tfinal,L,MonteCarloSweeps,lattice)

#Initialize lattice all +1s
lattice = numpy.zeros((L, L))+1
marker = 'ro'
IsingModel(T,Tinterval,Tfinal,L,MonteCarloSweeps,lattice)

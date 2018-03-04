"""
2D Ising model v1.1.2

Modified
Version 1.0: Thu Nov  9 17:34:37 2017
Version 1.1: Sun Jan 21 18:54:34 2018
Version 1.1.1 Mon Jan 22 20:34:28 2018
Version 1.1.2 Mon Jan 29 11:08:00 2018

@author: jameslowe1995

"""
#libraries
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy.random import rand
import numpy
matplotlib.use("Agg")
import matplotlib.animation as manimation

#Adjustable Varibles
H = 2   # Initializng lattice: 1 = all +1s, 2 = all -1s, 3 = random +1s and -1s
Tfinal = 5 #Final temperature
Tinterval = .1 # Intervals between temperature points
T = 1 #Starting temperature
L = 10 #Lattice array L*L
MonteCarloSweeps = 100 #Monte Carlo Sweeps

#Fixed variables
i = 1
j = 1
r = 0
m = 0
Kb = 1.38064852e-23 #Boltzmanns constant
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

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',comment='Movie support!')
writer = FFMpegWriter(fps=MonteCarloSweeps,metadata=metadata)


fig = plt.figure(figsize=(10, 10), dpi=80)
X, Y = np.meshgrid(range(L), range(L))

plt.xlim(0, L-1)
plt.ylim(0, L-1)

#plot intial lattice            
with writer.saving(fig, "2D_Ising_Model.mp4", 100):
    while T <= Tfinal:
    
        sweeps = 0
        x = 0
        y = 0
        z = 0
        energy = 0
        magnetism =0
        E = 0
        M = 0
        S = 0
        latticetotal = numpy.zeros((L, L))
    
        while sweeps < MonteCarloSweeps:
            while z == 0:
                if x < (L):
                    if y < (L):
                        s =  lattice[x, y]
    
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
            
                        if y <= L-1:
                            x = x + 1
            
                            if x == L:
                                x = 0
                                y = y + 1
            
                        if y == L:
                            x = 0
                            y = 0
                            
                            
                            plt.pcolormesh(X, Y, lattice, cmap=plt.cm.RdBu);
                            plt.grid("off")
                            plt.title('2D Ising Model',size=30)
                            plt.text(3.1, -0.7, 'T =', fontsize=30)
                            plt.xlabel(round(T,1),size=30)
                            writer.grab_frame()
                           

                            sweeps = sweeps + 1                    
                    
            
                if sweeps == MonteCarloSweeps:
                    z = 1                                 
                    RemainingTempRange = Tfinal - T
                    PercentageComplete = 100 -(RemainingTempRange/TempRange)*100
                    print("Percentage Completed = ", int(round(PercentageComplete)), "%")
            
        T = T + Tinterval

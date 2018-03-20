"""

2D Ising model correlation functions v1



@author: jameslowe1995



"""



#libraries

from __future__ import division

import numpy as np

import matplotlib.pyplot as plt

from numpy.random import rand

import numpy



#Adjustable Varibles

H = 2   # Initializng lattice: 1 = all +1s, 2 = all -1s, 3 = random +1s and -1s

Tfinal = 5 #Final temperature

Tinterval = .25 # Intervals between temperature points

T = 1 #Starting temperature

L = 20 #Lattice array L*L

MonteCarloSweeps = 100 #Monte Carlo Sweeps



#Fixed variables

i = 1

j = 1

r = 0

m = 0

#Kb = 1.38064852e-23 #Boltzmanns constant



if H == 1:



    #Initialize lattice all +1s

    lattice = numpy.zeros((L, L))+1



if H == 2:



    #Initialize lattice all -1s

    lattice = numpy.zeros((L, L))-1



if H ==3:

    #Initialize lattice random +1s and -1s

    lattice = 2*np.random.randint(2, size=(L,L))-1



while T <= Tfinal:



    sweeps = 0

    x = 0

    y = 0

    z = 0

    energy = 0

    magnetism =0

    E = 0

    latticetotal = numpy.zeros((L, L))

    corelation1 = 0

    corelation2 = 0

    corelation3 = 0

    corelation4 = 0

    corelation5 = 0

    corelation6 = 0

    corelation7 = 0

    corelation8 = 0

    corelation9 = 0

    corelation10 = 0



    while sweeps < MonteCarloSweeps:

      while z == 0:

            if x < (L):

                if y < (L):

                    s =  lattice[x, y]

                    energy = 0

                    #boundary condition 1



                    Eflip = lattice[(x+1)%L,y] + lattice[x,(y+1)%L] + lattice[(x-1)%L,y] + lattice[x,(y-1)%L]

                                

                    Eflip2 = 2*s*Eflip



                    if Eflip2 < 0:

                        s = s*-1 #flip the value



                    elif rand() < np.exp(-Eflip2*(1/T)):

                        s = s*-1 #flip the value

                 

                    for i in range(0,11):

                        correlation = (lattice[x,y] * (lattice[(x+i)%L,y] + lattice[x,(y+i)%L] + lattice[(x-i)%L,y] + lattice[x,(y-i)%L]))

                     

                        if i == 1:

                            corelation1 = corelation1 + correlation

                                                             

                        if i == 2 or i == 1:

                            corelation2 = corelation2 + correlation

                             

                        if i == 3 or i == 2 or i == 1:

                            corelation3 = corelation3 + correlation

                             

                        if i == 4 or i == 3 or i == 2 or i == 1:

                            corelation4 = corelation4 + correlation

                             

                        if i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation5 = corelation5 + correlation

                             

                        if i == 6 or i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation6 = corelation6 + correlation

                             

                        if i == 7 or i == 6 or i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation7 = corelation7 + correlation

                             

                        if i == 8 or i == 7 or i == 6 or i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation8 = corelation8 + correlation

                             

                        if i == 9 or i == 8 or i == 7 or i == 6 or i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation9 = corelation9 + correlation

                                                         

                        if i == 10 or i == 9 or i == 8 or i == 7 or i == 6 or i == 5 or i == 4 or i == 3 or i == 2 or i == 1:

                            corelation10 = corelation10 + correlation



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

             

                if sweeps == MonteCarloSweeps:

                    z = 1                   



    corelation1 = corelation1/4

    corelation2 = corelation2/8

    corelation3 = corelation3/12

    corelation4 = corelation4/16

    corelation5 = corelation5/20

    corelation6 = corelation6/24

    corelation7 = corelation7/28

    corelation8 = corelation8/32

    corelation9 = corelation9/36

    corelation10 = corelation10/40



    corelation1 = corelation1/(MonteCarloSweeps*L*L)

    corelation2 = corelation2/(MonteCarloSweeps*L*L)

    corelation3 = corelation3/(MonteCarloSweeps*L*L)

    corelation4 = corelation4/(MonteCarloSweeps*L*L)

    corelation5 = corelation5/(MonteCarloSweeps*L*L)

    corelation6 = corelation6/(MonteCarloSweeps*L*L)

    corelation7 = corelation7/(MonteCarloSweeps*L*L)

    corelation8 = corelation8/(MonteCarloSweeps*L*L)

    corelation9 = corelation9/(MonteCarloSweeps*L*L)

    corelation10 = corelation10/(MonteCarloSweeps*L*L)

 

    Totalcorelation = [corelation1,corelation2,corelation3,corelation4,corelation5,corelation6,corelation7,corelation8,corelation9,corelation10]

 

    print("Totalcorelation = ", Totalcorelation)

    print("t = ", T)

    if T == 1.5:

     

        plt.figure(2,figsize=(10, 10))

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'r-', )

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'ro', )

        plt.xlabel("i",size=20)

        plt.ylabel("f(i) = <si so> ",size=20)

        plt.title("Ising model correlations",size=20)

     

    if T == 2:

     

        plt.figure(2,figsize=(20, 20))

 

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'g-', )

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'go', )



     

    if T == 2.25:

     

        plt.figure(2,figsize=(20, 20))

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'b-', )

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'bo', )



     

    if T == 3:

     

        plt.figure(2,figsize=(20, 20))

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'c-', )

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'co', )



     

    if T == 5:

     

        plt.figure(2,figsize=(20, 20))

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'm-', )

        plt.plot([1,2,3,4,5,6,7,8,9,10],Totalcorelation , 'mo', )





    T = T + Tinterval


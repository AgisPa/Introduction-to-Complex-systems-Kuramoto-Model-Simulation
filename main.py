


import numpy as np
import euler
import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

start_time = time.time()

#Input that leads to different subquestions

ROOT = tk.Tk()
ROOT.eval('tk::PlaceWindow . center')

ROOT.withdraw()
input =simpledialog.askstring(title="Plot Choice",
                              prompt="Choose a type of plot:\n(a) r(T)-K for N(0,1)\n(b) r(t) for K=1 and K=2 for N(0,1)"
                                      "\n(c) r(T)-K for uniform distribution \n(d) fixed ω for uniform distribution\n(e) fixed initial conditions for uniform distribution"
                                    "\n Input the letter of your choice:")

#Parameter that reduces the size of the system uniformly
reduction=0.1
#Estimated run time of around 20 mins per graph

#Initialization for each subquestion
if input=="a" or input=="b":
    N=int(1000*reduction)
    T=100*reduction
    dt=0.1
    g=1/2
    dk = 0.2
elif input=="c" or input=="d" or input=="e":
    N=int(2000*reduction)
    T=200*reduction
    dt=0.05
    g=1/2
    dk = 0.03
else:
    print("wrong input")


#Main body where the function euler is used to extract the results which are then plotted

if input=="a":
    kc = 2 * np.sqrt(2 / np.pi)
    kappa = 0.5
    k = 0
    rT = np.zeros([int(1.5/dk)+1])
    while kappa < 2:
        rT[k] = euler.euler(N, kappa, g, T, dt, input,1)
        k = k + 1
        kappa = kappa + dk
    plt.figure(figsize=(10, 5))
    plt.scatter([0.5 + i * 0.2 for i in range(0, int(1.5/dk)+1)], rT, label='Order Parameter')
    plt.axvline(x=kc,color='orange',label='Kc = '+str(round(kc,4)))
    plt.axis(xlim=(0.5, 2), ylim=(0, 1))
    plt.title("Order parameter as a function of coupling constant")
    plt.ylabel("Order Parameter r(T)")
    plt.xlabel("Coupling constant K")
    plt.grid()
    plt.legend()
    plt.show()

if input=="b":
    t=[int(i) for i in range(int(T/dt))]
    plt.figure(figsize=(10, 5))
    r1=plt.scatter(t,euler.euler(N, 1,g, T, dt, input,1),label='K=1')
    r2=plt.scatter(t,euler.euler(N, 2,g, T, dt, input,1),label='K=2')
    plt.axis(xlim=(0.5, 2), ylim=(0, 1))
    plt.title("Order parameter as a function of time")
    plt.ylim(0,1)
    plt.ylabel("Order Parameter r(t)")
    plt.xlabel("Timesteps")
    plt.grid()
    plt.legend()
    plt.show()

if input=="c":
    kappa=0.5
    k = 0
    rT = np.zeros([int(1 / dk) + 1])
    kc=2/np.pi
    while kappa < 1.5:
        rT[k] = euler.euler(N, kappa, g, T, dt, input,1)
        k = k + 1
        kappa = kappa + dk
    plt.figure(figsize=(10, 5))
    plt.scatter([0.5 + i * dk for i in range(0, int(1 / dk) + 1)], rT, label='Order Parameter')
    plt.axvline(x=kc, color='orange', label='Kc = '+str(round(kc,3)))
    plt.axis(xlim=(0.5, 2), ylim=(0, 1))
    plt.title("Order parameter as a function of coupling constant")
    plt.ylabel("Order Parameter r(T)")
    plt.xlabel("Coupling constant K")
    plt.grid()
    plt.legend()
    plt.show()

if input=="d":
    kappa=1
    plt.figure(figsize=(10, 5))
    for i in range(11):
        r=euler.euler(N, kappa,g, T, dt,input,1)
        plt.plot(r, label='Simulation number = '+str(i))
        plt.axis(xlim=(0.5, 2), ylim=(0, 1))
        plt.title("Order parameter as a function of time")
        plt.ylabel("Order Parameter r(t)")
        plt.xlabel("Timesteps")
        plt.grid()
        plt.legend()
    plt.show()

if input=="e":
    kappa=1
    plt.figure(figsize=(10, 5))
    t = [int(i) for i in range(int(T / dt))]
    for seed in range(10):
        r=euler.euler(N, kappa,g, T, dt,input,seed)
        plt.scatter(t,r, label='Order Parameter for seed =' +str(seed))
        plt.axis(xlim=(0.5, 2), ylim=(0, 1))
        plt.title("Order parameter as a function of time")
        plt.ylabel("Order Parameter r(t)")
        plt.xlabel("Timesteps")
        plt.legend()
    plt.grid()
    plt.show()
stop_time=time.time()
print("Elapsed time: "+str(round((stop_time-start_time)/60,5))+"mins")
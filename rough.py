import numpy as np
from numpy import sin, cos, pi
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as animation


amp = 1
def generating_signal(tm,noise_flag=True):
    f1 = 1
    f2 = 10
    x = (2*sin(2*pi*f1*tm))+ (4*sin(2*pi*f2*tm))
    #print(tm)
    if (noise_flag):
        x +=(3*np.random.random(tm.size))
        print("noise added")
    return x


Fs=40
delF=0.0780
# delF=0.001
N=int(Fs/delF)
Tw=N/Fs

t=np.linspace(0,Tw,num=N)
signal=generating_signal(t)
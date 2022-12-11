import numpy as np
from numpy import sin, cos, pi
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt

#genarating signal
def generating_signal(tm,noise_flag=True):
    f1 = 1 #GHz
    f2 = 10 #GHz
    x = ((2*sin(2*pi*f1*tm))+ (4*sin(2*pi*f2*tm)))
    print(tm)
    if (noise_flag):
        x +=(3*np.random.random(tm.size))
        if __name__ == "__main__":
            print("noise added")
    return x
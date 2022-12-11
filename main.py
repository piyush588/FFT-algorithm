import numpy as np
from numpy import sin, cos, pi
from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt
from wave_generater import generating_signal

Fs=50    #40 origianl
delF=0.0880   #0.780 original
# delF=0.001
N=int(Fs/delF)
Tw=N/Fs

t=np.linspace(0,Tw,num=N)
signal=generating_signal(t)

print('Signal generated of duration {} sec'.format(Tw))

spectrum=fft(signal)
F=fftfreq(N,1/Fs)
Fpositive=np.where(F>=0)
#print(F.shape)
#print(type(Fpositive))
#print(spectrum.shape)
#print(Fpositive)


#ploting 
plt.figure(figsize=(20,4))

plt.subplot(1,2,1)
plt.plot(t,signal)
plt.xlabel('Time(Sec)',fontsize=14)
plt.ylabel('Signal',fontsize=14)

plt.subplot(1,2,2)
plt.plot(F[Fpositive],np.absolute(spectrum[Fpositive])/N,color='r')
plt.xlabel('Frequency(GHz)',fontsize=14)
plt.ylabel('Amplitude Spectrum',fontsize=14)
plt.show()

freq_thr=2
spectrum_filter= spectrum*(np.absolute(F)<freq_thr)
signal_filter=ifft(spectrum_filter)

spectrum_output=fft(signal_filter)

#@title Plot Filter Data & Spectrum
fig=plt.figure(figsize=(20,4))
gs=fig.add_gridspec(2,2)

ax1=fig.add_subplot(gs[:,0])
ax2=fig.add_subplot(gs[0,1])
ax3=fig.add_subplot(gs[1,1])


ax1.plot(t,signal,label='Input')
ax1.plot(t,signal_filter.real,color='r',label='output')
ax1.legend(fontsize=14)
ax1.set_xlabel('Time(sec)',fontsize=14)
ax1.set_ylabel('Signal',fontsize=14)

ax2.plot(F[Fpositive],np.absolute(signal[Fpositive])/N,label='Input')
ax2.grid()
ax1.legend(fontsize=14)
ax2.set_xlabel('Time(sec)',fontsize=14)
ax2.set_ylabel('Spectrum',fontsize=14)


ax3.plot(F[Fpositive],np.absolute(spectrum[Fpositive])/N,color='r',label='Output')
ax3.grid()
ax1.legend(fontsize=14)
ax3.set_xlabel('Time(sec)',fontsize=14)
ax3.set_ylabel('Spectrum',fontsize=14)
plt.show()
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import lh_iirpy


unfiltered_ecg_dat = np.loadtxt('ecg.dat')  # loading ecg from dat file
fs = 1000

unfiltered_ecg = unfiltered_ecg_dat[:, 1]  # select only the data, ignoring the time column

#converting data to mV
input_start = 0
input_end = 2**12
output_start = -1
output_end = 1
unfiltered_ecg = output_start + ((output_end - output_start) / (input_end - input_start)) * (unfiltered_ecg - input_start)
unfiltered_ecg = (unfiltered_ecg*4096)/500

unfiltered_ecg_freq = np.real(np.fft.fft(unfiltered_ecg))   # frequency domain of unfiltered ecg


new_filter = lh_iirpy.IIR2Filter()  # constructor

new_filter.bandStop(2, fs, 45, 55)  # initialisation

filtered_ecg = np.empty(len(unfiltered_ecg))

for i in range(len(unfiltered_ecg)):
    filtered_ecg[i] = new_filter.filter(unfiltered_ecg[i])  # filtering


filtered_ecg_freq = np.fft.fft(filtered_ecg) # frequency domain of filtered ecg

# creating axis for plotting
t_axis = np.linspace(0, (1/fs)*len(unfiltered_ecg)*1000, len(unfiltered_ecg))
f_axis = np.linspace(0, fs, len(unfiltered_ecg_freq))


# plotting
plt.figure(1)
plt.subplot(211)
plt.plot(t_axis, unfiltered_ecg)
plt.ylabel('Voltage (mV)')
plt.xlabel('Time (ms)')
plt.title('Unfiltered ECG in Time Domain')

plt.subplot(212)
plt.plot(t_axis, filtered_ecg)
plt.ylabel('Voltage (mV)')
plt.xlabel('Time (ms)')
plt.title('Filtered ECG in Time Domain')

plt.subplots_adjust(hspace=0.7)

plt.figure(2)
plt.subplot(211)
plt.plot(f_axis, abs(unfiltered_ecg_freq))
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.title('Unfiltered ECG in Frequency Domain')

plt.subplot(212)
plt.plot(f_axis, abs(filtered_ecg_freq))
plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.title('Filtered ECG in Frequency Domain')

plt.subplots_adjust(hspace=0.7)
plt.show()

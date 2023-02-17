# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:31:21 2023

@author: Mugen
"""

from scipy.io import wavfile
from scipy.signal import stft
import matplotlib.pyplot as plt
import numpy as np
import librosa

filepath = './sample/bass1.wav'
samplerate, data = wavfile.read(filepath)
signal_dB = 20*np.log10(np.abs(data))
time = [i/samplerate for i in range(len(data))]
x, sr = librosa.load(filepath)
onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
onset_times = librosa.frames_to_time(onset_frames)
for i in range(10):
    print(onset_times[i])
    idx = int(onset_times[i]*samplerate)
    idx_end = int(idx + 0.05*samplerate)
    dChunk = data[idx:idx_end]
    f, t, Zxx = stft(dChunk, samplerate, nfft=256)
    plt.specgram(np.abs(Zxx), Fs=samplerate)
    
    plt.title('STFT Magnitude'+str(onset_times[i]))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
    break

plt.plot(time, data)
plt.xlim(left=0, right=time[-1])
plt.title('Wave Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time [sec]')
plt.show()

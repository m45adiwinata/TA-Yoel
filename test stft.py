import numpy as np
from scipy.signal import stft


# Generate sample wave data
fs = 1000  # Sampling frequency
T = 1/fs  # Sample time
t = np.arange(0, 1, T)  # Time vector
f = 2  # Frequency
wave_data = np.sin(2*np.pi*f*t)

# Apply STFT
f, t, Zxx = stft(wave_data, fs)
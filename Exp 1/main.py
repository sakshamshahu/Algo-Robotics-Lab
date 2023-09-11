import numpy as np
import matplotlib.pyplot as plt
# Parameters for the signal
sampling_rate = 1000
duration = 1.0
frequency = 50
amplitude = 1.0
# Generate a time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# Generate a sine wave signal
signal = amplitude * np.sin(2 * np.pi * frequency * t)
# Compute the Fast Fourier Transform (FFT)
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), 1.0 / sampling_rate)
# Plot the time domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
# Plot the frequency domain representation
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
# Display the plots
plt.tight_layout()
plt.show()
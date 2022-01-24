from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

# Read the audioFile
sampleRate, data = read('data\\sahil10.wav')
# Frame rate for the Audio
print(sampleRate)

# Duration of the audio in Seconds
duration = len(data) / sampleRate
print("Duration of Audio in Seconds", duration)
print("Duration of Audio in Minutes", duration/60)

time = np.arange(0, duration, 1 / sampleRate)

# Plotting the Graph using Matplotlib
plt.plot(time, data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('sahil10.wav')
plt.show()

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
frequency = 44400

# Recording duration in seconds
duration = 3.5
for i in range(15,36):
	# to record audio from
	# sound-device into a Numpy
	print("recording started")
	recording = sd.rec(int(duration * frequency),
					samplerate = frequency, channels = 2)

	# Wait for the audio to complete
	sd.wait()

	print("recording stopped")
	file = "speaker" + str(i) + ".wav"
	write(file, frequency, recording)      #nullifies bg noise automatically

	# using wavio to save the recording in .wav format
	# This will convert the NumPy array to an audio
	# file with the given sampling frequency
	# wv.write("recording1.wav", recording, frequency, sampwidth=2)   #bg noise not ignorable

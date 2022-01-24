import glob
import soundfile
import numpy as np
import librosa
from sklearn.model_selection import train_test_split


import pandas as pd
import matplotlib.pyplot as plt
from librosa import display

# engine = tts.init()
#
# for i in range(0,10):
#     engine.say("jai gjinendra")
#     engine.runAndWait()
#
#
#
# engine.stop()


audio, sr = librosa.load("data\sahil1.wav")
n_mfcc = 40

mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc).T, axis=0)

print(mfccs.shape)
print(mfccs)



def extract_feature(file_name, mfcc, chroma, mel):
  with soundfile.SoundFile(file_name) as sound_file:
    X = sound_file.read(dtype="float32")
    sample_rate=sound_file.samplerate
    if chroma:
      stft=np.abs(librosa.stft(X))
    result=np.array([])
    if mfcc:
      mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
      result=np.hstack((result, mfccs))
    if chroma:
      chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
      result=np.hstack((result, chroma))
    if mel:
      mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
      result=np.hstack((result, mel))
  return result


def load_data(test_size = 0.2):
  x, y = [], []
  return train_test_split(np.array(x), y, test_size = test_size, random_state = 9)

# fig, ax = plt.subplots()
# img = display.specshow(data, x_axis='time', ax=ax)
# fig.colorbar(img, ax=ax)
# ax.set(title='MFCC')
#
#
# datapd = pd.DataFrame(data)
# print(datapd)
#
# datapd.to_csv("featuers.csv")
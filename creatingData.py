import sounddevice as sd
import librosa
import numpy as np
from scipy.io.wavfile import write


#records your voice n times, where n is inout

def record_audio():
    fs = 44100
    duration = 3

    print("how many recordings?? ")
    n = int(input())

    for i in range(0, n+1):
        print("recording started")

        rec = sd.rec(int((duration * fs)), samplerate=fs, channels=1)

        sd.wait()

        print("recording stopped")

        fileName = "D:\\Sahil\\coding\\Python\\voice biometrics\\data\\prakhar" + str(i) + ".wav"
        write(filename=fileName, rate=fs, data=rec)

        print("record again ?\n1 for yes and 0 for no")
        choice = int(input())
        if choice == 0:
            break


def extract_mfcc(file, n_mfcc=40):
    audio, sr = librosa.load(file)

    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc).T, axis=0)

    return mfccs



# Extract mfccs

# df = pd.DataFrame(columns=range(0,40))
# print(df.columns)
# for i in range(0, 21):
#     fileName = "data\\prakhar" + str(i) + ".wav"
#
#     mfccs = extract_mfcc(fileName, 40)
#     lst = list(mfccs)
#     df.loc[len(df)] = lst
#
# print(df)
# df.to_csv("data\sahil\\prakhar.csv")



# Append all individual data to complete data.
# df1 = pd.read_csv("data\sahil\\complete_data.csv")
# print(df1.shape)
# df2 = pd.read_csv("data\sahil\\prakhar.csv")
# print(df2.shape)
#
# df1 = df1.append(df2, ignore_index=True)
# print(len(df1))
# df1.to_csv("data\sahil\complete_data.csv")
#


# record_audio()

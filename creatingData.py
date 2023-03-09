#NOTE: The functions and code snippets written in the file are used when required by calling them manually, you can modify the code to
# automate the program

import sounddevice as sd
import librosa
import numpy as np
from scipy.io.wavfile import write
import pandas as pd

#records your voice n times, where n is input by user

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

#used in model.py / used to return 40 mfccs of a particular audio file.
def extract_mfcc(file, n_mfcc=40):
    audio, sr = librosa.load(file)

    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc).T, axis=0)

    return mfccs



# Extract mfccs
def createMfccCsv():
    df = pd.DataFrame(columns=range(0,40))
    for i in range(0, 21):
        fileName = "data\\prakhar" + str(i) + ".wav"
        mfccs = extract_mfcc(fileName, 40)
        lst = list(mfccs)
        df.loc[len(df)] = lst
    df.to_csv("data\sahil\\prakhar.csv") #dont forget to change the paths (there are literally many paths in the project)


# Append all individual data to complete data.
def appendIndividualToCompleteCSV():
    df1 = pd.read_csv("data\sahil\\complete_data.csv") #read completedata.csv
    df2 = pd.read_csv("data\sahil\\prakhar.csv") #read speaker_name.csv
    df1 = df1.append(df2, ignore_index=True) #append df2 into df1
    df1.to_csv("data\sahil\complete_data.csv") # save df1 in complete_data.csv (!! Note that the csv file should not be open in excel, that will give error).


#call this function to record audio files
# record_audio()

# call this function to create speaker_name.csv files of individual speakers
# createMfccCsv()

#call this function to append speaker_name.csv of individual speaker into completedata.csv
# appendIndividualToCompleteCSV()

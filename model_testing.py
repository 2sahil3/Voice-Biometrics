import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
from sklearn.model_selection import train_test_split
import sounddevice as sd
from scipy.io.wavfile import write
from creatingData import extract_mfcc
from sklearn.metrics import confusion_matrix
import time
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

def predictor():
    df = pd.read_csv("data\\csv\\complete_data.csv")  # target variable is boolean : 1 means sahil, 0 means unknown

    Y = df["speaker"]

    X = df.drop(columns=["speaker", "Unnamed: 0"])

    print(X.shape, "\n")

    # scaling pending

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

    # MLPClassifier
    classifier = MLPClassifier(solver='adam', alpha=0.001,
                               random_state=1, max_iter=500,
                               hidden_layer_sizes=100, activation="logistic")
    classifier.fit(X_train, Y_train)
    pred_mlp = classifier.predict(X_test)
    cm_mlp = confusion_matrix(Y_test, pred_mlp)
    # print("Score of MLPClassifier: ",classifier.score(X_test, Y_test))
    print("cm of mlp: \n", cm_mlp)

    # decision tree classifier
    clf = DecisionTreeClassifier(random_state=1)
    clf.fit(X_train, Y_train)
    pred_tree = clf.predict(X_test)
    cm_tree = confusion_matrix(Y_test, pred_tree)
    # print("Score for decision tree classifier: ", clf.score(X_test,Y_test))
    print("cm of tree: \n", cm_tree)
    print(pred_tree, "\n")
    print(Y_test)

    # random forest classifier
    clf_forest = RandomForestClassifier(max_depth=100, random_state=1
                                        , n_estimators=8, criterion="entropy",
                                        max_features="auto")
    clf_forest.fit(X_train, Y_train)
    pred_forest = clf_forest.predict(X_test)
    cm_forest = confusion_matrix(Y_test, pred_forest)
    # print("Score for Random forest classifier: ", clf_forest.score(X_test, Y_test))
    print("cm of forest: \n", cm_forest)

    # K nearest neighbours classifier
    neigh = KNeighborsClassifier(n_neighbors=5, weights="uniform"
                                 , algorithm="ball_tree")
    neigh.fit(X_train, Y_train)
    pred_neigh = neigh.predict(X_test)
    cm_neigh = confusion_matrix(Y_test, pred_neigh)
    # print("Score for KNN classifier: ", neigh.score(X_test, Y_test))
    print("cm of K neighbour: \n", cm_neigh)

    # Naive Bayes gaussian
    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    pred_gnb = gnb.predict(X_test)
    cm_gnb = confusion_matrix(Y_test, pred_gnb)
    # print("Score for gaussian NB classifier: ", gnb.score(X_test,Y_test))
    print("cm of gnb: \n", cm_gnb)

    # Naive bayes bernoulli
    bnb = BernoulliNB()
    bnb.fit(X_train, Y_train)
    pred_bnb = bnb.predict(X_test)
    cm_bnb = confusion_matrix(Y_test, pred_bnb)
    # print("Score for bernoulli NB classifier: ", bnb.score(X_test,Y_test))
    print("cm of bnb: \n", cm_bnb)

    # SVM
    # svmc = svm.SVC()
    # svmc.fit(X_train, Y_train)
    # pred_svm = svmc.predict(X_test)
    # cm_svm = confusion_matrix(Y_test, pred_svm)
    # #print("Score for SVM classifier: ", svmc.score(X_test,Y_test))
    # print("cm of svm: \n", cm_svm)


def verifyUser():
    fs = 44100
    duration = 3

    engine.say("Speak gjai Jinendra when the recording starts!")
    print("speak Jai Jinendra when the recording starts")

    # wait = sd.rec(5, samplerate=fs, channels=1)
    # sd.wait()
    time.sleep(3)
    print("recording started")

    rec = sd.rec(int((duration * fs)), samplerate=fs, channels=1)

    sd.wait()

    print("recording stopped")

    file = "data\\history\\last_try.wav"
    write(filename=file, rate=fs, data=rec)

    mfcc = extract_mfcc(file, n_mfcc=40)

    input = pd.DataFrame(columns=range(0, 40))

    lst = list(mfcc)
    input.loc[len(input)] = lst

    df = pd.read_csv("data\\csv\\complete_data.csv")  # target variable is boolean : 1 means sahil, 0 means unknown

    Y = df["speaker"]
    X = df.drop(columns=["speaker", "Unnamed: 0"])

    # MLPClassifier
    classifier = MLPClassifier(solver='adam', alpha=0.001,
                               random_state=1, max_iter=500,
                               hidden_layer_sizes=100, activation="logistic")
    classifier.fit(X, Y)
    pred_mlp = classifier.predict(input)
    print("the MLP CLASSIFIER speaker is ", pred_mlp)

    # decision tree

    clf = DecisionTreeClassifier(random_state=1)
    clf.fit(X, Y)
    pred_tree = clf.predict(input)
    print("the DECISION TREE speaker is ", pred_tree)

    # random forest
    clf_forest = RandomForestClassifier(max_depth=100, random_state=1
                                        , n_estimators=75, criterion="entropy",
                                        max_features="auto")
    clf_forest.fit(X, Y)
    pred_rf = clf_forest.predict(input)
    print("the RANDOM FOREST speaker is: ", pred_rf)

    # K nearest neighbours classifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, Y)
    pred_knn = neigh.predict(input)
    print("the KNN speaker is : ", pred_knn)

    # Naive Bayes gaussian
    gnb = GaussianNB()
    gnb.fit(X, Y)
    pred_gnb = gnb.predict(input)
    print("the gaussian NB speaker is : ", pred_gnb)

    # Naive bayes bernoulli
    bnb = BernoulliNB()
    bnb.fit(X, Y)
    pred_bnb = bnb.predict(input)
    print("The bernoulli NB speaker is: ", pred_bnb)


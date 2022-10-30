import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
from random import choice
import os
import subprocess
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
import traceback
# from decouple import config

#setup voice engine of py text to speech
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

bot_name = "jarvis"
User_name = "Sahil"


#setup software paths to later launch them automatically
paths = {
    'notepad': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad",
    'opera': "C:\\Users\\Sahil Mukesh Jain\\AppData\\Local\\Programs\\Opera\\launcher.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'R studio': "C:\\Program Files\\RStudio\\bin\\rstudio.exe"
}

#Make lists of responses, bot will pick a random response in respective types (positive, negative, gratitude)
positive_response = ["Cool, I am on it sir!", " Okay sir, I'm working on it!", "Just a second sir!"]
negative_response = ["I think its invalid Command ", "My inventor didn't taught me this!",
                     "Sorry!, i don't know how to do this" ]
gratitude = ["I am happy to help!", "My pleasure sir!", "No problem!"]

email_id = "sahilmjain03@gmail.com"
password = "20sahil03@"






def speak(text):
    engine.say(text)
    engine.runAndWait()

#unauthorized method used in main.py
def unauthorized():
    speak("You are unauthorized")

#bot will start listening to you
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  #converts the command into english string

        #exit command to stop the execution of software.
        if 'exit' in query or 'stop' in query:
            hour = datetime.datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()


#if command not converted to english string, throw exception
    except Exception as e:
        traceback.print_exc()
        speak('Sorry, I could not understand. Could you please say that again?')
        query = take_command()
    return query


#like "ok google" is the key word to start executing google assistant, below text subparts are keywords to call
# respective methods
#function is used to take only commands, for general purpose inputs take_user_input() function is defined below.
def validate_command(query):
    if "text file" in query:
        speak(choice(positive_response))
        new_text_file()
    elif "R studio" in query:
        speak(choice(positive_response))
        open_rstudio()
    elif "command prompt" in query:
        speak(choice(positive_response))
        open_cmd()
    elif "calculator" in str.lower(query):
        speak(choice(positive_response))
        open_calculator()
    elif "notepad" in str.lower(query):
        speak(choice(positive_response))
        open_notepad()
    elif "opera" in str.lower(query):
        speak(choice(positive_response))
        open_opera()
    elif "send a WhatsApp message" in query:
        speak(choice(positive_response))
        send_whatsapp_message()
    elif "search on Wikipedia" in query:
        speak(choice(positive_response))
        search_on_wikipedia()
    elif "thank you" in query:
        speak(choice(gratitude)) #choice function selects random element from the array
    elif "email" in query:
        send_email()

    # if none of the above commands were present in the input, give a negative response to the user.
    else:
        speak(choice(negative_response))


def send_email():
    try:
        speak("Whom do you want to mail?, write correct mail id on console")
        receiver_address = input("Write mail id here: ")
        speak("What should be the subject?")
        subject = take_user_input() #take_user_input method is defined below
        speak("What should i write?")
        message = take_user_input()

        draft = EmailMessage()
        draft["To"] = receiver_address
        draft["subject"] = subject
        draft["From"] = email_id
        draft.set_content(message)

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(email_id, password)
        s.send_message(draft)
        s.close()
        speak("Email sent successfully")

    except Exception as e:
        speak("There was an error!")
        print(e)


#used to take general inputs required while execution.
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query

def search_on_wikipedia():
    speak("What do you want to search?")
    query = take_user_input()
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

def open_cmd():
    os.system('start cmd')

#paths to the below softwares are declared above
def open_rstudio():
    os.startfile(paths['R studio'])

def open_calculator():
    subprocess.Popen(paths['calculator'])

def open_notepad():
    os.startfile(paths['notepad'])

def open_opera():
    os.startfile(paths['opera'])

def new_text_file():
    # make new notepad file
    speak("What will be the name of the file? ")
    file_name = take_user_input()
    file = "C:\\Users\\Sahil Mukesh Jain\\desktop\\"+file_name + ".txt"
    f = open(file, "w+")
    speak("What do you want to write into the file")
    content = take_user_input()
    f.write(content)
    speak("New text file made with name " + file_name)
    f.close()

def send_whatsapp_message():
    speak("whom do you want to send? please enter on console")
    number = input("enter the number: ")
    speak("what do you want to send")
    message = take_user_input()
    kit.sendwhatmsg_instantly(f"+91{number}", message)

    file_name = take_user_input()
def greet():
    current_time = datetime.datetime.now().hour

    if 4 < current_time <= 12:
        #the greeting phrase is jai jinendra of jainism religion, but since the bot wasn't pronouncing it correct i
        # tried some permutations
        speak("gjai gjiinendraaa and Good morning " + User_name + "!")
    elif 12 < current_time <= 16:
        speak("gjai gjiinendraaa and Good afternoon " + User_name + "!")
    elif 16 < current_time <= 21:
        speak("gjai gjiinendraaa and Good evening " + User_name + "!")
    elif 21 < current_time < 23 or 0 <= current_time <= 4:
        speak("Its a late night " + User_name + "!")

    speak("What would you like to do ?")


if __name__ == "__main__":
    #if user is authorized then this file starts executing, 1st greet, then start listening to commands
    greet()
    #alike google assistant, it won't stop after taking one command but start listening again after finishing given task.
    #for that  purposes , while true:
    while True:
        query = take_command()
        print("You said \" " + query + " \"")
        validate_command(query)

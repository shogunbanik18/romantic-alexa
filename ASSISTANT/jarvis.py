# importing modules 
# pip install pyttsx3 
import pyttsx3
# pip install speech_recognition
import speech_recognition as sr  
import datetime
# pip install wikipedia 
import wikipedia
import webbrowser
import os
import smtplib

# installing the sapi5 
# sapi 5 is a speeach application programming interface from microsoft 
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices)
''' setting the property of voices
 getting vopice of david''' 
# engine.setProperty('voice', voices[1].id)
# print(voices[0].id)
# getting voice of Zira
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)
# Defining a function speak or input 
def speak(audio):
    # pass
    engine.say(audio)
    engine.runAndWait()


# definng a wishme function 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak(("Good Afternoon"))
    else:
        speak(("Good Evening sir "))

    speak("let me introduce myself ")
    speak("I am Jarvis Sir your personal assisstant , I am here to solve your problems")
    speak("Please Tell me How may I help You")

    # SENDING EMAIL FUNCTION 
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shogunbnaik09@gmail.com','jayabanik18')
    server.sendmail('shogunbanik09@gmail.com', to,content)
    server.close()

# Taking input from the user 
def takeCommand():
    '''it takes microphone input from the user and returns the string output'''
    r=sr.Recognizer()
    # for different microphones 
    with sr.Microphone(device_index=2) as source:
    # with sr.Microphone(device_index=1) as source:
    # with sr.Microphone(device_index=0) as source:
        # gap between speaking 
        print('Listening...')
        r.pause_threshold=1
        audio = r.listen(source)

    # may come error so we use try 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User Said : ",query)
        # speak("I am JARVIS your favourite personal Assistant ")
        # print(f"user said: {query}\n")

    except Exceptions as e:
        # print(e)

        print("Say that again Please....")
        return "None"
    return query

# Wrinting the main method 
if __name__ == "__main__":
    # speak("David is a good boy and he is also a very good human being")
    # function calling 
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    # logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open Instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open Stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
    # conditionals for playing music 
        elif 'play music' in query:
            music_dir ="D:\songs moto e 4 plus"
            songs =os.listdir(music_dir)
            print(songs)
            # speak("which song you wnat to hear sir")
            os.startfile(os.path.join(music_dir,songs[2]))

        elif 'LISTEN SONGS' in query:
            music_dir ="D:\songs moto e 4 plus"
            songs =os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

    # condition for speaking the time 
     
        elif "the time" in query:
            # TIME IN 12 HOUR FORMAT 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # speak("Sir,the time is : ",strTime)        
            print(f"Sir,the time is {strTime}")   
            speak(f"Sir,the time is {strTime}")  

        elif "vs code" in query:
            codePath ="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif "thank you" in query:
            speak("your welcome sir, It's my pleasure talking to you sir ")


        elif "alexa" in query:
            speak("Yes sir, She is my Girlfriend sir ")  

    # sending email 
    # dictionary can also be used
        elif "email " in query:
            try:
                speak("What should I say ? ")
                content =takeCommand() 
                to = "shogunbanik09@gmail.com"
                sendEmail(to,content)

            except Exception as e:
                print(e)
                speak("Sorry sir Iwas unable to send Email")

        elif 'quit' in query:
            speak("bye sir")
            exit()

        elif 'Bye' in query:
            speak("bye sir")
            exit()

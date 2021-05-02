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
import pywhatkit
import pyjokes

# installing the sapi5 
# sapi 5 is a speeach application programming interface from microsoft 
engine = pyttsx3.init('sapi5')

# installing voices 
voices =engine.getProperty('voices')
# print(voices)
''' setting the property of voices
 getting vopice of david''' 

engine.setProperty('voice', voices[1].id)
# print(voices[0].id)
# getting voice of Zira
# engine.setProperty('voice', voices[0].id)
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

def hello():
    speak("hello sir ,I am Alexa")
    speak("Please Tell me How may I help You")

def introduce():
    # speak("let me introduce myself ")
    speak("I am Alexa your personal assisstant , I am here to solve your problems")
    speak("I like listening to you ")
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
        query =r.recognize_google(audio,language='en-in')
        # query =r.recognize_google(audio,language='hi-in')
        print("User Said : ",query)
        print("\n")
        # speak("I am JARVIS your favourite personal Assistant ")
        # print(f"user said: {query}\n")

    except Exceptions as e:
        # print(e)
        # print("Say that again Please....")
        pass
        speak("Say that again Please....")
        return "None"
    return query

# Wrinting the main method 
if __name__ == "__main__":
    # speak("David is a good boy and he is also a very good human being")
    # function calling 
    # wishMe()
    hello()
    # introduce()
    while True:
    # if 1:
        query = takeCommand().lower()
        # query = takeCommand()
        # text =gt.Translator(query)
        # query =text.text
        # query =query.lower()
    # logic for executing tasks based on query
        # if 'alexa' in query :
        #     query =query.replace('alexa', '')
        #     print (query) 

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        # introducing alexa 
        elif 'yourself' in query:
            introduce()

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
            # print(songs)
            # speak("which song you wnat to hear sir")
            os.startfile(os.path.join(music_dir,songs[2]))

        elif 'play music' in query:
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

        elif "date" in query:
            speak("sorry,I have a headache")


        elif "know Jarvis" in query:
            speak("Yes sir, he is a my best friend ")

        elif "doing" in query:
            speak("I am talking to you sir ")

        elif "single" in query:
            speak("I am in a relationship with wifi")

        elif "hurts" in query :
            speak("I am sorry sir, i didn't mean to hurt")

        elif "heart" in query :
            speak("I am sorry sir, i didn't mean to break your heart")

        elif "angry" in query:
            speak("sorry sir , i did'nt mean to break your heart ")

        elif "siri" in query:
            speak("I am flattered to be called siri , iam not siri sir , she is a good friend of mine ")

        elif "audible" in query:
            speak("yes sir, i can listen you")

        elif "wake up" in query:
            speak("hello sir, how can i help you")

        elif "Google" in query:
            speak("Yes sir, she is a my best friend ")  

    # sending email 
    # dictionary can also be used
        elif "email " in query:
            try:
                speak("What should I say ? ")
                content =takeCommand() 
                to = "shogunbanik09@gmail.com"
                sendEmail(to,content)

            except Exception as e:
                # print(e)
                speak("Sorry sir I was unable to send Email")

        elif 'exit' in query:
            speak("Have a good day sir")
            exit()

        elif 'great' in query:
            speak("Thank you sir, how can i help you ")
    # ending statement 
        elif 'goodbye' in query:
            speak("see you soon sir,have a good day")
            exit()

        elif 'good bye' in query:
            speak("see you soon sir,have a good day")
            exit()

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        else:
            speak("unable to recognize you sir ,please say that again ")

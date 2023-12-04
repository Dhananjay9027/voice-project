import wikipedia
import turtle 
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')   #API of microsoft for speeches
voices=engine.getProperty('voices') 
#print(voices[0].id) to print name of voices avalilabale
engine.setProperty('voice',voices[0].id)   

def speak(audio):   #speak function 
    engine.say(audio)
    engine.runAndWait()


hour=int(datetime.datetime.now().hour) #current hour
min=int(datetime.datetime.now().minute) #current min\


def wish(): #greet
    if hour>=0 and hour<12:
        speak("Good morning  I am jarvis your assistant ")
    elif hour>=12 and hour<=15:
        speak("Good Afternoon  I am jarvis your assistant ")
    elif hour>15 and hour<=18:
        speak("Good Evening  I am your jaris assistant ")
    else:
        speak("hello I am your jarvis assistant")


def speaktime(): #speak time
    speak(hour)
    speak("hour")
    speak(min)
    speak("minute")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query   #query has words that you speak


if __name__ == "__main__":
    wish()

    while True:
        query=takeCommand().lower()
        file=open("data.txt","r")
        for i in file:
            if i in query:
                speak("so rude.You are using offensive word kindly mind your language")


        #for wikipedia search
        if 'wikipedia' in query:
            speak("searching wikipedia ")
            query=query.replace('wikipedia',"")
            query=query.replace('search',"")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)


        elif 'who is' in query:
            speak("searching wikipedia ")
            query=query.replace('who is',"")
            query=query.replace('search',"")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        
        elif 'time' in query:
            speaktime()

        elif 'speak time' in query:
            speaktime()

        elif 'open google' in query :
            speak("opening google")
            webbrowser.open('www.google.com')
        
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open('https://open.spotify.com/collection/tracks')

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak(" to whom I have to send email")
                to = takeCommand()
                print(to)  
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.I am not able to send this email")

        elif 'what is your name' in query:
            speak("In the memories of tony stark's jarvis I am his prototype in beta version. ")    

        elif 'copy me' in query:
            query=query.replace('copy me','')
            speak(query)


        elif 'speak with me' in query:
            query=query.replace('speak with me','')
            speak(query)

        elif 'song' in query:
            speak('which song do you want to listen')
            s=takeCommand()
            t=str('https://open.spotify.com/search/'+s)
            speak("playing song")
            webbrowser.open(t)

        elif 'whatsapp' in query:
            speak("opening whatsapp")
            p="C:\\Users\\dhana\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(p)
        
        elif 'offensive word' in query:
            speak("teach me an offensive word I will recognize it")
            file=open("data.txt","a")
            speak('speak the offensive or abusive word')
            s=takeCommand()
            file.write(s)

        #for user and things
        elif 'user data' in query:
            file=open('user.txt',"r")
            speak("according to the database....User information is")
            for i in file:
                if i==0:
                    speak("name of user is ")
                    speak(i)
                elif i==1:
                    speak("age of user is ")
                    speak(i)
                elif i==2:
                    speak(" the blood group is")
                    speak(i)
                else:
                    speak(i)
            speak('is this information is correct')
            s=takeCommand()
            if 'yes' in s:
                speak('okay good to know')
            elif 'no' in s:
                speak("speak the name of user")
                t=takeCommand()
                a={'name':t}
                speak("speak your age")
                p=takeCommand()
                a['age']=p
                speak('speak your blood group')
                o=takeCommand()
                a['gp']=o
                f=open('data.txt','a')
                f.write(a['name'])
                f.write(a['age'])
                f.write(a['gp'])
                speak("the data base is updated")
                print("The data base is updated................")



        
        else:
            speak("sorry can you say that again")


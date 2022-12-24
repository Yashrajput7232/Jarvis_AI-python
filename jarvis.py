import pyttsx3
import datetime
import speech_recognition  as sr
import wikipedia
import webbrowser
import smtplib
import os
engeine=pyttsx3.init('sapi5')
voices=engeine.getProperty('voices')
engeine.setProperty('voice',voices[0].id)


def speak(audio):
    engeine.say(audio)
    engeine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour);
    s=str(hour)
    # speak(s)
    if hour>0 and hour<=12:
        speak('Goodmorning')
    elif hour >12 and  hour<16:
        speak("good Afternoon")
    else:
        speak("good evening")
    speak(" i am  jarvis  how may i  help you ")
def TakeCommand():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak I am Listening......')
        # c.pause_threshold=1/
        audio=c.listen(source)
    try:
        print("Recognizing.......")
        query=c.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Above error occured Please speak again")
        return "NONE"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yash7232@outlook.com', '*********')
    server.sendmail('yash7232@outlook.com', to, content)
    server.close()

    



if __name__=='__main__': 
    # speak("yash is a good boy")

    # wishme()
    sendEmail(to = "yash.7232.rajput@gmail.com",content='this is sytem generated email')
    while True:
        query=TakeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia');
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=5)
            print(result)
            speak(result)
        elif 'open google ' in query:
            webbrowser.open("www.google.com")
    # TakeCommand()
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\yash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                to = "yash.7232.rajput@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry !! I am not able to send this email") 
            
        
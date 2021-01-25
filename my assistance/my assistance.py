import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import pyjokes


listener = sr. Recognizer()
engine = pyttsx3.init()

# this code is to change voice to female voice
# voice = engine.getProperty('voices')
# engine.setProperty('voice', voice[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# this is function that intializes our program
def take_command():
    try:
        with sr.Microphone() as source:
            print("lestening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey drake' in command:
                command =command.replace('hey drake','')
                print(command)
                # talk(command)
            else:
                talk("shut up my name is drake ")


    except:
        print("pass occur probmlem in py audio ")
        print(" lower ur python version to 3.6 or")
        print('''#pip install pipwin
                #then
                #pipwin install pyaudio''')
        pass
    return command


#main folder in which all work is assign
def run_drake():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'google' in command:
        searcher =command.replace('google', '')
        info = wikipedia.summary(searcher, 2)
        print(info)
        talk('going to check on wikipedia')
        try:
            # time.sleep(1)
            engine.runAndWait()
        except:
         talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        talk('hahahahahahah a hahahaha  a hahahahah a hahahahaha')




run_drake()
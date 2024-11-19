import speech_recognition as sr 
import pyttsx3
import pyjokes 
import datetime
import pyaudio
import wikipedia as wiki
import pywhatkit as pymus

# create a recognizer object
recognizer = sr.Recognizer()

#initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for male voice and 1 for female voice

#setup greeting and goodbye messages
hello = "Hello Kai, How can I be of assistance today?"
goodbye = "See you later, Kai!"
action = ''
engine.say(hello)
engine.runAndWait()

# create new function 
def google_api():
    try:
        # capture audio from default microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

            # perform speech recognition
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print("recognized text: ", text)
    except sr.UnknownValueError:
            print("Unable to understand your speech")
            text = "Speech Error!"

    return text

def interactions():
    text =  google_api()

    if "joke" in text:
        joke = pyjokes.get_joke()
        engine.say(joke)
        engine.runAndWait()

    elif "date" in text:
        currentDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
        engine.say("Today is " + currentDate)
        engine.runAndWait()

    elif "who is" in text:
        user = text.replace("who is", "")
        wiki_sum = wiki.summary(user, sentences=2)
        engine.say(wiki_sum)
        engine.runAndWait()

    elif "play" in text:
        song = text.replace("play", "")
        engine.say("Playing" + song)
        engine.runAndWait()
        pymus.playonyt(song)
        text = 'quit'

    return text


while action != 'quit':
    action  = interactions()
else: 
    engine.say(action)
    engine.runAndWait()



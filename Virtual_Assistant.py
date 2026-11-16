import pyttsx3
import pyttsx3
import pyjokes
import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr
import pyaudio

# create a recognizer object
recognizer = sr.Recognizer()

#initialize the speech engine
def speak(text_to_speak):
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[0].id) # 0 for male voice and 1 for female voice
    tts_engine.say(text_to_speak)
    tts_engine.runAndWait()
    tts_engine.stop()

#setup greeting and goodbye messages
hello = "Hello Kai, How can I be of assistance today?"
goodbye = "See you later, Kai!"
action = ''
speak(hello)

# create new function 
def google_api():
    try:
        # capture audio from default microphone
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognizer.pause_threshold = 1.0
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            # perform speech recognition
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print("Recognized Text: ", text)
    except sr.UnknownValueError:
            print("Unable to understand your speech")
            text = "Speech Error!"
    except sr.WaitTimeoutError:
            print("Listening timed out, no speech detected")
            text = "Speech Error!"
    except sr.RequestError as e:
            print("Could not request results from the speech service; {0}".format(e))
            text = "Speech Error!"
    except Exception as e:
            print("Unexpected error: ", e)
            text = "Speech Error!"

    return text

def interactions():
    text =  google_api()

    if "joke" in text:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "date" in text or "day" in text:
        currentDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today is " + currentDate)

    elif "who is" in text:
        user = text.replace("who is", "")
        wiki_sum = wikipedia.summary(user, sentences=2)
        speak(wiki_sum)

    elif "play" in text:
        song = text.replace("play", "")
        speak("Playing" + song)
        pywhatkit.playonyt(song)
        return 'quit'

    elif "quit" in text or "stop" in text or "goodbye" in text:
        return 'quit'

    elif text == "Speech Error!":
        # didn't catch anything usable, just listen again silently
        pass

    else:
        speak("Sorry, I didn't catch that. Can you repeat?")

    return text


while action != 'quit':
    action  = interactions()
else: 
    speak(goodbye)


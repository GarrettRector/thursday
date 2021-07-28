import configparser
import http.client
import requests
import speech_recognition
from gtts import gTTS
import os
from playsound import playsound
from jproperties import Properties
from time import localtime, strftime
configs = Properties()

# init speech recognition
recognize = speech_recognition.Recognizer()


def listen(recognizer):
    tts = None
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(f"You > {tts}")
    # exception handling for tts errors
    except speech_recognition.UnknownValueError:
        texttospeech("valerr")
        return None
    except speech_recognition.RequestError:
        texttospeech("down")
        return None
    except http.client.IncompleteRead:
        texttospeech("inc")
        return None
    return tts


def texttospeech(name):
    path = f"tts/{name}.mp3"
    playsound(os.path.abspath(path), True)


def ttsgen(texts):
    fil = gTTS(text=texts, lang="en", slow=False)
    fil.save(f"response.mp3")
    playsound(f"response.mp3")
    os.remove(f"response.mp3")


# main function
while True:
    listener = listen(recognize)
    if listener is not None:
        if "shutdown" in listener.lower():
            ttsgen("Goodbye")
            exit()
        if "time is it" in listener.lower():
            time = "%H:%M"
            time = f"{strftime(time, localtime())}"
            print(f"thursday > {time}")
            ttsgen(time)
        else:
            config = configparser.ConfigParser()
            config.read('config.properties')
            r = requests.post(config.get("address", "address"), listener)
            response = r.text
            if response != "":
                print(f"thursday > {response}")
                ttsgen(response)
            else:
                text = "Sorry, my AI response server is offline right now. Please try again later"
                ttsgen(text)
                exit()

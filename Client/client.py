import configparser
import http.client
import time
import requests
import speech_recognition
from gtts import gTTS
import os
from playsound import playsound
from jproperties import Properties
configs = Properties()

# init speech recognition
recognize = speech_recognition.Recognizer()


def listen(recognizer):
    tts = ""
    def texttospeech(name): playsound(f"{name}.mp3")
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(tts)
    # exception handling for tts errors
    except speech_recognition.UnknownValueError:
        texttospeech("valerr")
    except speech_recognition.RequestError:
        texttospeech("down")
    except http.client.IncompleteRead:
        texttospeech("inc")
    return tts


def ttsgen(texts):
    fil = gTTS(text=texts, lang="en", slow=False)
    fil.save(f"response.mp3")
    playsound(f"response.mp3")
    time.sleep(len(response) * 0.7)
    os.remove(f"response.mp3")


# main function
while True:
    listener = listen(recognize)
    if listener is not None:
        config = configparser.ConfigParser()
        config.read('config.properties')
        r = requests.post(config.get("address", "address"), listener)
        response = r.text
        if response != "":
            print(response)
            ttsgen(response)
        else:
            text = "Sorry, my AI response server is offline right now. Please try again later"
            ttsgen(text)
            exit()

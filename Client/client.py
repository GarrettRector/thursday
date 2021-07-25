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
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(tts)
    # exception handling for tts errors
    except speech_recognition.UnknownValueError:
        err = "Sorry, I didn't get that. Could you try again?"
        texttospeech("valerr")
    except speech_recognition.RequestError:
        err = "Sorry, my speech service is down."
        texttospeech("down")
    except http.client.IncompleteRead:
        err = "an error has occured"
        texttospeech("inc")
    return tts


def texttospeech(name):
    playsound(f"{name}.mp3")


# main function
while True:
    listener = listen(recognize)
    if listener is not None:
        config = configparser.ConfigParser()
        config.read('config.properties')
        r = requests.post(config.get("address", "address"), listener)
        response = r.text
        print(response)
        files = gTTS(text=response, lang="en", slow=False)
        files.save(f"response.mp3")
        playsound(f"response.mp3")
        time.sleep(len(response) * 0.7)
        os.remove(f"response.mp3")

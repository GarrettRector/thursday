import http.client
import time
import requests
import speech_recognition
from gtts import gTTS
import os
from playsound import playsound

# init chatterbot
recognize = speech_recognition.Recognizer()


def listen(recognizer):
    tts = ""
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(tts)
    except speech_recognition.UnknownValueError:
        err = "Sorry, I didn't get that. Could you try again?"
        texttospeech(err, "valerr")
    except speech_recognition.RequestError:
        err = "Sorry, my speech service is down."
        texttospeech(err, "down")
    except http.client.IncompleteRead:
        err = "an error has occured"
        texttospeech(err, "inc")
    return tts


def texttospeech(text, name):
    print(text)
    files = gTTS(text=text, lang="en", slow=False)
    files.save(f"{name}.mp3")
    playsound(f"{name}.mp3")
    time.sleep(len(text) * 0.7)
    os.remove(f"{name}.mp3")


while True:
    listener = listen(recognize)
    if "hello" in listener.lower():
        r = requests.post("http://127.0.0.1:5000/", listener)
        response = r.text
        print(response)
        language = 'en'
        file = gTTS(text=response, lang=language, slow=False)
        file.save("tts.mp3")
        playsound("tts.mp3")
        time.sleep(len(response)*0.7)
        os.remove("tts.mp3")

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
    check = False
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(f"You > {tts}")
            check = True
    # exception handling for tts errors
    except speech_recognition.UnknownValueError:
        texttospeech("valerr", 0)
    except speech_recognition.RequestError:
        texttospeech("down", 0)
    except http.client.IncompleteRead:
        texttospeech("inc", 0)
    return tts if check else None


def texttospeech(text, types):
    match types:
        case 1:
            path = f"tts/{text}.mp3"
            playsound(os.path.abspath(path), True)
        case 0:
            fil = gTTS(text=text, lang="en", slow=False)
            fil.save(f"response.mp3")
            playsound(f"response.mp3")
            os.remove(f"response.mp3")


def request(listener):
    config = configparser.ConfigParser()
    config.read('config.properties')
    r = requests.post(config.get("address", "address"), listener)
    response = r.text
    match response:
        case "":
            texttospeech("Sorry, my AI response server is offline right now. Please try again later", 1)
            exit()
        case "KEYERR":
            print("Key is invalid")
            texttospeech("Key is invalid", 1)


# main function
def main():
    listener = listen(recognize)
    if listener is not None:
        if "shutdown" in listener:
            texttospeech("Goodbye", 1)
            exit()
        elif "time" in listener:
            time = "%H:%M"
            time = f"{strftime(time, localtime())}"
            print(f"thursday > {time}")
            texttospeech(time, 1)
        else:
            request(listener)


if __name__ == "__main__":
    main()

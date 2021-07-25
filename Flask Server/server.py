import speech_recognition
from chatterbot import ChatBot
import nltk
nltk.download('punkt')

recognize = speech_recognition.Recognizer()
bot = ChatBot("")


def listen(recognizer):
    tts = ""
    try:
        with speech_recognition.Microphone() as mic:
            audio = recognizer.listen(mic)
            tts = recognizer.recognize_google(audio)
            print(tts)
    except speech_recognition.UnknownValueError:
        print("Sorry, I didn't get that. Could you try again?")
    except speech_recognition.RequestError:
        print("Sorry, my speech service is down.")
    return tts


while True:
    listener = listen(recognize)
    if "friday" in listener.lower():
        print(listener)
        try:
            bot_input = bot.get_response(listener)
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            print("err")
            break

import pyaudio
import speech_recognition as sr
import os
from playsound import playsound as ps


def main():
    r = sr.Recognizer()
    greetings = ["test", "hello", "hi"]
    commands = ["launch", "open", "activate", "search"]

    with sr.Microphone() as source:
        ps("audio.mp3")
        print("Say something!")
        audio = r.listen(source, timeout=5)

    try:
        text = r.recognize_google(audio).split()
        command = text[0].strip()
        if not command in commands and command not in greetings:
            print(text[0] + " is not a command")

        if command == "launch":
            application = text[1]
            print(application)
            if application[0].lower().strip() in ["google", "chrome"]:
                chrome_launch()

        if command in greetings:
            print("Hey there, my name is Pylot, how can I help?")    




    #bad audio
    except sr.UnknownValueError:
        print("Pyrsonal Assistant could not understand audio")
    #req error
    except sr.RequestError as e:
        print("Error; {0}".format(e))

    def chrome_launch():
        print("Launching Chrome...")
        os.system("google-chrome")

if __name__ == "__main__":
    main()
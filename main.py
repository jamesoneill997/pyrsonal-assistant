import pyaudio
import speech_recognition as sr
import os
from playsound import playsound as ps
from gtts import gTTS
from functionality.chrome_launch import chrome_launch
from functionality.open_page import open_page
import subprocess

def main():
    #copy parent vars
    my_env = os.environ.copy()
    #google speech rec module
    r = sr.Recognizer()

    #greetings and commands
    english_greetings = ["test", "hello", "hi", "good morning", "good afternoon", "hey", "hey pylot", "hey pilot"]
    fr_greetings  = ["salut", "bonjour", "bonsoir", "bon matin"]
    commands = ["launch", "open", "activate", "search", "call", "ring"]

    #mic in
    with sr.Microphone() as source:
        ps("audio/audio.mp3")
        print("Say something!")
        audio = r.listen(source, timeout=5)
        
    #process input
    try:
        text = r.recognize_google(audio).split()
        command = text[0].strip()
        if command == "no":
            ps("./audio/exit.mp3")
            return
        elif command == "change language":
            ps("audio/change_lang.mp3")

        if not command in commands and command not in english_greetings:
            print(text[0] + " is not a command")

        #used to launch applications
        if command == "launch":
            application = text[1].lower().strip()
            if application in ["google", "chrome"]:
                chrome_launch()
                ps("./audio/launch.mp3")
                ps("./audio/nextCommand.mp3")
                main()
            elif application in ["vs code", "code", "visual studio"]:
                os.system("code")
                ps("./audio/nextCommand.mp3")
                main()

        elif command == "open":
            ps("./audio/launch.mp3")
            open_page(text[1])
            ps("./audio/nextCommand.mp3")
            main()
                    
        #greeting
        elif command in english_greetings:
            ps("./audio/greeting.mp3")
            main()

        elif command == "call" or command == "ring":
            ps("./audio/call.mp3")
            subprocess.call(['/bin/bash', '-i', '-c', "findPhone"])
            ps("./audio/nextCommand.mp3")
            main()


        elif command == "search":
            print("Hello")
            ps("./audio/nextCommand.mp3")
            main()
            

    #bad audio
    except sr.UnknownValueError:
        ps("./audio/noUnderstand.mp3")
        main()

    #req error
    except sr.RequestError as e:
        ps("./audio/requestErr.mp3")
    

if __name__ == "__main__":
    main()
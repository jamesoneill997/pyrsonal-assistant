import pyaudio
import speech_recognition as sr
import os
from playsound import playsound as ps
from gtts import gTTS
from functionality.chrome_launch import chrome_launch
import subprocess

def main():
    my_env = os.environ.copy()
    r = sr.Recognizer()
    greetings = ["test", "hello", "hi", "good morning", "good afternoon", "hey", "hey pylot", "hey pilot"]
    commands = ["launch", "open", "activate", "search", "call", "ring"]

    with sr.Microphone() as source:
        ps("audio/audio.mp3")
        print("Say something!")
        audio = r.listen(source, timeout=5)
        

    try:
        text = r.recognize_google(audio).split()
        command = text[0].strip()
        if not command in commands and command not in greetings:
            print(text[0] + " is not a command")

        #used to launch applications
        if command == "launch":
            application = text[1].lower().strip()
            if application in ["google", "chrome"]:
                chrome_launch()
                ps("./audio/launch.mp3")
                ps("./audio/nextCommand.mp3")
                main()
                    
        #greeting
        elif command in greetings:
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
        output = "Error; {0}".format(e)
        ps("./audio/requestErr.mp3")
    

if __name__ == "__main__":
    main()
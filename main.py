import pyaudio
import speech_recognition as sr
import os


def main():
    r = sr.Recognizer()
    commands = ["launch", "open", "activate"]

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).split()
        command = text[0]
        if not command in commands:
            print(text[0] + " is not a command")

        if command == "launch":
            application = [text[i]+ " " for i in range(1,len(text))]
            print(application)
            if application[0].lower().strip() in ["google", "chrome"]:
                print("Launching Chrome...")
                os.system("google-chrome")




    #bad audio
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    #req error
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

if __name__ == "__main__":
    main()
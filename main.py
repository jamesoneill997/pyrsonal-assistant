import pyaudio
import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print(r.recognize_sphinx(audio))
    #bad audio
    except sr.UnknownValueError:=
        print("Sphinx could not understand audio")
    #req error
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

if __name__ == "__main__":
    main()
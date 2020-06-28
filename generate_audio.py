from gtts import gTTS
import os

files = ["call"]

for i in range(len(files)):
    file = open("script/{}.txt".format(files[i]), "r").read()
    speech = gTTS(text = str(file),lang='en',slow = False)
    speech.save("./audio/{}.mp3".format(files[i]))
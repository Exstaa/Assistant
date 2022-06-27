import speech_recognition as sr
import keyboard
import os
import pyttsx3
import webbrowser

mic = sr.Recognizer()
talker = pyttsx3.init()
talker.say("Hello How Are You?")
with sr.Microphone() as source:
    print("say smth")
    audio = mic.listen(source)
voice_data = mic.recognize_google(audio)
if 'Open Browser' in voice_data:
    import os
    import pyttsx3
os.startfile('msedge.exe')
webbrowser.open('http://hangouts.google.com', new=2)
webbrowser.open('http://youtube.com', new=3)
webbrowser.open('https://web.whatsapp-.com', new=4)
talker = pyttsx3.init()
talker.say("Microsoft Edge Opened Sucsesfully")
talker.say("You Are Welcome")
print("Forwardded Sucsesfully")
talker.runAndWait()

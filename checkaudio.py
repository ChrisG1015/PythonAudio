import speech_recognition as sr
import sys 

#Logs output of audio to a text file
stdoutOrigin=sys.stdout 
sys.stdout = open("audiolog.txt", "w")

r = sr.Recognizer()

incomingaudio = sr.AudioFile('OSR_us_000_0032_8k.wav')
with incomingaudio as source:
    audio = r.record(source)

#print(type(audio))
#print("-------------------")
#print("\n")
#print("-------------------")
#print("\n")
print(r.recognize_google(audio))
#print("-------------------")
#print("\n")
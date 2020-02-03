import speech_recognition as sr
import sys 

#Logs output of audio to a text file
stdoutOrigin=sys.stdout 
sys.stdout = open("audiolog.txt", "w")

# use sr recognizer (easy to use, basic)
r = sr.Recognizer()

#functiong to process incoming audio
incomingaudio = sr.AudioFile('OSR_us_000_0032_8k.wav')
with incomingaudio as source:
    audio = r.record(source)

# use the google_speech api via the speech_recognition wrapper to process the audio speech 
print(r.recognize_google(audio))





#print(type(audio))
#print("-------------------")
#print("\n")
#print("-------------------")
#print("\n")
#print("-------------------")
#print("\n")
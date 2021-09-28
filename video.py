import speech_recognition as sr
from moviepy.editor import *
import os

video = VideoFileClip("speech.mp4")
video.audio.write_audiofile("speech.wav")

r = sr.Recognizer()
with sr.AudioFile("speech.wav") as source:
    audio = r.listen(source)
    print("Audio file is converting")
    try:
        text = r.recognize_google(audio)
        print("Converting audio to text")
        print("File is converted and saving the file in text file")
        file1 = open(r"C:\Users\KRISH\Desktop\output\videoconverted.txt", "a")
        file1.writelines(text)
        print("Conversion Finished")
        file1.close()
    except Exception as e:
        print(e)
import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile('SteveJobsSpeech_2min.wav') as source:
    audio = r.listen(source)
    print("We are processing the Audio please wait........")
    try:
        text = r.recognize_google(audio)
        print("Converting audio to text")
        print("File is converted and saving the file in text file")
        file1 = open(r"C:\Users\KRISH\Desktop\output\audioconverted.txt", "a")
        file1.writelines(text)
    except:
        print('Sorry.. run again...')

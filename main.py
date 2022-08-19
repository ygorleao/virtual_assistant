import speech_recognition as sr 

# Obtain audio from the microphone
r = sr.Recognizer()

# Get the default microfone
with sr.Microphone() as source:

    while True:
        audio = r.listen(source)

        google = r.recognize_google(audio, language="pt-br")
        sphinx = r.recognize_sphinx(audio)

        print(f"GOOGLE SAYS: {google}\nSPHINX SAYS: {sphinx}")
        
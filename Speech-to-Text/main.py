"""
pip install SpeechRecognition
"""
import speech_recognition as sr


def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=3)  # Listen for up to 3 seconds

    print('done')

    text = r.recognize_google(audio)
    print('Recognized text:', text)


if __name__ == '__main__':
    get()

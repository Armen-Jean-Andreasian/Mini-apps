"""
pip install pyttsx3
"""

import pyttsx3

engine = pyttsx3.init()


def say(text: str):
    engine.say(text)
    engine.runAndWait()


say('Marcel')
say('meow')

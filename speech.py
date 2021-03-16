import pyttsx3

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speakMsg(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
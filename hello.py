import pyttsx3
engine = pyttsx3.init()  # object creation
# & Volume
# getting to know current volume level (min=0 and max=1)
volume = engine.getProperty('volume')
# print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)
# & Voices
voices = engine.getProperty('voices')  # getting details of current voice
# changing index, changes voices. o for male
# engine.setProperty('voice', voices[0].id)
# changing index, changes voices. 1 for female
engine.setProperty('voice', voices[1].id)


def talk(talk):
    engine.say(talk)
    engine.runAndWait()


talk("hi Ashish")
# talk("I love you")

# engine.say("Hello World")

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# # engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
engine.stop()

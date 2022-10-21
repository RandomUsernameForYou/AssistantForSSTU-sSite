import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150) #Voice speed
engine.setProperty('volume', 0.9) #Volume level

engine.say('Привет, меня зовут рафаэль')
engine.runAndWait() #Clearing queue and text playback
import speech_recognition

class Assistant:
    def __init__(self):
        self.sr = speech_recognition.Recognizer()
        self.sr.pause_threshold = 0.5
        self.commands_dict = {
            'commands': {
                'greeting': ['хай', 'прифки', 'привет'],
                'get_answer': ['как дела', 'че как сам']
            }
        }
    def listening(self):
        '''The method return recognized command'''
        try:
            with speech_recognition.Microphone() as mic:
                self.sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = self.sr.listen(source=mic)
                query = self.sr.recognize_google(audio_data=audio, language='ru-RU').lower()

            return query
        except speech_recognition.UnknownValueError:
            return 'Сообщение не распознано!!!'
    def greeting(self):
        '''This method greet user'''
        return 'Привет'
    def get_answer(self):
        return 'нормально, у тебя как?'
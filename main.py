import time
import warnings

import speech_recognition as sr

import module as md

warnings.filterwarnings("ignore")


def listen_speak():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    r.dynamic_energy_threshold = True

    with sr.Microphone(sample_rate=16000, chunk_size=512) as source:
        print('Bang Eric mau nanya apa?')
        say = 'Bang Eric mau nanya apa?'
        md.jarvis(say)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            message = r.recognize_google(audio, language='id', show_all=False)
            print("You said: " + message)
            response = md.generate(prompt=message)
            say = response
            print("ZiyonGPT: " + say)
            md.jarvis(text=say)
        except:
            print("Please Repeat")
            time.sleep(1)


if __name__ == '__main__':
    while True:
        listen_speak()

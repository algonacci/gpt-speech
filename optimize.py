import time
import threading
import warnings

import speech_recognition as sr

import module as md

warnings.filterwarnings("ignore")

def listen():
    r = sr.Recognizer()

    with sr.Microphone(sample_rate=16000, chunk_size=512) as source:
        print('Bang Eric mau nanya apa?')
        md.jarvis('Bang Eric mau nanya apa?')

        r.energy_threshold = 4000

        while True:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

            try:
                message = r.recognize_google(audio, language='id', show_all=False)
                print("You said: " + message)

                if message.strip():
                    response = md.generate(prompt=message)
                    say = response
                    print("ZiyonGPT: " + say)

                    threading.Thread(target=md.jarvis, args=(say,)).start()
                    time.sleep(0.5)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")


if __name__ == '__main__':
    listen()

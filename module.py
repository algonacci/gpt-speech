import os

import openai
from dotenv import dotenv_values
from gtts import gTTS
from playsound import playsound

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

audio_file = "jarvis_record.mp3"


def jarvis(text):
    myobj = gTTS(text=text, lang='id', slow=False)
    myobj.save(audio_file)
    playsound('jarvis_record.mp3')
    os.remove(audio_file)


def generate(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        n=1,
        stop=None,
        timeout=15
    )
    return response.choices[0].text.strip()

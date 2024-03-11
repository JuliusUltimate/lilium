import torch
import numpy
import pyaudio  
import wave
import os
import platform
import random
from TTS.api import TTS

##-----------------------------Initialize Data---------------------------------

scriptDir = os.path.dirname(os.path.realpath(__file__)) # Script working dir
tempFolder = os.path.join(scriptDir, r"temp_output") # Temp folder path (where the audio is stored before getting played)
output = f"{tempFolder}\out_temp.wav" # file output (with name)

noises_dir = os.path.join(scriptDir, r"predefined")

model_path = os.path.join(scriptDir, r"finetunes") # Fintuned model path
config_path = os.path.join(scriptDir, r"finetunes", r"config.json") # Model configuration path file
voice_reference = os.path.join(scriptDir, r"voices", r"catgirl", r"catgirl.wav") # Speaker reference (catgirl)

noises_sounds = []

# Taking each file in the pre defined dir
for w in os.listdir(noises_dir):
    basedir = os.path.join(noises_dir, w) #Full path
    noises_sounds.append(basedir) # Adding to the list

print(noises_sounds)

##-----------------------------Main Function---------------------------------

class PlaySound:

    def play(sound): # Playing sound with pyaudio (literally copy pasted code)
        chunk = 1024
        file = wave.open(sound, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                        channels = file.getnchannels(),
                        rate = file.getframerate(),
                        output = True)
        data = file.readframes(chunk)
        while True:
            if data != '':
                stream.write(data)
                data = file.readframes(chunk)

            if data == b'':
                break

player = PlaySound()


def speak(world):

    while world['power state']:

        if world['main state'] == 'awake':
            print("custom wake up")

        if world['main state'] == 'talk': # I'm out of idea

            def speak(text):

                sound = random.choice(noises_sounds)

                uwu_text = text.replace('l', 'w').replace('r', 'w') # Changing the text into uwu language
                tts = TTS(model_path=model_path, config_path=config_path) #gpu=False
                tts.tts_to_file(uwu_text, file_path=f"{output}", language="en", speaker_wav=[voice_reference]) #for single / short sentences : split_sentences=False

                player.play(sound) #skill issue tbh

            


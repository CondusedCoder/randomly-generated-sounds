import os
import math
import wave
import struct
import random


os.chdir("D:/Coding Files/python projects/random sounds")
audio = []

sample_rate = 44100.0

def append_silence(duration_milliseconds):
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(0.0)


def append_sinewav(freq, duration_milliseconds, volume):
    global audio

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2* math.pi * freq * (x / sample_rate)))

def save_wav(file_name):
    wav_file=wave.open(file_name, "w")
    nchannels = 1
    sampwidth = 2

    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack("h", int(sample * 32767.0)))

    wav_file.close()

def create_random_sound():
    min_freq = 0
    max_freq = 1000
    random_freq = random.randrange(min_freq, max_freq)
    
    append_sinewav(random_freq, 1000, 1.0)

for i in range(10):
    create_random_sound()

    append_silence(1000)

save_wav("sound.wav")
os.system("sound.wav")



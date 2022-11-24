from vosk import Model,KaldiRecognizer
import pyaudio
import json
model=Model("./vosk-model-en-in-0.5")
# C:\Users\ajink\Desktop\Lite Bytes\vosk-model-en-in-0.5
recognizer= KaldiRecognizer(model,16000)

mic= pyaudio.PyAudio()
stream= mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True,frames_per_buffer=8192)
stream.start_stream()
 
# while True:
def talk():
    data= stream.read(4096)
    # if len(data)==0:
    #     break
    if recognizer.AcceptWaveform(data):
        result=recognizer.Result()
        text = json.loads(result)["text"]
        print(text)
        return text
talk()
  

from django.shortcuts import render
import azure.cognitiveservices.speech as speechsdk
import playsound
from playsound import playsound
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription="938a984b703e43c8b85e1718707bb7f1", region="eastus")
    speech_config.speech_recognition_language="en-US"

    #To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
    #audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        sentence =speech_recognition_result.text
        print(sentence)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

    sounds= ["lion",'cat','dog','rain','raining','windy','thunder','fox']
   
    tokens = nltk.word_tokenize(sentence)
    print(tokens)
    for i in tokens:
        for j in sounds:
            if i == j:
                print(j)
                txt=j + ".mp3"
                playsound(txt)

# Create your views here.
def home(request):
    return render(request, 'home.html', )

def start(request):
    recognize_from_microphone()
    return render(request, 'home.html', )

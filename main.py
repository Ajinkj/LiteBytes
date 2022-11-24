# import nlp
import final
import multiprocessing
# import threading
import playsound
from playsound import playsound
if __name__ == "__main__":
    while True:
        sounds= ["lion",'cat','dog','rain','raining','windy','Thunder','fox']
        text=final.recognize_from_microphone()
        # text="The lion was sad and thunder was happy"
        data=text.split(' ')
        print(data)
        for i in data:
            if i in sounds:
                txt=i + ".mp3"
                print(txt)
                # playsound(txt)
                p1 = multiprocessing.Process(target=playsound, args=(txt, ))
                p1.start()
                # t1 = threading.Thread(target=playsound, args=(txt,))
                # t1.start()

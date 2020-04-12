import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time


def talk():
    engine = pyttsx3.init() 

    r1= sr.Recognizer()
    r2= sr.Recognizer()
    r3= sr.Recognizer()

    with sr.Microphone() as source:
        engine.say("Choose one of the following: say test for Google or say dog for youtube")
        engine.runAndWait()
        
        print("Speak Now")
        audio=r3.listen(source)
    

    if 'dog' in r2.recognize_google(audio):
        r2= sr.Recognizer()
        # url="https://www.edureka.co/" 
        url="https://www.youtube.com/results?search_query="
        with sr.Microphone() as source:
            print("Search your query")
            audio = r2.listen(source)

            try:
                get= r2.recognize_google(audio)
                print(get)
                wb.get().open(url+get)
            except sr.UnknownValueError:
                print("error")
            except sr.RequestError as e:
                print("failed".format(e))
            except:
                print("Error")
    

talk()
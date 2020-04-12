import keyboard  # using module keyboard
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time


engine = pyttsx3.init() 
engine.setProperty('rate',150)
engine.setProperty('volume',1)

ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)



r1= sr.Recognizer()
r2= sr.Recognizer()
r3= sr.Recognizer()

count=0
flag=0
with sr.Microphone() as source:
    while True:
        if flag==1:
            break

        engine.say("Press A")
        engine.runAndWait()
        while True:
            count=count+1
            if keyboard.is_pressed('a'):  
                engine.say("Key A pressed Successfully")
                engine.runAndWait()
                flag=1
                break

            if(count==100000):
                count=0
                break



    



# if 'dog' in r2.recognize_google(audio):
#     r2= sr.Recognizer()
#     # url="https://www.edureka.co/" 
#     url="https://www.youtube.com/results?search_query="
#     with sr.Microphone() as source:
#         print("Search your query")
#         audio = r2.listen(source)
 
#         try:
#             get= r2.recognize_google(audio)
#             print(get)
#             wb.get().open(url+get)
#         except sr.UnknownValueError:
#             print("error")
#         except sr.RequestError as e:
#             print("failed".format(e))
#         except:
#             print("Error")



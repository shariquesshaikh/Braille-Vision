from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import keyboard
import time
import os
import string

app = Flask(__name__)

x=[]

letters = list(string.ascii_lowercase)

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

path1= 'E:\VSCodeProj\Brail'
y=os.path.join(path1,'templates\learn.html')

path2= 'E:\VSCodeProj\Brail'
w=os.path.join(path2,'templates\practice.html')

path3= 'E:\VSCodeProj\Brail'
z=os.path.join(path3,'templates\index.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    engine = pyttsx3.init() 
    engine.setProperty('rate',150)
    engine.setProperty('volume',1)
    engine.setProperty('voice', en_voice_id)
    flag=0

    wb.open(z,new=0)   
    
    while flag==0:
        count=0
        engine.say("Press first key to go to learning section")
        engine.runAndWait()

        engine.say("Press first, and, third, key to go to practice section")
        engine.runAndWait()

        while True:
            count=count+1
            if keyboard.is_pressed('a'):  
                engine.say("Directing to learning section")
                engine.runAndWait()
                return redirect('/learn')

            if keyboard.is_pressed('b'):  
                engine.say("Directing to practice section")
                engine.runAndWait()
                return redirect('/practice')

            if(count==50000):
                count=0
                break

lflag=0

@app.route('/learn', methods=['POST', 'GET'])
def learn():
    # wb.open(y,new=0) 
    global lflag

    if lflag==0:
        en = pyttsx3.init() 
        en.setProperty('rate',150)
        en.setProperty('volume',1)
        en.setProperty('voice', en_voice_id) 

        en.say("Press Enter key to start the learning process.")
        en.runAndWait() 
        lflag=1


    return render_template("learn.html")

@app.route('/pchecker', methods=['POST', 'GET'])
def learnc():

    if request.method == 'POST':
        value= request.form.get('val')
        en = pyttsx3.init() 
        en.setProperty('rate',150)
        en.setProperty('volume',1)
        en.setProperty('voice', en_voice_id)

        if value in x:
                en.say("You just press the key "+value+"You have successfully pressed it once. There is no need to press it again and again.")
                en.runAndWait()
                return redirect("/practice") 

        if (value=='a' or value=='A') : 
                en.say("Key A is pressed")
                x.append(value)
                en.runAndWait()
     
        
        elif value=='b' or value=='B':  
                en.say("Key B is pressed")
                x.append(value)
                en.runAndWait()
     
        elif value=='c' or value=='C':  
            en.say("Key C is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='d' or value=='D':  
            en.say("Key D is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='e' or value=='E':  
            en.say("Key E is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='f' or value=='F':  
            en.say("Key F is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='g' or value=='G':  
            en.say("Key G is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='h' or value=='H':  
            en.say("Key H is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='i' or value=='I':  
            en.say("Key I is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='j' or value=='J':  
            en.say("Key J is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='k' or value=='K':  
            en.say("Key H is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='l' or value=='L':  
            en.say("Key L is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='m' or value=='M':  
            en.say("Key M is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='n' or value=='N':  
            en.say("Key N is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='o' or value=='O':  
            en.say("Key O is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='p' or value=='P':  
            en.say("Key P is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='q' or value=='Q':  
            en.say("Key Q is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='r' or value=='R':  
            en.say("Key R is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='s' or value=='S':  
            en.say("Key S is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='t' or value=='T':  
            en.say("Key T is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='u' or value=='U':  
            en.say("Key U is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='V' or value=='v':  
            en.say("Key V is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='w' or value=='W':  
            en.say("Key W is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='x' or value=='X':  
            en.say("Key X is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='y' or value=='Y':  
            en.say("Key Y is pressed")
            x.append(value)
            en.runAndWait()
     
        elif value=='z' or value=='Z':  
            en.say("Key Z is pressed")
            x.append(value)
            en.runAndWait()
        elif value=='':
            en.say("You did not press anything")
            en.runAndWait()
        else:
            en.say("Pressed value is")
            en.say(value)
            en.runAndWait()
        
    return redirect('/practice')


@app.route('/practice', methods=['POST', 'GET'])
def practice():
    return render_template("practice.html")



@app.route('/lchecker', methods=['POST', 'GET'])
def practicec():
    engine = pyttsx3.init() 
    engine.setProperty('rate',150)
    engine.setProperty('volume',1)
    engine.setProperty('voice', en_voice_id)
    # wb.open(y,new=0)

    value=0

    if request.method == 'POST':
            value= request.form.get('val')
            
    if value=='a':  
            engine.say("Congratulations!")
            engine.say("You have learnt the pattern for key A")
            engine.runAndWait()
            value=0
        
        
    if value=='b':  
            engine.say("Congratulations!")
            engine.say("You have learnt the pattern for key B")
            engine.runAndWait()
            value=0

    engine.say("Press first key to enter A")
    engine.runAndWait()

    engine.say("Press first and third key to enter B")
    engine.runAndWait()
                


        # if flag==2:

        #     engine.say("Press first and third key to enter B")
        #     engine.runAndWait()

        #     while True:
        #         count=count+1
        #         if keyboard.is_pressed('a'):  
        #             engine.say("Congratulations!")
        #             engine.say("You have learnt the pattern for key A")
        #             engine.runAndWait()
        #             flag=3

        #         if(count==100000):
        #             count=0
        #             break    


    # engine.say("Press first and third key to enter B")
    # engine.say("Press first and second key to enter C")
    # engine.say("Press first,second and fourth key to enter D")
    # engine.say("Press first and fourth key to enter E")
    # engine.say("Press first,second and third key to enter F")
    # engine.say("Press first,second,third and fourth key to enter G")
    # engine.say("Press first,third and fourth key to enter H")
    # engine.say("Press second and third key to enter I")
    # engine.say("Press second,third and fourth key to enter J")
    # engine.say("Press first and fifth key to enter K")
    # engine.say("Press first,third and fifth key to enter L")
    # engine.say("Press first,second and fifth key to enter M")
    # engine.say("Press first,second, fourth key to enter N")
    # engine.say("Press first,fourth and fifth key to enter O")
    # engine.say("Press first,second,third and fifth key to enter P")
    # engine.say("Press first,second,third,fourth and fifth key to enter Q")
    # engine.say("Press first,third,fourth and fifth key to enter R")
    # engine.say("Press second,third and fifth key to enter S")
    # engine.say("Press second,third,fourth and fifth key to enter T")
    # engine.say("Press first,fifth and sixth key to enter U")
    # engine.say("Press first,third,fifth and sixth key to enter V")
    # engine.say("Press second,third,fourth and sixth key to enter W")
    # engine.say("Press first,second,fifth and sixth key to enter X")
    # engine.say("Press first,second,fourth,fifth and sixth key to enter Y")
    # engine.say("Press first,fourth,fifth and sixth key to enter Z")    
    
    # return redirect('/practice')
     
    return redirect("/learn")


if __name__ == "__main__":
    app.run(debug=True)

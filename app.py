from flask import Flask, render_template, request
import time
from time import strftime
import datetime
import re
from pyfiglet import Figlet
import pywhatkit

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
# def index(name):
#     return '<h1>hello {}</h1>'.format(name)

def set_alarm():
    schedule_date = request.form.get('schedule_date')
    num = request.form.get('num')
    f = Figlet(font ='5lineoblique')
    print(f.renderText("Alarms has been set"))
    print()
    now = datetime.datetime.now()
    print("----------------------")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print("----------------------")
    return render_template("index.html")

@app.route('/')

def ring_alarm():
    schedule_date = request.form.get('schedule_date')
    set_time = request.form.get('set_time')
    while True:
        if (time.localtime() == set_time) and  (datetime.date.today() == schedule_date):
            print(f.renderText("BEEP BEEP ITS TIME...  "))
            pywhatkit.playonyt("programming in python")
            # arr.reverse()
            # arr.pop()
            # arr.reverse()
            # display()
    return render_template("index.html")

from flask import Flask, render_template, request
import time
from time import strftime
import datetime
import re
from pyfiglet import Figlet
import pywhatkit

# def index(name):
#     return '<h1>hello {}</h1>'.format(name)


app = Flask(__name__)


# @app.route('/')
@app.route('/', methods=['GET','POST'])
def set_alarm():
    if request.method == "POST":
        schedule_date = request.form.get('schedule_date')
        print("schedule_date is", schedule_date," ", type(schedule_date))

        set_time = request.form.get('set_time')
        print("set_time is", set_time," ", type(schedule_date))

        print("time.localtime() is ",time.localtime()," ", type(schedule_date))

        return "Schedule is " + schedule_date + " set_time is " + set_time
        # num = request.form.get('num')
        # f = Figlet(font ='5lineoblique')
        # print(f.renderText("Alarms has been set"))
        # print()
        # now = datetime.datetime.now()
        # print("----------------------")
        # print(now.strftime("%Y-%m-%d %H:%M:%S"))
        # print("----------------------")

    return render_template("index.html")


# @app.route('/', methods =["GET", "POST"])
# def gfg():
#     if request.method == "POST":
#        # getting input with name = fname in HTML form
#        first_name = request.form.get("fname")
#        # getting input with name = lname in HTML form 
#        last_name = request.form.get("lname") 
#        return "Your name is "+first_name + last_name
#     return render_template("index.html")

# @app.route('/')
# def func():
#     return render_template("index.html")

# @app.route('/')
def ring_alarm():
    schedule_date = request.form.get('schedule_date')
    set_time = request.form.get('set_time')
    while True:
        if (time.localtime() == set_time) and  (datetime.date.today() == schedule_date):
            print(f.renderText("BEEP BEEP IT;S TIME...  "))
            pywhatkit.playonyt("programming in python")
            # arr.reverse()
            # arr.pop()
            # arr.reverse()
            # display()
    return render_template("index.html")


if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = '5000')

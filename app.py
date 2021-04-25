from flask import Flask, render_template, request
import time
from time import strftime
import datetime
import re
from pyfiglet import Figlet
import pywhatkit


app = Flask(__name__)

# @app.route('/')
@app.route('/', methods=['GET','POST'])
def set_alarm():
    if request.method == "POST":
        schedule_date = str(request.form.get('schedule_date'))
        print("schedule_date is", schedule_date," ", type(schedule_date))

        set_time = str(request.form.get('set_time'))
        print("set_time is", set_time," ", type(set_time))

        # print("time.localtime() is ",time.localtime()," ", type(time.localtime()))
        print("datetime.date.today() is " , datetime.date.today(), " ", type(datetime.date.today))
        
        # print(curr_date)

        
        
        # print(curr_time)
        # print(set_time)
        # print(curr_date)
        # print(schedule_date)

        while True:
            curr_date = str(datetime.date.today())
            now = datetime.datetime.now()
            hour = str(now.hour)
            minute = str(now.minute)
            # seconds = str(now.second)
            curr_time = hour + ":" + minute 
            # print("Current time is: "  + curr_time)
            if (curr_time == set_time) and  (curr_date == schedule_date):
                # print(f.renderText("BEEP BEEP IT'S TIME...  "))
                pywhatkit.playonyt("programming in python")

        return "Schedule date is " + schedule_date + "   set_time is " + set_time
    return render_template("index.html")


if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = '5000')



import time
from time import strftime
import datetime
import re
from pyfiglet import Figlet
import pywhatkit


num = int(input("How many alarms you want to set? "))
i=1
arr=[]
flag=0

print()
print("Alram format: (hh:mm:ss) ")
print("Date format: (dd/mm/yyyy)")
print()
c, b, a = input("Enter the date" + str(i)+": ").split("/")
schedule_date = datetime.date(int(a), int(b), int(c))


while num:
    t = input("set the alarm time "+ str(i) + " : ")
    arr.append(re.split('[: /s]', t))
    h = int(arr[-1][0])
    m = int(arr[-1][1])
    s = int(arr[-1][2])
    if m>=60 or s>=60:
        print("invalid time")
        arr.pop()
        i-=1
        num+=1
    i=i+1
    num=num-1


    

f = Figlet(font ='5lineoblique')
print(f.renderText("Alarms has been set"))
print()

now = datetime.datetime.now()
print("----------------------")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("----------------------")
print(arr)

def display():
    print()
    print("----------------------")
    print("|| Alarm yet to ring ||")
    print("----------------------")
    for k in arr:
        print("||"+k[0]+":"+k[1]+":"+k[2]+ "||")
        print("---------------------")

while True:
    for row in arr:
        if (time.localtime().tm_hour == int(row[0])) and (time.localtime().tm_min == int(row[1])) and (time.localtime().tm_sec == int(row[2])) and (datetime.date.today() == schedule_date):
            print(f.renderText("BEEP BEEP ITS TIME...  "))
            pywhatkit.playonyt("programming in python")
            arr.reverse()
            arr.pop()
            arr.reverse()
            display()
    



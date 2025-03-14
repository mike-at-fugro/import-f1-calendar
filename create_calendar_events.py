import win32com.client as client
import json
from datetime import datetime


def get_start(time, date):
    month = date.split(' ')[0]
    day = date.split(' ')[1]
    dt = "2025/" + month + "/" + day + "T" + time
    dt_format = "%Y/%B/%dT%H:%M"
    dt = datetime.strptime(dt, dt_format)
    return dt


def create_outlook_event(event):
    appointment = outlook.CreateItem(1) #1 refers to the appointment item
    appointment.Subject = "Grand Prix: " + event['Country']
    appointment.Start = get_start(event['GMT'], event['Date'])
    appointment.Duration = 120
    appointment.Save()


outlook = client.Dispatch('Outlook.Application')
namespace = outlook.GetNamespace('MAPI')
calendar = namespace.GetDefaultFolder(9) #9 refers to outlook calendar folder

with open('race_start_times.json', 'r') as races_file:
    race_data = json.load(races_file)

for race in race_data:
    create_outlook_event(race)
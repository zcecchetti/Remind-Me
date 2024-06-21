# use this script for functions to interact with SQLite Alerts database

import sqlite3
from datetime import date

con = sqlite3.connect("/Users/zach/Documents/Python/remindMe/Alerts.db")

cur = con.cursor()

def countAlerts ():
    cur.execute("SELECT COUNT(*) FROM Alerts")
    alert_count = cur.fetchone()[0]

    return(alert_count)

def addNewAlert (alert_name, alert_details, alert_recipients, alert_date, alert_time, recurring):
    new_alert_id = countAlerts() + 1 
    new_data = [new_alert_id, alert_name, alert_details, alert_recipients, alert_date, alert_time, recurring]
    cur.execute("INSERT INTO Alerts VALUES ( ?, ?, ?, ?, ?, ?, ?)", new_data)
    con.commit()

    return new_data

def removeAlert():
    alert_name = "Roux Birthday"
    cur.execute("DELETE FROM Alerts WHERE alert_name = ?", (alert_name,))
    con.commit()

    return

def readAllAlerts ():
    alertList = []
    for row in cur.execute("select alert_id , alert_name FROM Alerts ORDER BY alert_id"):
        alertList.append(row)
    
    return alertList

def checkDailyAlerts ():
    alertList = []
    today = date.today()
    for row in cur.execute("select alert_date, alert_name, alert_details, alert_time FROM Alerts WHERE alert_date = ?", (today, )):
        alertList.append(row)

    print(today)

    return alertList

print(countAlerts())
print(addNewAlert("Roux Birthday", "Today is Rouxs birthday", "Everyone", "2005-11-22", "12:00:00.000", "1" ))
print(readAllAlerts())
removeAlert()
print(readAllAlerts())
print(checkDailyAlerts())


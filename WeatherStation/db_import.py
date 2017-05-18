import MySQLdb
import json
import urllib2
import time
import smtplib
from email.mime.text import MIMEText

# This is the code on the Raspberry Pi used for data extraction and generating warnings regarding the station on reserve power

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = '/home/pi/Documents/WeatherStationAlertMessage.txt'
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

#setting up email parameters
me = '*******'
you = '*******'
msg['Subject'] = 'Error: Weather Station Low Voltage!'
msg['From'] = me
msg['To'] = you

lowCount = 0
highCount = 0
trigger = False

lowerBoundTrigger = 12.1
upperBoundTrigger = 12.7


#startup wait for internet connection
time.sleep(70)


while True:
    recent_batt = -1

    #connecting to the db
    db = MySQLdb.connect(host="*****",    # your host, usually localhost
                     user="******",         # your username
                     passwd="******",  # your password
                     db="******")        # name of the data base

    cur = db.cursor()
    
    # below is the code for inserting the recent records into the database
    cur.execute("SELECT recordNum FROM WeatherStation_record where recordNum=(SELECT MAX(recordNum) FROM WeatherStation_record);")
    for row in cur.fetchall():
        recent_rec = row[0]

    #webAPI call to obtain the JSON file containing the required data to be inserted into MySQL db off-site
    wc = "http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=" + str(
                    recent_rec)
    url = urllib2.urlopen(wc)
    j = json.loads(url.read().decode())

    #used to find out how many records were obtained, usually it is only 1 but could be more if there was a hiccup in the system such as a network outage
    num_recs = len(j["data"])
    count=1

    #loops through as many records as were obtained and inserts them into the off-site db
    while count < num_recs:
        dt = j["data"][count]['time']
        newDt = dt.replace('T', ' ')
        cur.execute("INSERT INTO WeatherStation_record VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (newDt, j["data"][count]['no'], j["data"][count]['vals'][0], j["data"][count]['vals'][1], j["data"][count]['vals'][2], j["data"][count]['vals'][3], j["data"][count]['vals'][4], j["data"][count]['vals'][5], j["data"][count]['vals'][6], j["data"][count]['vals'][7], j["data"][count]['vals'][8], j["data"][count]['vals'][9], j["data"][count]['vals'][10], j["data"][count]['vals'][11]) )
        count = count + 1
    ######################################################

    

     # below is the code for low battery warning system, count bounds set to 3 times what they normally would be to account for 10 min check times yet only 30 min data recording  
    cur.execute("SELECT battAvg FROM WeatherStation_record where recordNum=(SELECT MAX(recordNum) FROM WeatherStation_record);")
    for row in cur.fetchall():
        recent_batt = row[0]



    if (recent_batt == -1):
        #something went wrong
        print("Error")
    elif ((recent_batt < lowerBoundTrigger) and (lowCount <15)):
        lowCount+=lowCount
    #triggering the error message sequence
    elif ((recent_batt < lowerBoundTrigger) and (lowCount >=15) and (trigger==False)):
        trigger = True
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("esrm.ci.weatherstation@gmail.com", "7021$$mAuI^3")
        s.sendmail(me, [you], msg.as_string())
        s.quit()
    #repeat error message
    elif((recent_batt < upperBoundTrigger) and (trigger==True)):
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("esrm.ci.weatherstation@gmail.com", "7021$$mAuI^3")
        s.sendmail(me, [you], msg.as_string())
        s.quit()
    #checking to see if it is consistently above the upper bound to break error sequence
    elif((recent_batt >= upperBoundTrigger) and (highCount <6) and (trigger == True)):
        highCount+=highCount
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("esrm.ci.weatherstation@gmail.com", "7021$$mAuI^3")
        s.sendmail(me, [you], msg.as_string())
        s.quit()
    #once all is consistently recovered, reset all the check values and turn off the alert system
    elif((recent_batt >= upperBoundTrigger) and (highCount >=6) and (trigger == True)):
        trigger = False
        highCount = 0
        lowCount = 0

    #close the db connection
    db.close()
    #time between checks in seconds, currently every 10 minutes (600 seconds)
    time.sleep(600)
    

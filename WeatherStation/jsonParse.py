import django
django.setup()
import json
from WeatherStation.models import Record

#false = 'false'

#j = {"head": {"transaction": 0,"signature": 55431,"environment":  {"station_name":  "1844","table_name":  "Table1","model":  "CR6","serial_no":  "1844","os_version":  "CR6.Std.02","prog_name":  "CPU:untitled.CR6"},"fields":  [{"name":  "BattV_Avg","type":  "xsd:float","units":  "Volts","process":  "Avg","settable":  false},{"name":  "PTemp_C_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},{"name":  "AirTC_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},{"name":  "RH","type":  "xsd:float","units":  "%","process":  "Smp","settable":  false},{"name":  "SlrkW","type":  "xsd:float","units":  "kW/m^2","process":  "Smp","settable":  false},{"name":  "SlrMJ_Tot","type":  "xsd:float","units":  "MJ/m^2","process":  "Tot","settable":  false},{"name":  "WS_ms","type":  "xsd:float","units":  "meters/second","process":  "Smp","settable":  false},{"name":  "WindDir","type":  "xsd:float","units":  "degrees","process":  "Smp","settable":  false},{"name":  "PAR_Den","type":  "xsd:float","units":  "umol/s/m^2","process":  "Smp","settable":  false},{"name":  "PAR_Tot_Tot","type":  "xsd:float","units":  "mmol/m^2","process":  "Tot","settable":  false},{"name":  "BP_mmHg","type":  "xsd:float","units":  "mmHg","process":  "Smp","settable":  false},{"name":  "Rain_mm_Tot","type":  "xsd:float","units":  "mm","process":  "Tot","settable":  false}]},"data": [{"time":  "2017-04-10T06:30:00","no":  18570,"vals": [13.16,13.73,9.16,65.07,0.161,0.183819,0.346,243.6,1386,1854.59,762.1,0]},{"time":  "2017-04-10T07:00:00","no":  18571,"vals": [13.16,13.77,11.04,55.34,0.272,0.380101,0.061,71.7,2911,4032.802,762.4,0]},{"time":  "2017-04-10T07:30:00","no":  18572,"vals": [13.15,14.15,11.99,63.27,0.381,0.6007632,0.893,103,4217,6566.409,762.3,0]},{"time":  "2017-04-10T08:00:00","no":  18573,"vals": [13.16,14.88,13.04,55.06,0.486,0.803947,1.364,58.85,5466,8983.428,762.5,0]},{"time":  "2017-04-10T08:30:00","no":  18574,"vals": [13.15,15.7,14.56,46.62,0.537,0.9684597,1.165,143.2,6141,10975.86,762.6,0]}]}
import urllib.request, json
last_rec = 18560
com = "http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=" + str(last_rec)
print(com)
with urllib.request.urlopen(com) as url:
    j = json.loads(url.read().decode())
    print(j)
# http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=X   -where X is last record recorded
#print(json.dumps(j["data"]["vals"]))

record = Record()

# extracting data (formatting the time properly) and importing into Record models db
num_recs = len(j["data"])
count = 0
while count < num_recs:
    print("num_rec = " + str(count))
    dt = j['data'][count]['time']
    record.timeStamp = dt.replace('T', ' ')
    record.recordNum = j['data'][count]['no']
    record.battAvg = j['data'][count]['vals'][0]
    record.pTempCAvg = j['data'][count]['vals'][1]
    record.airTCAvg = j['data'][count]['vals'][2]
    record.rH = j['data'][count]['vals'][3]
    record.slrkW = j['data'][count]['vals'][4]
    record.slrMJTot = j['data'][count]['vals'][5]
    record.wSMs = j['data'][count]['vals'][6]
    record.windDir = j['data'][count]['vals'][7]
    record.pARDen = j['data'][count]['vals'][8]
    record.pARTotTot = j['data'][count]['vals'][9]
    record.bPMmHg = j['data'][count]['vals'][10]
    record.rainMmTot = j['data'][count]['vals'][11]
    print(record.recordNum)
    print(record.timeStamp)
    print(record.windDir)
    count = count + 1
    #record.save()
#print(record.bPMmHg)
import django
django.setup()
import json
from WeatherStation.models import Record

false = 'false'

j ={"head": {"transaction": 0,"signature": 55431,
              "environment":{"station_name":  "1844","table_name":  "Table1","model":  "CR6","serial_no":  "1844","os_version":  "CR6.Std.02","prog_name":  "CPU:untitled.CR6"},
              "fields":  [{"name":  "BattV_Avg","type":  "xsd:float","units":  "Volts","process":  "Avg","settable":  false},
                          {"name":  "PTemp_C_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},
                          {"name":  "AirTC_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},
                          {"name":  "RH","type":  "xsd:float","units":  "%","process":  "Smp","settable":  false},
                          {"name":  "SlrkW","type":  "xsd:float","units":  "kW/m^2","process":  "Smp","settable":  false},
                          {"name":  "SlrMJ_Tot","type":  "xsd:float","units":  "MJ/m^2","process":  "Tot","settable":  false},
                          {"name":  "WS_ms","type":  "xsd:float","units":  "meters/second","process":  "Smp","settable":  false},
                          {"name":  "WindDir","type":  "xsd:float","units":  "degrees","process":  "Smp","settable":  false},
                          {"name":  "PAR_Den","type":  "xsd:float","units":  "umol/s/m^2","process":  "Smp","settable":  false},
                          {"name":  "PAR_Tot_Tot","type":  "xsd:float","units":  "mmol/m^2","process":  "Tot","settable":  false},
                          {"name":  "BP_mmHg","type":  "xsd:float","units":  "mmHg","process":  "Smp","settable":  false},
                          {"name":  "Rain_mm_Tot","type":  "xsd:float","units":  "mm","process":  "Tot","settable":  false}]},
     "data": [{"time":  "2017-04-06T14:00:00","no":  18393,"vals": [13.05,21.67,16.05,80.8,0.357,0.8125592,6.718,164.4,4257,9616.478,760.1,0]}]}

#print(json.dumps(j["data"]["vals"]))

record = Record()

# extracting data (formatting the time properly) and importing into Record models db
dt = j['data'][0]['time']
record.timeStamp = dt.replace('T', ' ')
record.recordNum = j['data'][0]['no']
record.battAvg = j['data'][0]['vals'][0]
record.pTempCAvg = j['data'][0]['vals'][1]
record.airTCAvg = j['data'][0]['vals'][2]
record.rH = j['data'][0]['vals'][3]
record.slrkW = j['data'][0]['vals'][4]
record.slrMJTot = j['data'][0]['vals'][5]
record.wSMs = j['data'][0]['vals'][6]
record.windDir = j['data'][0]['vals'][7]
record.pARDen = j['data'][0]['vals'][8]
record.pARTotTot = j['data'][0]['vals'][9]
record.bPMmHg = j['data'][0]['vals'][10]
record.rainMmTot = j['data'][0]['vals'][11]
#record.save()
#print(record.bPMmHg)
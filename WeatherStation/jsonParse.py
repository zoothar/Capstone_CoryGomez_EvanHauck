import django
django.setup()
import urllib.request, json
import django
django.setup()
from WeatherStation.models import Record

def queryWeatherStation():
    last_rec = Record.objects.latest('recordNum')
    print(last_rec.recordNum)
    # http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=X   -where X is last record recorded
    com = "http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=" + str(last_rec.recordNum)
    print(com)
    with urllib.request.urlopen(com) as url:
        j = json.loads(url.read().decode())

    record = Record()

    # extracting data (formatting the time properly) and importing into Record models db
    num_recs = len(j["data"])
    print(str(num_recs))
    count = 0
    while count < num_recs:
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
        print(" recNum = " + str(record.recordNum) + "    timeStamp--->  " +  str(record.timeStamp) )
        count = count + 1
        record.save()
# from https://www.tutorialspoint.com/python3/python_networking.htm
import socket, json, time, urllib.request, traceback

# get local machine name
host = '10.31.143.236'

port = 12915

recent_rec = 19102

while True:
    check = True
    print('Client recent record: ' + str(recent_rec))
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while check:
        try:
            print('Attempting to grab JSON file and connect to server.')
            # connection to hostname on the port.
            s.connect((host, port))
            wc = "http://10.121.1.194/?command=dataquery&uri=dl:Table1&table=Table1&format=json&mode=since-record&p1=" + str(
                recent_rec)
            print(wc)
            with urllib.request.urlopen(wc) as url:
                j = json.loads(url.read().decode())
            print('connected')
            check = False
        except Exception as e:
            print(e)
            time.sleep(5)
    print('here we are.....')
    # for testing default json
    #false = 'false'
    #js = {"head": {"transaction": 0,"signature": 55431,"environment":  {"station_name":  "1844","table_name":  "Table1","model":  "CR6","serial_no":  "1844","os_version":  "CR6.Std.02","prog_name":  "CPU:untitled.CR6"},"fields":  [{"name":  "BattV_Avg","type":  "xsd:float","units":  "Volts","process":  "Avg","settable":  false},{"name":  "PTemp_C_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},{"name":  "AirTC_Avg","type":  "xsd:float","units":  "Deg C","process":  "Avg","settable":  false},{"name":  "RH","type":  "xsd:float","units":  "%","process":  "Smp","settable":  false},{"name":  "SlrkW","type":  "xsd:float","units":  "kW/m^2","process":  "Smp","settable":  false},{"name":  "SlrMJ_Tot","type":  "xsd:float","units":  "MJ/m^2","process":  "Tot","settable":  false},{"name":  "WS_ms","type":  "xsd:float","units":  "meters/second","process":  "Smp","settable":  false},{"name":  "WindDir","type":  "xsd:float","units":  "degrees","process":  "Smp","settable":  false},{"name":  "PAR_Den","type":  "xsd:float","units":  "umol/s/m^2","process":  "Smp","settable":  false},{"name":  "PAR_Tot_Tot","type":  "xsd:float","units":  "mmol/m^2","process":  "Tot","settable":  false},{"name":  "BP_mmHg","type":  "xsd:float","units":  "mmHg","process":  "Smp","settable":  false},{"name":  "Rain_mm_Tot","type":  "xsd:float","units":  "mm","process":  "Tot","settable":  false}]},"data": [{"time":  "2017-04-06T14:00:00","no":  18393,"vals": [13.05,21.67,16.05,80.8,0.357,0.8125592,6.718,164.4,4257,9616.478,760.1,0]}]}

    jsFile = json.dumps(j)
    s.sendall(jsFile.encode('ascii'))
    #s.sendall(jsFile.encode('ascii'))
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    s.close()
    print (msg.decode('ascii'))
    jload = json.loads(jsFile)
    count = len(jload["data"])
    recent_rec = jload["data"][count-1]['no']
    time.sleep(30)
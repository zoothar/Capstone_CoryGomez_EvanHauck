# from https://www.tutorialspoint.com/python3/python_networking.htm
from datetime import  datetime
import django
django.setup()
from WeatherStation.hostname import gethost
from socket import *
from WeatherStation.jsonParse import queryWeatherStation

def runserv():
    # create a socket object
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    host = gethost()
    print(host)
    port = 12915

    # bind to the port
    s.bind((host, port))


    s.listen(1)

    while True:
        # establish a connection
        clientsocket, addr = s.accept()
        rsp = 'File received at server at --->  ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        queryWeatherStation(clientsocket.recv(1024000))
        clientsocket.send(rsp.encode('ascii'))
        clientsocket.close()

#runserv()
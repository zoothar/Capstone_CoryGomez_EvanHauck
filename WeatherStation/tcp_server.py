# from https://www.tutorialspoint.com/python3/python_networking.htm
from datetime import  datetime
import django
django.setup()
from socket import *
from WeatherStation.jsonParse import queryWeatherStation
# create a socket object
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host = '192.168.0.57'
port = 12913

# bind to the port
s.bind((host, port))

# queue up to 5 requests
s.listen(1)

while True:
    # establish a connection
    clientsocket, addr = s.accept()
    clientsocket.setblocking(False)
    rsp = 'File received at server at --->  ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    queryWeatherStation(clientsocket.recv(10240))
    clientsocket.send(rsp.encode('ascii'))
    clientsocket.close()
# from https://www.tutorialspoint.com/python3/python_networking.htm
from datetime import  datetime
import django
django.setup()
import socket
#from socket import *
from WeatherStation.jsonParse import queryWeatherStation

def runserv():
    # create a socket object
    #socket()
    #s = socket(AF_INET, SOCK_STREAM)
    #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    host = socket.gethostbyname(socket.gethostname())
    print(host)
    port = 12915

    # bind to the port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        clientsocket, addr = s.accept()

    with clientsocket:
        while True:
            # establish a connection
            rsp = 'File received at server at --->  ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            queryWeatherStation(clientsocket.recv(1024000))
            clientsocket.send(rsp.encode('ascii'))
            clientsocket.close()

runserv()
import socket

def gethost():
    me = socket.gethostbyname(socket.gethostname())
    return me

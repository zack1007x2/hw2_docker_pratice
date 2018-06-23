import socket
import sys

arg1 = sys.argv[1]
print arg1

#target addr
HOST = '172.28.1.3'
PORT = 5001
ADDR = (HOST,PORT)
BUFSIZE = 4096
srcfile = "./src/"
srcfile += arg1


bytes = arg1+'@%@%@'+open(srcfile).read()

print len(bytes)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "open"
client.connect(ADDR)
print "connected"
client.send(bytes)

client.close()
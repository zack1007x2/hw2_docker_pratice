import socket
import sys

#setup self as server
HOST = '172.28.1.3'
PORT = 5001
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
  conn, addr = serv.accept()
  print 'client connected ... ', addr
  getFileName=False

  while True:
    data = conn.recv(BUFSIZE)
    if not data: break

    if not getFileName:
      myfile = open('./src/'+data.split('@%@%@')[0], 'w')
      print 'receive file : '+data.split('@%@%@')[0]
      getFileName = True
      myfile.write(data.split('@%@%@')[1])
    else:
      myfile.write(data)
    print 'writing file ....'

  myfile.close()
  print 'finished writing file'

conn.close()
print 'client disconnected'
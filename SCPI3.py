from telnetlib import Telnet
tn=Telnet('192.168.29.2', 5555) ## IP EB500
f=open('./RDSFM.txt','r',encoding="utf-8")
inst1= f.readline()
inst2= f.readline()
inst3= f.readline()
inst4= f.readline()
inst5= f.readline()
inst6= f.readline()

print(inst1)
print(inst2)
print(inst3)
print(inst4)
print(inst5)
print(inst6)

x1=inst1 + "\n"
x2=inst2 + "\n"
x3=inst3 + "\n"
x4=inst4 + "\n"
x5=inst5 + "\n"
x6=inst6 + "\n"

tn.write(x1.encode('utf-8'))
tn.write(x2.encode('utf-8'))
tn.write(x3.encode('utf-8'))
tn.write(x4.encode('utf-8'))
tn.write(x5.encode('utf-8'))
tn.write(x6.encode('utf-8'))

f.close()

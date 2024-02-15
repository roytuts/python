import subprocess
import platform

if(platform.system()=="Windows"):
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii")
elif(platform.system=="Linux"):
    results = subprocess.check_output(["iwlist", "scan"])
    results = results.decode("utf-8")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)
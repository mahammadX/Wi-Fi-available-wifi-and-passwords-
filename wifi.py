import subprocess

print("+"*20,"Programming by Eng. Mahammad Qassem","+"*20)
print("+"*20,"IT Support and Civil Engineering","+"*20)


print(" ")
print("-"*20,"Wi-Fi available to  Connected","-"*20)
results = subprocess.check_output(["netsh","wlan","show","network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x<len(ls):
    if x%5==0:
        ssids.append(ls[x])
    x+=1

print(ssids)

print("-"*20,"Password for Wi-Fi Connected By This Device","-"*20)
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")

print("+"*20,"Thanks for Using Program","+"*20)
print("+"*20,"Programming by Eng. Mahammad Qassem","+"*20)
print("+"*20,"IT Support and Civil Engineering","+"*20)


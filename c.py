import subprocess
import os

inputdnfpackage = ""
e = ""
command = f"sudo dnf install {inputdnfpackage}"
output = subprocess.check_output(['ls'], text=True)
current = os.getcwd()
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("welcome to subminal-dev!! python based terminal (poorly known coding) and this is broken , dont wait too much from this :(")

komut_gir = input(f"{current} --> ")

if komut_gir.lower() == 'ls':
    print(output)
    komut_gir = input(f"{current} --> ")
if komut_gir.lower() == 'help':
    print("commands : help , ls , exit , info , github , dnfeasy (just install packages)")
    komut_gir = input(f"{current} --> ")
if komut_gir.lower() == 'exit':
    print("see you later!!")
if komut_gir.lower() == 'info':
    print("username :", os.getlogin())
    print("os :", os.name)
    print("subminal-dev version : 1.0")
    komut_gir = input(f"{current} --> ")
if komut_gir.lower() == 'github':
    print("command in development..")
    komut_gir = input(f"{current} --> ")
    
        




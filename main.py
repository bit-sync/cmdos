# start backend

import os 
import platform
import software.Poss.pcommands as poss


plat = platform.system()
runposs = "python3 software/Poss/posspmanager.py"
possversion = "1.3.1 CmdOS version"
version = "Build 1.3.6"

def about():
    print("about CmdOS")
    print("version: " + version)
    print("platform: "+ plat)
    print("Made by Extraskilled56")
    print("Copyright Extraskilled56, 2024")
    
def command():
    command = str(input("C:"))
    if command == "version":
        print(version)
    elif command == "about":
        about()
    elif command == "poss":
        os.system(runposs)
    elif command == "poss install fusiongamesxcli":
        poss.install_FusionGamesXCLI()
    elif command == "poss run fusiongamesxcli":
        poss.run_FusionGamesXCLI()
    elif command == "poss install pycalculate":
        poss.install_pyCalculate()
    elif command == "poss run pycalculate":
        poss.run_pyCalculate()
    elif command == "poss list":
        poss.list()
    elif command == "exit":
        exit()
    elif command == "poss version":
        print(possversion)
    elif command == "update":
        os.system("git pull")
    else:
        print("command not reconized")
    
# start frontend

print("Welcome to CmdOS")

print("A basic OS, for basic things")

print("This is a beta " + version + " some things might not work")

command()
command()
command()
command()
command()
command()
command()
command()
command()

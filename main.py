# start backend

import os 
import platform
import pcommands as poss


plat = platform.system()
runposs = "python3 posspmanager.py"
version = "Build 0.0.1"


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

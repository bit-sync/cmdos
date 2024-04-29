# start backend
#! Most poss commands cannot be used, they do not work

import os 
import platform
import Poss.pcommands as poss
import system.autorepair as autorp

plat = platform.system()
runposs = "python3 Poss/posspmanager.py"
possversion = "1.3.1 CmdOS version"
version = "Build 1.6.0"
errors = int("0")
abcheckid = True

def about():
    global abcheckid
    abcheckid = True
    print("about CmdOS")
    print("version: " + version)
    print("platform: "+ plat)
    print("Made by Extraskilled56")
    print("Copyright Extraskilled56, 2024")
#TODO fix this function so that it correctly places autorepair file in correct folder
#! auto repair dosent work rn
def boot():
    global errors
    PYpadcheck = os.path.isfile("system/sys_software/PYpad/PYpad.py")
    PYmathcheck = os.path.isfile("system/sys_software/PYmath/PYmath.py")
    PYpaintcheck = os.path.isfile("system/sys_software/PYpaint/PYpaint.py")
    Posscheck1 = os.path.isfile("Poss/pcommands.py")
    Posscheck2 = os.path.isfile("Poss/posspmanager.py")
    if version != version:
        print("Vcheck failed")
        errors += 1 # type: ignore
    else:
        print("Vcheck passed")

    if PYpadcheck == False:
        print("PYpadchech failed")
        errors += 1 # type: ignore
        autorp.repair("PYpad")
    else:
        print("PYpadchech passed")
    if PYmathcheck == False:
        print("PYmathchech failed")
        autorp.repair("PYmath")
        errors += 1 # type: ignore
    else:
        print("PYmathchech passed")
    if PYpaintcheck == False:
        print("PYpaintchech failed")
        autorp.repair("PYpaint")
        errors += 1 # type: ignore
    else:
        print("PYpaintchech passed")
    if Posscheck1 == False:
        print("Posschech failed")
        autorp.repair("poss1")
        errors += 1 # type: ignore
    if Posscheck2 == False:
        print("Posschech failed")
        autorp.repair("poss2")
        errors += 1 # type: ignore
    else:
        print("Posschech passed")
    if possversion != "1.3.1 CmdOS version":
        print("possversioncheck failed")
        errors += 1 # type: ignore
    else:
        print("possversioncheck passed") 
    if errors != 0:
        print("errors:")
        print(errors)
        print("Seems there was a problem booting CmdOS. (Error code: IGBMCHERRO)")
        print("If you have any questions, please contact us at: software@bitsyncdev.com")
        if errors > 3:
            print("Fatal errors detected. The program can no longer continue.")
            print("Stopping with exit code 12")
    else:
        print("errors:")
        print(errors)
        print("Welcome to CmdOS")
        print("A basic OS, for basic things")
        print("version: " + version)
        print("If you have any questions, please contact us at: software@bitsyncdev.com")

    

    
def command():
    command = str(input("C:"))
    if command == "version":
        print(version)
    elif command == "about":
        about()
    elif command == "PYpad":
        os.system("python3 system/sys_software/PYpad/PYpad.py")
    elif command == "PYmath":
        os.system("python3 system/sys_software/PYmath/PYmath.py")
    elif command == "PYpaint":
        os.system("python3 system/sys_software/PYpaint/PYpaint.py")
    elif command == "poss":
        print("Warning: This command is in testing, might not work properly")
        os.system(runposs)
    elif command == "poss install fusiongamesxcli":
        print("Warning: This command is in testing, might not work properly")
        poss.install_FusionGamesXCLI()
    elif command == "poss run fusiongamesxcli":
        print("Warning: This command is in testing, might not work properly")
        poss.run_FusionGamesXCLI()
    elif command == "poss install pycalculate":
        print("Warning: This command is in testing, might not work properly")
        poss.install_pyCalculate()
    elif command == "poss run pycalculate":
        print("Warning: This command is in testing, might not work properly")
        poss.run_pyCalculate()
    elif command == "poss install git-python":
        print("Warning: This command is in testing, might not work properly")
        poss.install_gitpython()
    elif command == "poss run git-python":
        print("Warning: This command is in testing, might not work properly")
        poss.run_gitpython()
    elif command == "poss list":
        print("Warning: This command is in testing, might not work properly")
        poss.list()
    elif command == "exit":
        exit()
    elif command == "poss version":
        print("Warning: This command is in testing, might not work properly")
        print(possversion)
    elif command == "update":
        os.system("git pull")
    else:
        print("command not reconized")
    
# start frontend

boot()

command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()
command()

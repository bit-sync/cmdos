# backend start

import os
import platform
lista = open("list.txt", "a")
listr = open("list.txt", "r")
version = "1.4.2 CmdOS build"
plat = platform.system()
def list():
    print(listr.read())

def about():
    print("About Poss:")
    print(version)
    print("platform: " + plat)
    print("Made by Extraskiled56")
    print("Thanks for using Poss!")

def update():
    os.system("git pull")
def command():
    command = input("")
    if command == "list":
        list()
    elif command == "exit":
        exit()
    elif command == "install":
        print("this command needs arguments")
    elif command == "run":
        print("this command needs arguments")
    elif command == "install fusiongamesxcli":
       install_FusionGamesXCLI()
       lista.write("fusiongamesxcli, ")
    elif command == "run fusiongamesxcli":
        run_FusionGamesXCLI()
    elif command == "install pycalculate":
       install_pyCalculate()
       lista.write("pycalculate, ")
    elif command == "run pycalculate":
        run_pyCalculate()
    elif command == "install git-python":
       install_gitpython()
       lista.write("git-python" + "/N")
    elif command == "run git-python":
        run_gitpython()
    elif command == "about":
        about()
    elif command == "update":
        update()
    else:
        print("command not found")

# fgxcli package start
def install_FusionGamesXCLI():
    os.system("cd software")
    os.system("git clone -b poss https://gitlab.com/fusiongames1/Fusion-Games-X-CLI.git")
def run_FusionGamesXCLI():
    os.system("cd software")
    os.system("python3 Fusion-Games-X-CLI/FusionGamesXCLI.py")
# fgxcli package end

# pycal package start
def install_pyCalculate():
    os.system("cd software")
    os.system("git clone -b main https://gitlab.com/zjones.092912/pycalculate.git")
def run_pyCalculate():
    os.system("cd cmdos")
    os.system("cd software")
    os.system("python3 software/pycalculate/main.py")
# pycal package end

# gitpy package start
def install_gitpython():
    os.system("cd software")
    os.system("git clone -b main https://gitlab.com/zjones.092912/git-python.git")
def run_gitpython():
    os.system("cd software")
    os.system("python3 git-python/git-python.py")
# gitpy package end
def end():
    exit()


# frontend start



print("Welcome to Poss. A Python package manager.")
print("Version: " + version)
print("platform: " + plat)

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
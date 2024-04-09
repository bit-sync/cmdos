import os
lista = open("list.txt", "a")
listr = open("list.txt", "r")

# fgxcli package start
def install_FusionGamesXCLI():
    os.system("cd software")
    os.system("git clone -b poss https://gitlab.com/fusiongames1/Fusion-Games-X-CLI.git")
    lista.write("fusiongamesxcli" + "\n")
def run_FusionGamesXCLI():
    os.system("cd software")
    os.system("python3 Fusion-Games-X-CLI/FusionGamesXCLI.py")
# fgxcli package end

# pycal package start
def install_pyCalculate():
    os.system("cd software")
    os.system("git clone -b main https://gitlab.com/zjones.092912/pycalculate.git")
    lista.write("pycalculate" + "\n")
def run_pyCalculate():
    os.system("python3 pycalculate/main.py")
# pycal package end

def list():
    print(listr.read())
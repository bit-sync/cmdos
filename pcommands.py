import os
lista = open("list.txt", "a")
listr = open("list.txt", "r")

# fgxcli package start
def install_FusionGamesXCLI():
    os.system("git clone -b poss https://gitlab.com/fusiongames1/Fusion-Games-X-CLI.git")
    lista.write("fusiongamesxcli, ")
def run_FusionGamesXCLI():
    os.system("python3 Fusion-Games-X-CLI/FusionGamesXCLI.py")
# fgxcli package end

# pycal package start
def install_pyCalculate():
    os.system("git clone -b main https://gitlab.com/zjones.092912/pycalculate.git")
    lista.write("pycalculate, ")
def run_pyCalculate():
    os.system("python3 pycalculate/main.py")
# pycal package end
    
def install_git_python():
    os.system("git clone -b main https://gitlab.com/zjones.092912/git-python.git")
def run_git_python():
    os.system("python3 git-python/git-python.py")

def list():
    print(listr.read())
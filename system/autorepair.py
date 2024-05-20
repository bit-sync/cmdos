import os


def repair(item):
    if item == "PYmath":
        os.system("curl -o PYmath.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYmath/PYmath.py")
        os.system("mv PYmath.py system/sys_software/PYmath")
        print("attempted to repaired PYmath, please re-run CmdOS to chech")
    elif item == "PYpaint":
        os.system("curl -o PYpaint.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpaint/PYpaint.py")
        os.system("mv PYpaint.py system/sys_software/PYpaint")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
        
    elif item == "PYpad":
        os.system("curl -o PYpad.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpad/PYpad.py")
        os.system("mv PYpad.py system/sys_software/PYpad")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
    elif item == "poss1":
        os.system("curl -o pcommands.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/Poss/pcommands.py")
        os.system("mv pcommands.py Poss")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    elif item == "poss2":
        os.system("curl -o posspmanager.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/Poss/posspmanager.py")
        os.system("mv posspmanager.py Poss")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    else:
        print(item + " not compatable with auto repair")
        

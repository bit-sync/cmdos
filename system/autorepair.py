import os


def repair(item):
    if item == "PYmath":
        os.system("curl -o system/sys_software/PYmath/PYmath.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYmath/PYmath.py")
        print("attempted to repaired PYmath, please re-run CmdOS to chech")
    elif item == "PYpaint":
        os.system("curl -o system/sys_software/PYpaint/PYpaint.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpaint/PYpaint.py")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
        
    elif item == "PYpad":
        os.system("curl -o system/sys_software/PYpad/PYpad.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpad/PYpad.py")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
    elif item == "poss1":
        os.system("curl -o Poss/pcommands.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/software/Poss/pcommands.py")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    elif item == "poss2":
        os.system("curl -o Poss/posspmanager.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/software/Poss/posspmanager.py")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    else:
        print(item + " not compatable with auto repair")
        

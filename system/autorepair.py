import os


def repair(item):
    if item == "PYmath":
        os.system("cd system/sys_software/PYmath")
        os.system("curl -o PYmath.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYmath/PYmath.py")
        print("attempted to repaired PYmath, please re-run CmdOS to chech")
    elif item == "PYpaint":
        os.system("cd system/sys_software/PYpaint")
        os.system("curl -o PYpaint.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpaint/PYpaint.py")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
    elif item == "PYpad":
        os.system("cd system/sys_software/PYpad")
        os.system("curl -o PYpad.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpad/PYpad.py")
        print("attempted to repaired PYpad, please re-run CmdOS to chechd")
    elif item == "poss1":
        os.system("cd software/Poss")
        os.system("curl -o pcommands.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/software/Poss/pcommands.py")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    elif item == "poss2":
        os.system("cd software/Poss")
        os.system("curl -o posspmanager.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/software/Poss/posspmanager.py")
        print("attempted to repaired poss, please re-run CmdOS to chech")
    else:
        print("{item} not compatable with auto repair")
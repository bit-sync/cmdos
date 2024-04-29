"""
elif item == "PYpaint":
        if os.path.isfile("system/sys_software/PYpaint/") == True:
            os.system("cd system/sys_software/PYpaint")
            os.system("curl -o PYpaint.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpaint/PYpaint.py")
        else:
            os.system("cd system/sys_software")
            os.system("mkdir PYpaint")
            os.system("curl -o PYpaint.py https://git.bitsyncdev.com/bit-sync/cmdos/raw/branch/main/system/sys_software/PYpaint/PYpaint.py")
        print("attempted to repaired PYpaint, please re-run CmdOS to chech")
"""
# start backend

import os 
import platform


plat = "NULL"

version = "Build 0.0.1"


def about():
    print("about CmdOS")
    print("version: " + version)
    print("platform: "+ plat)
    print("Made by Extraskilled56")
    print("Copyright Extraskilled56 2024")
    


def command():
    command = str(input("C:"))
    if command == "version":
        print(version)
    if command == "about":
        about()
    else:
        print("command not reconized")
# start frontend

print("Welcome to CmdOS")

print("A basic OS, for basic things")

print("This is a beta " + version + "s ome things might not work")

command()
command()
command()
command()
command()
command()
command()
command()
command()

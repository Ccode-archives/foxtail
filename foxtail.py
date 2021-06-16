from termcolor import colored as c
from termcolor import cprint
import os
running = True
def NU():
    print("unknown command")
while running:
    path_ = os.getcwd()
    path = format(path_)
    inp = input(c(path, 'blue') + c(" $", 'green'))
    if inp.startswith("cd "):
        try:
            change = inp.replace("cd ", "")
            os.chdir(path + "/" + change)
        except:
            print("File is either not a directory or does not exist.")
    elif inp == "l":
        os.system("ls")
    elif inp == "cwd":
        print(c(path, 'green'))
    elif inp.startswith("echo "):
        out = inp.replace("echo ", "")
        print(out)
    elif inp.startswith("mdir "):
        mk = inp.replace("mdir ", "")
        if not os.system("mkdir " + mk) == 0:
            print("bash error")
    elif inp.startswith("rem "):
        rm = inp.replace("rem ", "")
        if not os.system("rm " + rm) == 0:
            print("bash error")
    elif inp.startswith("remdir "):
        rm = inp.replace("remdir ", "")
        if not os.system("rm -r " + rm) == 0:
            print("bash error")
    elif inp.startswith("mf "):
        add = inp.replace("mf ", "")
        if not os.system("touch " + add) == 0:
            print("bash error")
    elif inp.startswith("read "):
        read = inp.replace("read ", "")
        if not os.system("cat " + read) == 0:
            print("bash error")
    elif inp.startswith("version"):
        cprint("1.0", 'green')
    elif inp == "exit":
        running = False
    else:
        NU()

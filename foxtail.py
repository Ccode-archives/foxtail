import os
running = True
def NU():
    print("unknown command")
while running:
    path_ = os.getcwd()
    path = format(path_)
    inp = input(path + " $")
    if inp.startswith("cd ") == True:
        try:
            change = inp.replace("cd ", "")
            os.chdir(path + "/" + change)
        except:
            print("File is either not a directory or dose not exist.")
    else:
        if inp == "l":
            os.system("ls")
        else:
            if inp == "cwd":
                print(path)
            else:
                if inp.startswith("echo ") == True:
                    out = inp.replace("echo ", "")
                    print(out)
                else:
                    if inp.startswith("mdir ") == True:
                        mk = inp.replace("mdir ", "")
                        if not os.system("mkdir " + mk) == 0:
                            print("bash error")
                    else:
                        if inp.startswith("rem ") == True:
                            rm = inp.replace("rem ", "")
                            if not os.system("rm " + rm) == 0:
                                print("bash error")
                        else:
                            if inp.startswith("remdir ") == True:
                                rm = inp.replace("remdir ", "")
                                if not os.system("rm -r " + rm) == 0:
                                    print("bash error")
                            else:
                                if inp.startswith("mf ") == True:
                                    add = inp.replace("mf ", "")
                                    if not os.system("touch " + add) == 0:
                                        print("bash error")
                                else:
                                    if inp.startswith("read ") == True:
                                        read = inp.replace("read ", "")
                                        if not os.system("cat " + read) == 0:
                                            print("bash error")
                                    else:
                                        if inp == "exit":
                                            running = False
                                        else:
                                            NU()

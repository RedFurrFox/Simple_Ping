T = """
\033[1;32;40m@@@@@@@   @@@  @@@  @@@   @@@@@@@@
@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@@
@@\033[1;33;40m!  \033[1;32;40m@@@  @@\033[1;33;40m!  \033[1;32;40m@@\033[1;33;40m!\033[1;32;40m@\033[1;33;40m!\033[1;32;40m@@@  \033[1;33;40m!\033[1;32;40m@@      
\033[1;33;40m!\033[1;32;40m@\033[1;33;40m!  \033[1;32;40m@\033[1;33;40m!\033[1;32;40m@  \033[1;33;40m!\033[1;32;40m@\033[1;33;40m!  !\033[1;32;40m@\033[1;33;40m!!\033[1;32;40m@\033[1;33;40m!\033[1;32;40m@\033[1;33;40m!  !\033[1;32;40m@\033[1;33;40m!      
\033[1;32;40m@\033[1;33;40m!\033[1;32;40m@@\033[1;33;40m!\033[1;32;40m@\033[1;33;40m!   !!\033[1;32;40m@  \033[1;32;40m@\033[1;33;40m!\033[1;32;40m@ \033[1;33;40m!!\033[1;32;40m@\033[1;33;40m!  !\033[1;32;40m@\033[1;33;40m! \033[1;32;40m@\033[1;33;40m!\033[1;32;40m@\033[1;33;40m!\033[1;32;40m@
\033[1;33;40m!!\033[1;32;40m@\033[1;33;40m!!!    !!!  !\033[1;32;40m@\033[1;33;40m!  !!!  !!! !!\033[1;32;40m@\033[1;33;40m!!
!!\033[1;31;40m:       \033[1;33;40m!!\033[1;31;40m:  \033[1;33;40m!!\033[1;31;40m:  \033[1;33;40m!!!  \033[1;31;40m:\033[1;33;40m!!   \033[1;33;40m!!\033[1;31;40m:
\033[1;31;40m:\033[1;33;40m!\033[1;31;40m:       :\033[1;33;40m!\033[1;31;40m:  :\033[1;33;40m!\033[1;31;40m:  \033[1;33;40m!\033[1;31;40m:\033[1;33;40m!  \033[1;31;40m:\033[1;33;40m!\033[1;31;40m:   \033[1;33;40m!\033[1;31;40m::
 ::        ::   ::   ::   ::: ::::
 :        :    ::    :    :: :: : \033[0;37;40m\n\n
"""

try:
    import os
except ModuleNotFoundError:
    print("Cannot Find Package Named 'os' On This Device. Please Install It Manually By Doing This Command:\n"+"'python -m pip install os' or 'pip install os")
try:
    try:
        import time
    except ModuleNotFoundError:
        print("[!] Missing Required Package Detected")
        print("[-] Automatically Installing Package Named: time")
        os.system("python -m pip install time")
    try:
        import subprocess
    except ModuleNotFoundError:
        print("[!] Missing Required Package Detected")
        print("[-] Automatically Installing Package Named: subprocess")
        os.system("python -m pip install time")
    try:
        import speedtest
    except ModuleNotFoundError:
        print("[!] Missing Required Package Detected")
        print("[-] Automatically Installing Package Named: subprocess")
        os.system("python -m pip install speedtest")
except ConnectionAbortedError:
    print("\n\n\n" + "[!] Error Found: ConnectionAbortedError")
    print("[-] Proceeding Script Termination")
    exit()
except ConnectionRefusedError:
    print("\n\n\n" + "[!] Error Found: ConnectionRefusedError")
    print("[-] Proceeding Script Termination")
    exit()
except ConnectionResetError:
    print("\n\n\n" + "[!] Error Found: ConnectionResetError")
    print("[-] Proceeding Script Termination")
    exit()
except ConnectionError:
    print("\n\n\n" + "[!] Error Found: ConnectionError")
    print("[-] Proceeding Script Termination")
    exit()
except:
    print("[!] Encountered An Error, Proceeding To Exit")
    exit()

def Clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def C1():
    Clear()
    print(T)
    print("[>] Selections:\n    [01] Start\n    [02] Help\n    [03] Self Destruct\n    [00] Exit\n")
    try:
        time.sleep(0.80)
        A = int(input("[?] Your Selection: "))
        if A == 1:
            def O1():
                print(T)
                print("[>] Selections:\n    [01] Ping By Website/Host\n    [02] Speedtest\n    [03] Back\n    [00] Exit\n")
                try:
                    time.sleep(0.80)
                    B = int(input("[?] Your Selection: "))
                    if B == 1:
                        def O_sub():
                            Clear()
                            print(T)
                            time.sleep(0.80)
                            host = input("[?] Enter Website/Host: ")
                            packet = int(input("[?] Enter Packet Size: "))
                            print("\n\n")
                            p = subprocess.getoutput(f"ping -w {packet} {host}")
                            print("----------------------------------\n" + p + "\n----------------------------------\n\n\n")
                            time.sleep(0.80)
                            print("[>] Selections:\n    [01] Try Again\n    [02] Back\n    [03] Home\n    [00] Exit\n")
                            time.sleep(0.80)
                            try:
                                C = int(input("[?] Your Selection: "))
                                if C == 1:
                                    print("\n\n\n" + "[-] Redirecting You Automatically...")
                                    O_sub()
                                elif C == 2:
                                    print("\n\n\n" + "[-] Redirecting You Automatically...")
                                    O1()
                                elif C == 3:
                                    print("\n\n\n" + "[-] Redirecting You Automatically...")
                                    C1()
                                elif C == 0:
                                    print("\n\n\n" + "[*] Thank You For Using My Script")
                                    print("[-] Proceeding Script Termination")
                                    exit()
                                else:
                                    print("\n\n\n" + "[!] Selection Not Found On The List")
                                    print("[-] Redirecting You Automatically...")
                                    time.sleep(1.50)
                                    O1()
                            except ValueError:
                                print("\n\n\n" + "[!] Invalid Choice")
                                print("[-] Redirecting You Automatically...")
                                time.sleep(1.50)
                                O1()
                            except TypeError:
                                print("\n\n\n" + "[!] Invalid Choice")
                                print("[-] Redirecting You Automatically...")
                                time.sleep(1.50)
                                O1()
                        O_sub()
                    elif B == 2:
                        """
                        def O_sub():
                            Clear()
                            print(T)
                            print("[>] Selections:\n    [01] Download Speed\n    [02] Upload Speed\n    [03] Ping\n    [04] Back\n    [05] Home\n    [00] Exit\n")
                            try:
                                time.sleep(0.80)
                                st = speedtest.Speedtest()
                                op = int(input("[?] Your Selection: "))
                                if op == 1:
                                    print(st.download())
                                elif op == 2:
                                    print(st.upload())
                                elif op == 3:
                                    servernames = []
                                    st.get_servers(servernames)
                                    print(st.results.ping)
                                elif op == 4:
                                    print("\n\n\n" + "[-] Redirecting You Automatically...")
                                    O1()
                                elif op == 5:
                                    print("\n\n\n" + "[-] Redirecting You Automatically...")
                                    C1()
                                elif op == 0:
                                    print("\n\n\n" + "[*] Thank You For Using My Script")
                                    print("[-] Proceeding Script Termination")
                                    exit()
                                else:
                                    print("\n\n\n" + "[!] Selection Not Found On The List")
                                    print("[-] Redirecting You Automatically...")
                                    time.sleep(1.50)
                                    O1()
                            except ValueError:
                                print("\n\n\n" + "[!] Invalid Choice")
                                print("[-] Redirecting You Automatically...")
                                time.sleep(1.50)
                                O_sub()
                            except TypeError:
                                print("\n\n\n" + "[!] Invalid Choice")
                                print("[-] Redirecting You Automatically...")
                                time.sleep(1.50)
                                O_sub()
                        O_sub()
                        """
                    elif B == 3:
                        print("\n\n\n" + "[-] Redirecting You Automatically...")
                        C1()
                    elif B == 0:
                        print("\n\n\n" + "[*] Thank You For Using My Script")
                        print("[-] Proceeding Script Termination")
                        exit()
                    else:
                        print("\n\n\n" + "[!] Selection Not Found On The List")
                        print("[-] Redirecting You Automatically...")
                        time.sleep(1.50)
                        O1()
                except ValueError:
                    print("\n\n\n" + "[!] Invalid Choice")
                    print("[-] Redirecting You Automatically...")
                    time.sleep(1.50)
                    O1()
                except TypeError:
                    print("\n\n\n" + "[!] Invalid Choice")
                    print("[-] Redirecting You Automatically...")
                    time.sleep(1.50)
                    O1()
            Clear()
            O1()
        elif A == 2:
            print(2)
        elif A == 3:
            x = "[!] Self Destruct Initiated...\n" + "[:] Note: You Can't Retrieve This File And Its Contents After It Hits Zero, Only This File Will Be Removed!\n" + "[>] To Terminate Self Destruct, Please Press 'Ctrl+c' Or 'Ctrl+z' To Cancel\n\n"
            y = "[-] Automatic Tool Disposal Will Run After: "
            for i in range(0, 16):
                v = str(15-i)
                Clear()
                print(f'{x + y + v}s')
                time.sleep(1.00)
            # os.remove("run.py")
        elif A == 0:
            print("\n\n\n" + "[*] Thank You For Using My Script")
            print("[-] Proceeding Script Termination")
            exit()
        else:
            print("\n\n\n" + "[!] Selection Not Found On The List")
            print("[-] Redirecting You Automatically...")
            time.sleep(1.50)
            C1()
    except ConnectionAbortedError:
        print("\n\n\n" + "[!] Error Found: ConnectionAbortedError")
        print("[-] Proceeding Script Termination")
        exit()
    except ConnectionRefusedError:
        print("\n\n\n" + "[!] Error Found: ConnectionRefusedError")
        print("[-] Proceeding Script Termination")
        exit()
    except ConnectionResetError:
        print("\n\n\n" + "[!] Error Found: ConnectionResetError")
        print("[-] Proceeding Script Termination")
        exit()
    except ConnectionError:
        print("\n\n\n" + "[!] Error Found: ConnectionError")
        print("[-] Proceeding Script Termination")
        exit()
    except ValueError:
        print("\n\n\n" + "[!] Invalid Choice")
        print("[-] Redirecting You Automatically...")
        time.sleep(1.50)
        C1()
    except TypeError:
        print("\n\n\n" + "[!] Invalid Choice")
        print("[-] Redirecting You Automatically...")
        time.sleep(1.50)
        C1()
    except KeyboardInterrupt:
        print("\n\n\n" + "[!] Script Terminated By 'CTRL+Z'")
        print("[*] Thank You For Using My Script")
        print("[-] Proceeding Script Termination")
        exit()
    except EOFError:
        print("\n\n\n" + "[!] Error Found: EOFError")
        print("[*] Thank You For Using My Script")
        print("[-] Proceeding Script Termination")
        exit()


if __name__ == "__main__":
    Clear()
    C1()

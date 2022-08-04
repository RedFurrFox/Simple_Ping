############################################################
"""                   Required Modules                   """
############################################################

import os
import requests

try:
    import yaml
except ModuleNotFoundError:
    print("pyyaml is missing... Automatically installing it for you.")
    os.system("python -m pip install pyyaml")

############################################################
"""                       Strings                        """
############################################################

Green = '\033[1;32;40m'
Yellow = '\033[1;33;40m'
Red = '\033[1;31;40m'
Cyan = '\033[1;36;40m'
White = '\033[0;37;40m'

Logo = f"""{Green}@@@@@@@   @@@  @@@  @@@   @@@@@@@@
@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@@
@@{Yellow}!  {Green}@@@  @@{Yellow}!  {Green}@@{Yellow}!{Green}@{Yellow}!{Green}@@@  {Yellow}!{Green}@@      
{Yellow}!{Green}@{Yellow}!  {Green}@{Yellow}!{Green}@  {Yellow}!{Green}@{Yellow}!  !{Green}@{Yellow}!!{Green}@{Yellow}!{Green}@{Yellow}!  !{Green}@{Yellow}!      
{Green}@{Yellow}!{Green}@@{Yellow}!{Green}@{Yellow}!   !!{Green}@  {Green}@{Yellow}!{Green}@ {Yellow}!!{Green}@{Yellow}!  !{Green}@{Yellow}! {Green}@{Yellow}!{Green}@{Yellow}!{Green}@
{Yellow}!!{Green}@{Yellow}!!!    !!!  !{Green}@{Yellow}!  !!!  !!! !!{Green}@{Yellow}!!
!!{Red}:       {Yellow}!!{Red}:  {Yellow}!!{Red}:  {Yellow}!!!  {Red}:{Yellow}!!   {Yellow}!!{Red}:
{Red}:{Yellow}!{Red}:       :{Yellow}!{Red}:  :{Yellow}!{Red}:  {Yellow}!{Red}:{Yellow}!  {Red}:{Yellow}!{Red}:   {Yellow}!{Red}::
 ::        ::   ::   ::   ::: ::::
 :        :    ::    :    :: :: : """

############################################################
"""                      Functions                       """
############################################################

def Terminal_Cleaner():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def Ping(url, timeout):
    global reqg
    try:
        reqg = requests.get(url, timeout)
        print(f'[Console][Requests] Target Url: "{url}" || Status Code: "{reqg.status_code}" || ✔ [Requests Sent :: You Have Internet Access]')
        pass
    except requests.ReadTimeout:
        print(f'[Console][Requests] Target Url: "{url}" || Status Code: "{reqg.status_code}" || ✖ [Requests Blocked :: Auth/Server/DDoS Issue]')
        pass
    except (requests.ConnectTimeout, requests.ConnectionError):
        print(f'[Console][Requests] Target Url: "{url}" || Status Code: "{reqg.status_code}" || ✖ [Requests Not Sent :: No Internet]')
        pass
    except requests.RequestException:
        print(f'[Console][Requests] Invalid URl => "{url}"')
        pass

def Check_Tool_Version(url, timeout, version):
    global reqg
    try:
        reqg = requests.get(url, timeout).text
        if reqg == version:
            pass
        else:
            print('[Console][Warning] Outdated Tool\n')
    except (requests.ReadTimeout,requests.ConnectTimeout, requests.ConnectionError, requests.RequestException):
        pass

def Check_And_Create_Settings_Yaml():
    if os.path.exists("settings.yaml"):
        pass
    else:
        with open("settings.yaml", "w") as Writer:
            Writer.write("")

############################################################
"""                   Settings Reader                    """
############################################################

with open("settings.yaml", "r") as Reader:
    YML = yaml.safe_load(Reader)
    Ping_List = YML["Settings"]["Ping_List"]
    Timeout = YML["Settings"]["Default_Value"]["Timeout"]
    Version_Compare = YML["Settings"]["Version_Control"]["Compare"]
    Version_Self = YML["Settings"]["Version_Control"]["Version"]

############################################################
"""                    Main Function                     """
############################################################

def Main():
    print(Logo + Cyan + Version_Self + White)
    Check_Tool_Version(url=Version_Compare, timeout=Timeout, version=Version_Self)
    print("\n\nChecking Your Internet Please Wait...")
    for Item in Ping_List:
        print(Item)
        Ping(url=str(Item), timeout=int(Timeout))
    print("Session Finished!!! Exiting...")
    exit()




############################################################
"""                     Main Runner                      """
############################################################

if __name__ == "__main__":
    Terminal_Cleaner()
    Main()

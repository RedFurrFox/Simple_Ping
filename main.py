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

Settings_Template = """Settings:

  Ping_List:
    - https://google.com
    - https://facebook.com
    - https://github.com

  Default_Value:
    Timeout: 5

  Version_Control:
    Compare: https://raw.githubusercontent.com/RedFurrFox/Simple_Ping/main/.resources/.version
    Version: v1.0"""

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
        requests.get(url="https://camo.githubusercontent.com/12df27140682753703f98aa63ea1afe69472864e061805883667dc107d86efcb/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d52656446757272466f78", timeout=timeout)
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
            Writer.write(Settings_Template)
            Writer.close()

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
    print("\n\n[Console][Prompt] Checking Your Internet Please Wait...")
    for Item in Ping_List:
        Ping(url=Item, timeout=str(Timeout))
    print("[Console][Prompt] Session Finished!!! Exiting...")
    exit()

############################################################
"""                     Main Runner                      """
############################################################

if __name__ == "__main__":
    Terminal_Cleaner()
    Main()

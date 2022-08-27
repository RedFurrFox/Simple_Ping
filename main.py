############################################################
"""                   Required Modules                   """
############################################################

import os
import requests

try:
    import yaml
except ModuleNotFoundError:
    try:
        
        print("yaml not found... Automatically installing it for you.")
        os.system("python -m pip install pyyaml")
        
    except:
        print('Error occurred while installing "yaml", please manually install it by typing "pip install pyymal".')

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
    - https://msn.com   
    - # Feel free to add more site here

  Default_Value:
    Timeout: 5

  Version_Control:
    Compare: https://raw.githubusercontent.com/RedFurrFox/Simple_Ping/main/.resources/.version"""

############################################################
"""                      Functions                       """
############################################################

def Terminal_Cleaner():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def Ping(purl, ptimeout):

    global reqg1

    try:
        reqg1 = requests.get(url=purl, timeout=ptimeout)
        print(f'[Console][Requests] Target Url: "{purl}" || Status Code: "{reqg1.status_code}" || ✔ [Requests Sent :: You Have Internet Access]')
        pass
    except requests.ReadTimeout:
        print(f'[Console][Requests] Target Url: "{purl}" || Status Code: "{reqg1.status_code}" || ✖ [Requests Blocked :: Auth/Server/DDoS Issue]')
        pass
    except (requests.ConnectTimeout, requests.ConnectionError):
        print(f'[Console][Requests] Target Url: "{purl}" || Status Code: "{reqg1.status_code}" || ✖ [Requests Not Sent :: No Internet]')
        pass
    except requests.RequestException:
        print(f'[Console][Requests] Invalid URl => "{purl}"')
        pass

def Check_Tool_Version(ctvurl, ctvtimeout, ctvversion):
    
    global reqg2

    try:
        requests.get(url="https://camo.githubusercontent.com/12df27140682753703f98aa63ea1afe69472864e061805883667dc107d86efcb/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d52656446757272466f78", timeout=ctvtimeout)
        reqg2 = requests.get(url=ctvurl, timeout=ctvtimeout).text

        if reqg2 == ctvversion:
            pass
        else:
            print('[Console][Tip] Outdated Tool... Please run "git fetch" command inside on this directory to update this tool.\n')

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
"""                     Data Reader                      """
############################################################

try:
    with open("settings.yaml", "r") as Reader_1:
        
        YML = yaml.safe_load(Reader_1)
        Ping_List = YML["Settings"]["Ping_List"]
        Timeout = YML["Settings"]["Default_Value"]["Timeout"]
        Version_Compare = YML["Settings"]["Version_Control"]["Compare"]
        
except FileNotFoundError:
    with open("settings.yaml", "w") as Writter:
        
        Writter.write(Settings_Template)
        Writter.close()
        
    print("[Console][Tips] Missing Required Files Added. Please Re-run The Script.")
    exit()

try:
    with open(r"../Simple_Ping/.resources/.version", "r") as Reader_2:
        Version_Self = Reader_2.read()
except (FileNotFoundError,FileExistsError):
    print('[Console][Warning] Missing Required Files For Checking Tool Version... Skipping.\n[Console][Tips] Please run "git fetch" command inside on this directory to update this tool.')
    pass

############################################################
"""                    Main Function                     """
############################################################

def Main():
    
    print(Logo + Cyan + Version_Self + White)
    Check_Tool_Version(ctvurl=Version_Compare, ctvtimeout=Timeout, ctvversion=Version_Self)
    print("\n\n[Console][Prompt] Checking Your Internet Please Wait...")

    while True:

        for Item in Ping_List:
            if Item is None:
                continue

            Ping(purl=Item, ptimeout=Timeout)

        print("[Console][Prompt] Session Finished!!! Exiting...")
        exit()

############################################################
"""                     Main Runner                      """
############################################################

if __name__ == "__main__":
    Terminal_Cleaner()
    
    if os.path.isfile("settings.yaml"):
        Main()
    else:
        with open("settings.yaml", "w") as Writter:
            
            Writter.write(Settings_Template)
            Writter.close()
            
        Main()

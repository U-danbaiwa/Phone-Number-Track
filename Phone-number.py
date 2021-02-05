import requests
import os
import sys
#import scan
#import httplib
#import urllib2
#import subprocces
import time
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
print("")
os.system("clear")
os.system("figlet U-danbaiwa")
print(yellow,"\t\t\tv 1.0.0")
print(cya,"\t\t coded by U-danbaiwa")
print(green,bold,"\t\tPHONE NUMBER INFO")
print("\n\n")
print(cy,"\t*******************************************")
print(yellow,bold,"\tSEE PHONE NUMBER INFO HERE")
print(cy,"\t*******************************************")
print(green,"**********************************************")
code=input(green,"Enter Number Country Code: ")
print(green,"**********************************************")
print("")
print(green,"**********************************************")
num=input(cyan,"Enter Phone Number: ")
print(green,"**********************************************")
print("")
print(cy,"please wait...")
time.sleep(5)
response = requests.get("https://phonevalidation.abstractapi.com/v1/?api_key=4e21d9cc6e7d41b785d3e4c5297f1b28&phone="+code+num)
print(green,"[*] Victim Status code[<======>]",response.status_code)
print("")
print(yellow,"[*] Victim Phone Number[<======>]",response.json()["phone"])
print("")
print(cya,"[*] Phone Number It Work[<======]",response.json()["valid"])
print("")
print(cyan,"[*] international Call[<======>]",response.json()["format"]["international"])
print("")
print(yellow,"[*] Local Call[<======>]",response.json()["format"]["local"])
print("")
print(green,"[*] Country Name[<======>]",response.json()["country"]["name"])
print("")
print(cy,"[*] Code[<======]",response.json()["country"]["code"])
print("")
print(yellow,"[*] Country Call Code[<======>]",response.json()["country"]["prefix"])
print("")
print(cyan,"[*] Victim Location[<======>]",response.json()["location"])
print("")
print(green,"[*] Device Type[<======>]",response.json()["type"])
print("")
print(cy,"[*] SimCard Company Name[<======>]",response.json()["carrier"])
print("\n\n")
print(green,bold,"\t\t\tFollow me on github U-danbaiwa")
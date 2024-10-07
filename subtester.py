#!/usr/bin/python3

import requests
import argparse
from colorama import Fore as f
import os 
import socket as s

argparser = argparse.ArgumentParser(description="Description : Test subdomains --> subtester -l [wordlist]")

argparser.add_argument("-l", "--list", help="URL list .")
args = argparser.parse_args()


os.system('cls' if os.name == 'nt' else 'clear')

def showBanner() :
    print()
    print(f.YELLOW + "        _____ __  ______ _________________________________ ")
    print(f.GREEN + "       / ___// / / / __ )_  __/ ____/ ___/_  __/ ____/ __ \\")
    print(f.BLUE + "       \__ \/ / / / __  |/ / / __/  \__ \ / / / __/ / /_/ /")
    print(f.GREEN + "      ___/ / /_/ / /_/ // / / /___ ___/ // / / /___/ _, _/ ")
    print(f.YELLOW + "     /____/\____/_____//_/ /_____//____//_/ /_____/_/ |_|  ")
    print()
    print(f.WHITE + "     v 1.5.0")
    print("     developed by kindkali")
    print()
    print()

url_list = open(args.list, "r")
scheme = ""
c = f.WHITE
isFind = False


showBanner()

try : 
    for url in url_list :
        try : 
            try : 
                req = requests.get(url)
                isFind = True
            except requests.exceptions.MissingSchema : 
                try : 
                    req = requests.get(f"https://" + url[:-1])
                    scheme = "https://"
                    isFind = True
                except requests.exceptions.ConnectionError : 
                    req = requests.get(f"http://" + url[:-1])
                    scheme = "http://"
                    isFind = True
        except requests.exceptions.ConnectionError : 
            print(f.WHITE + "[" + f.RED + " x " + f.WHITE + "]   " + f.RED + "ERROR")
            isFind = False

        
        if isFind == True : 
            sc = req.status_code
            
            if 200 <= sc <= 299 : 
                c = f.GREEN
            elif 300 <= sc <= 399 : 
                c = f.YELLOW
            elif 400 <= sc <= 499 : 
                c = f.RED
            elif 500 <= sc <= 599 : 
                c = f.RED
        
            ip_addr = s.gethostbyname(url[:-1])
            
            print(f.WHITE + "[" + c + str(sc) + f.WHITE + "]   " + scheme + url[:-1] + "   [" + c + ip_addr + f.WHITE + "]  ")
except KeyboardInterrupt : 
    print(f.BLUE + "\n" + ("." * 28) + "-< Terminated >" + ("." * 28) + f.WHITE + "\n")


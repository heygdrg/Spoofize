import requests
from os.path import join
import os 
from pystyle import *
import time

banner1 = """
 _______  _____   _____   _____  _______ _____ ______ _______
 |______ |_____] |     | |     | |______   |    ____/ |______
 ______| |       |_____| |_____| |       __|__ /_____ |______
                                                           
"""


banner = """
╔═══════════════════════════════════╗ 
║         Mass Leave                ║ 
║       By rattler / heygdrg        ║ 
╚═══════════════════════════════════╝
"""
def input_set():
    return f'{Col.purple}[{Col.dark_blue}?{Col.purple}]{Col.dark_blue}'

def print_set():
    return f'{Col.purple}[{Col.dark_blue}!{Col.purple}]{Col.dark_blue}'


def get_middle():
    return '                                            '

def check_token(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
        
    if r.status_code == 200:
        pass
    else:
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[!] Invalid Token") , 1))
        input(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[!] Enter anything to continue. . . ") , 1))
        os.system('cls')
        main(banner, banner1)

def getheaders(token):
    headers = {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    }

    if token: 
        headers["Authorization"] = token
    return headers

def get_guild():
    global guild_requests
    guild_requests = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token))

def write_on_file(payload):
    with open(f'{payload["name"]}.txt', 'a+')as file:
            file.write(payload["content"])


def leave_guild(guild_id):
    global r
    header = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE2MTg4NCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        'authorization' : token
    }
    
    r = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild_id}", headers=header)

def get_menu():
    print(Center.XCenter(Colorate.Color(Col.pink, banner1)))

def get_banner():
    
    print(Center.XCenter(Colorate.Color(Col.purple, banner)))

def get_title(user_check,user_spoof):
    os.system(f'Title - Spoofize - User check : {user_check}  User spoof : {user_spoof}')


def mass_leave():
    
    get_guild()

    for guild in guild_requests:
        
        guild_id = guild['id']
        
        payload = {'name' : 'guild',
                    'content' : f'{guild_id}\n'}
        write_on_file(payload)
        
        for _guild_ in guild_requests:
            try:
                leave_guild(guild_id)
                
                if r.status_code == 400:
                    print(Center.XCenter(Colorate.Color(Col.dark_blue, f"{get_middle}{print_set()}{Col.red}can't leave : {Col.pink}{guild_id}{Col.blue}")))
                    input(Center.XCenter(Colorate.Color(Col.dark_blue, f'{get_middle}{input_set()}{Col.blue} Enter anything to {Col.pink}continue{Col.blue}')))
                    time.sleep(2)
                    main(banner,banner1)
                
                else:
                    print(Center.XCenter(Colorate.Color(Col.dark_blue, f'{get_middle}{print_set()}{Col.green} leaving {Col.pink}{guild["name"]}{Col.blue}')))
                    input(Center.XCenter(Colorate.Color(Col.dark_blue, f'{get_middle}{input_set()}{Col.blue} Enter anything to {Col.pink}continue{Col.blue}')))
                    time.sleep(2)
                    main(banner,banner1)
            except:
                print(Center.XCenter(Colorate.Color(Col.dark_blue, f"{get_middle}{print_set()}{Col.red}can't leave : {Col.pink}{guild_id}{Col.blue}")))
                input(Center.XCenter(Colorate.Color(Col.dark_blue, f'{get_middle}{input_set()}{Col.blue} Enter anything to {Col.pink}continue{Col.blue}')))
                time.sleep(2)
                main(banner,banner1)



def main(banner, banner1):
    
    global token
    global id 
    
    os.system(f'Title - Spoofize - @heygdrg - BKS#1958')
    
    get_menu()
    get_banner()

    self = input(Center.XCenter(Colorate.Color(Col.dark_blue, f"{get_middle()}{input_set()} Enter to {Col.pink}continue{Col.blue} : ")))
    
    os.system('cls')
    get_menu()
    token = input(Center.XCenter(Colorate.Color(Col.dark_blue, f"{get_middle()}{input_set()} Enter {Col.pink}token{Col.blue} : ")))
    check_token(token)
    mass_leave()



main(banner,banner1)
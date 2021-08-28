import requests as req
from colorama import Fore
from time import sleep
print(Fore.CYAN+"""
hello monster
""")
MONSTER_hp=input(Fore.GREEN+"Enter"+Fore.RED+"Number irancell"+Fore.GREEN+"=>")
print(Fore.GREEN+"please wait ...")
url=str("https://ziroapi.xyz/Apis/irancell/?phone="+MONSTER_hp)
r=req.get(url).text
r3=r.replace("@ZiroTM","@MONSTER_hp")
print(Fore.CYAN+r3)
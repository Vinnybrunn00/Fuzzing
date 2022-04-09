from os import system, name
from rich import print
import pyfiglet as pg
import requests
import time
import sys

clear = 'cls' if name == 'nt' else 'clear'
system(clear)

def Banner():
    banner = pg.figlet_format('Fuzzing')

    if sys.platform == 'linux':
        print(f'[bold][italic]{banner}[/] Version 1.0 \t OS: [italic][bold][cyan]Linux[/]\n\n')

    elif sys.platform == 'darwin':
        print(f'[bold][italic]{banner}[/] Version 1.0 \t OS: [italic][bold][cyan]MacOS[/]\n\n')

    elif sys.platform == 'win32':
        print(f'[bold][italic]{banner}[/] Version 1.0 \t OS: [italic][bold][cyan]Windows[/]\n\n')

    else:
        print(f'[bold][italic]{banner}[/] Version 1.0 \t OS: [italic][bold][red]Not Found[/]\n\n')


def Fuzzing():

    try:
        Banner()
        site = input(f'[$] Website: ')
        wordlist = eval(input('[$] Drag the wordlist here: '))
        
        with open(f"{wordlist}", 'r') as file:
            arquivo = file.read()
            lista = arquivo.split('\n')

            for i in lista:
                qq = requests.get(site + i)

                if qq.status_code == 200:
                    print(f'[cyan][*] {site}{i} - {qq.status_code}[/]')
                    time.sleep(1)

                elif qq.status_code == 404:
                    print(f'[red][*] {site}{i} - {qq.status_code}[/]')
                    time.sleep(1)

                elif qq.status_code == 401:
                    print(f'[yellow][*] {site}{i} - {qq.status_code}[/]')
                    time.sleep(1)

    except:
        system(clear)
        print(
            "[italic][red]Check the url or the imported file.[/]\n"
            "[italic][red]https://' and the forward slash(/) after the '.com' in the url are required.[/]"
            )

Fuzzing()
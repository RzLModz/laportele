import lzma
import zlib
import codecs
import base64
import pytz
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));import os
os.system("pip install pyfiglet")
os.system("pip install requests")
os.system('pip install webbrowser')
os.system('pip install user_agent')
os.system('clear')
import requests,random,pyfiglet,webbrowser,sys,time
from random import randint
from user_agent import generate_user_agent as ua
from datetime import datetime
from pytz import timezone
now = datetime.now(timezone('Asia/Jakarta'))
west_indo_day = now.strftime("%A")  # Full weekday name (e.g., Sunday)
west_indo_time = now.strftime("%d %B %Y %H:%M:%S")
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("TELEGRAM AUTO REPORT")
print(a_bSa+ab)
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

    print(f"{RED}Date >> {MAGENTA}{west_indo_day} {west_indo_time}{RESET}\n"
      f"{RED}DEVELOPER >> {YELLOW}@OverloadServer{RESET}\n"
      f"{RED}JOIN >> {MAGENTA}T.ME/POWERPROOFOVERLOAD{RESET}")
def R(m, email, num):
    res = requests.get('https://telegram.org/support',headers={"Host": "telegram.org","cache-control": "max-age=0","sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "cross-site","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://www.google.com/","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"}).cookies;stel=res['stel_ssid'];data=f'message={m}&email={email}&phone={num}&setln=';req=requests.post('https://telegram.org/support',data=data,headers={"Host": "telegram.org","cache-control": "max-age=0","sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://telegram.org","content-type": "application/x-www-form-urlencoded","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://telegram.org/support","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5","cookie":f"stel_ssid={stel}"}).text;print();#print((req.split('class="alert alert-success"><b>')[1].split('<')[0]))
 
if "Thanks" in req.text: 
    print(f'{G}[√]REPORT{E}==>{B} SUCCESS {E}| {G}{E}{B} {G}FROM{E}==> \033[35;m{email}{B} \nTHIS TOOL IS MADE BY @OverloadServer\n')
else:
  print("Error Report")
u=input(
"\033[30;m[×] Enter Username of scammer : "
)
m = """Hello sir/ma'am,

I would like to report a Telegram user who is engaging in suspicious and harmful activities. Their username is """+u+""" . I believe they may be involved in scams and phishing attempts, which is causing harm to the community. I would appreciate it if you could look into this matter and take appropriate action.

Thank you for your attention to this matter.


"""

names = ["Rakesh","rsmesh","Aman","avishek","mohan","Neha","akhilesh","sayam.","robin","rahul","dev","meera","Anushka","akshita","manjeet","manoj","rakhi","rampal","sonu","Subhashree","Lakhan","mohit","mohini","kakoli","prince","karan","sushila","sushil","Krishna","Ankit","prakash"]

while True:
 num="+91",randint(9392823620,9994997058)
 email = f'{random.choice(names)}{randint(9392820,9994958)}@gmail.com'
 
 
 R(m,email,num)


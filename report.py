import lzma
import zlib
import codecs
import base64
import pytz
import requests
import os
os.system("pip install pyfiglet")
os.system("pip install requests")
os.system('pip install webbrowser')
os.system('clear')
import random,pyfiglet,webbrowser,sys,time
from random import randint
from datetime import datetime
from pytz import timezone
from time import sleep

# --- Definisi Warna (Dipindahkan ke sini agar dapat diakses lebih awal) ---
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

# --- Fungsi untuk Memuat Proxy dari URL ---
def load_proxies_from_url(url="https://proxy.webshare.io/api/v2/proxy/list/download/joagployahcfvuhpmnngjyhfihzdvuckbmxfafhn/-/any/username/ip/-/"):
    """
    Memuat daftar proxy dari URL yang diberikan.
    Akan mencoba memparse format ip:port:username:password atau username:password@ip:port
    dan mengonversinya menjadi http://username:password@ip:port atau http://ip:port.
    """
    proxies = []
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        for line in response.text.splitlines():
            stripped_line = line.strip()
            if not stripped_line:
                continue

            # Inisialisasi default
            ip = ""
            port = ""
            username = ""
            password = ""
            formatted_proxy = ""

            # Kasus 1: Format username:password@ip:port
            if "@" in stripped_line:
                # Memastikan skema http:// ditambahkan
                if not stripped_line.startswith("http://") and not stripped_line.startswith("https://"):
                    formatted_proxy = f"http://{stripped_line}"
                else:
                    formatted_proxy = stripped_line
            else:
                # Kasus 2: Mencoba memparse format ip:port:username:password
                parts = stripped_line.split(':')
                if len(parts) == 4: # ip:port:username:password
                    ip = parts[0]
                    port = parts[1]
                    username = parts[2]
                    password = parts[3]
                    formatted_proxy = f"http://{username}:{password}@{ip}:{port}"
                elif len(parts) == 2: # ip:port
                    ip = parts[0]
                    port = parts[1]
                    formatted_proxy = f"http://{ip}:{port}"
                else:
                    # Jika format tidak dikenal, coba tambahkan http:// saja dan biarkan requests handle
                    print(f"{S}[!] Peringatan: Format proxy tidak standar terdeteksi: '{stripped_line}'. Mencoba memformat sederhana.{B}")
                    if not stripped_line.startswith("http://") and not stripped_line.startswith("https://"):
                        formatted_proxy = f"http://{stripped_line}"
                    else:
                        formatted_proxy = stripped_line
            
            if formatted_proxy:
                proxies.append(formatted_proxy)
            else:
                print(f"{E}[!] Tidak dapat memparse atau memformat baris proxy: {stripped_line}{B}")

        print(f"{G}[+] Berhasil memuat {len(proxies)} proxy dari {url}{B}")
        return proxies
    except requests.exceptions.RequestException as e:
        print(f"{E}[!] Error memuat proxy dari URL '{url}': {e}{B}")
        return []

# Muat proxy saat startup script dari URL yang baru
proxies_list = load_proxies_from_url("https://proxy.webshare.io/api/v2/proxy/list/download/joagployahcfvuhpmnngjyhfihzdvuckbmxfafhn/-/any/username/ip/-/")

hari_id = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu"
}
now = datetime.now(timezone('Asia/Jakarta'))
west_indo_day = hari_id[now.strftime("%A")]
west_indo_time = now.strftime("%d %B %Y %H:%M:%S")

ab = pyfiglet.figlet_format("TELEGRAM AUTO REPORT")
print(a_bSa+ab)

def to(message):
    for char in message + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

my_string = (f"\033[31;m Date >> \033[31;m{west_indo_day} {west_indo_time}\n\033[1;31mDEVELOPER >>\033[1; @Overloadserver \n\033[31;mJOIN >> \033[1;36m T.ME/POWERPROOFOVERLOAD \n")

to(my_string)  

def R(m, email, num, proxy): 
    """
    Mengirim laporan ke Telegram menggunakan proxy yang diberikan.
    """
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    
    headers_get = {
        "Host": "telegram.org",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://www.google.com/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    }

    try:
        initial_response = requests.get('https://telegram.org/support', headers=headers_get, proxies=proxies, timeout=10)
        initial_response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"{E}[!] Error mendapatkan respons awal dengan proxy {proxy}: {e}{B}") 
        return False 

    stel_ssid = initial_response.cookies.get('stel_ssid')
    data=f'message={m}&email={email}&phone={num}&setln='
    
    headers_post = {
        "Host": "telegram.org",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "origin": "https://telegram.org",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://telegram.org/support",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    }
    
    if stel_ssid:
        headers_post["cookie"] = f"stel_ssid={stel_ssid}"

    try:
        response = requests.post('https://telegram.org/support', data=data, headers=headers_post, proxies=proxies, timeout=10)
        response.raise_for_status() 
        print(f'{G}[√]REPORT{E}==>{B} SUCCESS {E}| {G}{E}{B} {G}FROM{E}==> \033[35;m{email}{B} \nTHIS TOOL IS MADE BY @OverloadServer\n')
        return True 
    except requests.exceptions.RequestException as e:
        print(f"{E}[!] Error mengirim laporan dengan proxy {proxy}: {e}{B}") 
        return False 
            
u = input("\033[30;m[×] Masukkan Username scammer: ")

m = """Hello sir/ma'am,

Saya ingin melaporkan pengguna Telegram yang terlibat dalam aktivitas mencurigakan dan berbahaya. Nama pengguna mereka adalah """+u+""" . Saya yakin mereka mungkin terlibat dalam upaya penipuan dan phishing, yang menyebabkan kerugian bagi komunitas. Saya akan sangat menghargai jika Anda dapat menyelidiki masalah ini dan mengambil tindakan yang sesuai.

Terima kasih atas perhatian Anda terhadap masalah ini.


"""

names = ["Rakesh","rsmesh","Aman","avishek","mohan","Neha","akhilesh","sayam.","robin","rahul","dev","meera","Anushka","akshita","manjeet","manoj","rakhi","rampal","sonu","Subhashree","Lakhan","mohit","mohini","kakoli","prince","karan","sushila","sushil","Krishna","Ankit","prakash"]

def generate_nomor_indonesia():
    kode_area = ["811", "812", "813", "851", "821", "822", "823", "895", "896", "831", "817"]  
    kode_area_terpilih = random.choice(kode_area)
    nomor_telepon = str(random.randint(10000000, 99999999))
    nomor_lengkap = f"+62{kode_area_terpilih}{nomor_telepon}"
    return nomor_lengkap

while True:
    if not proxies_list:
        print(f"{E}Tidak ada proxy yang tersedia. Mencoba memuat ulang dari URL...{B}")
        proxies_list = load_proxies_from_url("https://proxy.webshare.io/api/v2/proxy/list/download/joagployahcfvuhpmnngjyhfihzdvuckbmxfafhn/-/any/username/ip/-/")
        if not proxies_list: 
            print(f"{E}Tidak dapat memuat proxy dari URL. Menghentikan script.{B}")
            break

    proxy = random.choice(proxies_list)
    num = generate_nomor_indonesia()
    email = f'{random.choice(names)}{randint(9392820,9994958)}@gmail.com'
   
    R(m, email, num, proxy)
    sleep(2)
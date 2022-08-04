# !/usr/bin/python3.10
# -*- coding: utf-8 -*-
# Author:_TRISA_
# File:1.py
# Time:2022/8/4 21:53
# Software:PyCharm
# Email:1628791325@QQ.com
# -U2hhcmUlMjBhbmQlMjBMb3Zl-base64

import requests
from pathlib import Path
import json
import sys,time

curFileDir = Path(sys.argv[0]).parent
try:
    with open(curFileDir / "config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

except:
    print("载入配置文件出错")
    exit(0)

headers: dict = config["headers"]
ext = config["ext"]
authkey = config["authkey"]
game_version = config["game_version"]

txt = open(curFileDir / "result.txt", "r", encoding = "utf-8")
cdk = txt.read()
key =[]
for i in range(0,len(cdk)):
    test = cdk[i]
    if cdk[i] == "\n":
        key.append(cdk[i-12:i])

while 1:
    for k in range(0,len(key)):
        cdkey = key[k]
        params = (
            ('sign_type', '2'),
            ('auth_appid', 'apicdkey'),
            ('authkey_ver', '1'),
            ('cdkey', cdkey),
            ('lang', 'zh-cn'),
            ('device_type', 'pc'),
            ('ext', ext),
            ('game_version', game_version),
            ('plat_type', 'pc'),
            ('authkey', authkey),
            ('game_biz', 'hk4e_cn'),
        )

        response = requests.get('https://hk4e-api.mihoyo.com/common/apicdkey/api/exchangeCdkey', headers=headers, params=params)
        print(response.text)
        time.sleep(5)
# except:
#     print("error")


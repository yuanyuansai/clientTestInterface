import json

import requests

url = "https://zyapi-test.zhouyunft.com/user/gateway/user/getUserInfo"
cookies = None
headers = {
    "Content-Type": "application/json",
    "appid": "1001",
    "appver": "2.0.0",
    "nonce": "",
    "signature": "1b221f9bfc96ccf6c42df4c61e51eed2b98ef629",
    "token": "77912cee-aa95-4cc5-925e-63803bd281ae1660207946737",

}
data = {}
print(type(url))
print(type(data))
print(type(json.dumps(data)))
print(type(headers))

res = requests.post(url, data=json.dumps(data),
                    cookies=cookies, headers=headers, verify=False).json()
print(res)

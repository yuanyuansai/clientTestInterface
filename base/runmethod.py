import requests

class RunMethod:

    def send_get(self,url,cookies=None,headers=None):

        res = requests.get(url,cookies=cookies,headers=headers,verify=False)
        return res

    def send_post(self,url,data=None,cookies=None,headers=None):

        res = requests.post(url,data=data,cookies=cookies,headers=headers,verify=False)
        return res

    def run_main(self,url,method,data=None,cookies=None,headers=None):

        requests.packages.urllib3.disable_warnings()
        res = None


        if method == 'GET':
            res = self.send_get(url,cookies,headers)
        else:
            res = self.send_post(url,data=data,cookies=cookies,headers=headers)

        #响应的捕捉异常
        res1=None
        try:
            res1=res.json()
        except Exception as e:
            print("这是异常")
            print(e)
            print("这是异常")

        return res1
if __name__ == '__main__':
    url = "https://gl-test.1911edu.com/api/auth/login"
    data = None
    cookies = None
    headers = {
        "cookie": "Path=/; Path=/; Path=/",
        "content-type": "application/json"
    }
    method = "POST"
    data = {
        "phone": "13888888888",
        "password": "59E778220E9785BF72D53B5297A45561",
        "code": "9999"
    }
    import json

    print(type(headers))
    data = json.dumps(data)
    r = requests.post(url, data=data, cookies=cookies, headers=headers, verify=False)
    # r=RunMethod().run_main(url, method, data,cookies,headers)
    print(type(r))
    print(r.text)
    print(r.headers)
    print(r.headers['Set-Cookie'])

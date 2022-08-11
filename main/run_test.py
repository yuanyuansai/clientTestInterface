# coding:utf-8
import sys
from util.operation_json import OperationJson
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import json
from util import connect_db, connect_redis
import os
import time


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        # self.send_mail = SendEmail()
        self.userDetail = self.Login()
        self.headers = {
            "Content-Type": "application/json",
            "appid": "1001",
            "appver": "2.0.0",
            "nonce": "",
            "signature": "1b221f9bfc96ccf6c42df4c61e51eed2b98ef629",

        }
        self.headers['token'] = self.userDetail['data']['token']

    def Login(self):
        url = "https://zyapi-test.zhouyunft.com/user/gateway/user/register"
        cookies = None
        headers = {
            "content-type": "application/json",
            "appid": "1001",
            "appver": "2.0.0",
            "nonce": "",
            "signature": "af51db73166acac0e1acc2d7ae6e2e94f25b8b50",

        }
        data = {
            "code": "1111",
            "phone": "13681319134",
            "systemVersion": "14.2",
            "inviteCode": "",
            "phoneModel": "iPhone 12"
        }

        method = "POST"

        import requests
        res = requests.post(url, data=json.dumps(data),
                            cookies=cookies, headers=headers, verify=False).json()
        return res

    # def carry_header(self):
    #     '''
    #     获取token
    #     '''
    #     r = ret = connect_db.OperationMysql().search_one()
    #     r1 = "jwtTokenKey_" + str(r) + "_app"
    #     token_442 = connect_redis.Operation_redis().search_string(r1)
    #     return {
    #         'authorization': token_442
    #     }

    # 程序执行的
    def go_on_run(self):
        print(self.headers['token'])
        print('------接口测试执行中,静等2分钟------')
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()  # 获取用例行数
        print('用例数：', rows_count - 1)
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                method = self.data.get_request_method(i)  # 请求方式
                request_data = self.data.get_data_for_json(i)  # 请求数据
                expect = self.data.get_expact_data(i)  # 获取预期结果
                header = self.data.is_header(i)  # 获取是否携带header
                depend_case = self.data.is_depend(i)  # 获取是否有case依赖
                contentType = self.data.get_contentType(i)
                hasUserId = self.data.get_userId(i)
                url = self.data.get_request_url(i)  # 请求地址
                print(url)
                # cookies = eval(OperationJson('../dataconfig/cookie').data)
                cookies = None

                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                # if header == 'write':
                #     res = self.run_method.run_main(url,method,request_data)
                #     op_header = OperationHeader(res)
                #     op_header.write_cookie()
                if header == 'yes':
                    # if contentType:
                    #     self.headers['content-type'] = contentType
                    res = self.run_method.run_main(url, method, request_data, cookies, self.headers)

                else:
                    res = self.run_method.run_main(url, method, request_data, self.headers)
                print(type(res['code']))
                print("expect",expect)
                print(type(expect))
                # isinstance(res, dict) and
                if  res['code'] == expect:
                    # 判断两个字符串相等     self.com_util.is_equal_dict(expect,res) == 0:判断结果相等写入pass
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    fail_count.append(i)  # 预期与实际不一样写入fail
                    print('请求失败接口地址:', url)
                    print('响应:', res)
                    self.data.write_result(i, json.dumps(res))
            else:
                continue

        # self.send_mail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

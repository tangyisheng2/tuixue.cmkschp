# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import os
import sys

# SSL
from OpenSSL import SSL
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS


absPath = os.path.abspath(__file__)  # 返回代码段所在的位置，肯定是在某个.py文件中
temPath = os.path.dirname(absPath)  # 往上返回一级目录，得到文件所在的路径
temPath = os.path.dirname(temPath)  # 在往上返回一级，得到文件夹所在的路径
sys.path.append(temPath)  # 添加该路径到搜索路径中

# Import Blueprint


context = SSL.Context(SSL.TLSv1_2_METHOD)


# context.use_privatekey_file('cert/3118405_agv.tangyisheng2.com.key')
# context.use_certificate_file('cert/3118405_agv.tangyisheng2.com.crt')
# context.load_client_ca('cert/3118405_agv.tangyisheng2.com.crt',
#                        )


class Debug(Resource):

    def get(self):
        """

        :return: Status 0 代表OK
        """
        return {'status': '0'}

    def post(self):
        # 获取arg
        parser = reqparse.RequestParser()
        parser.add_argument("key", type=int, required=True, help="Missing key or key should be int")
        args = parser.parse_args()
        # try:
        #     args["key"]
        # except:
        #     IndexError
        #     return -1
        return {'mes': args}


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
# 添加资源
api.add_resource(Debug, '/')

# 添加蓝图


# Blueprint Ref: http://www.bjhee.com/flask-ad6.html
# https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#use-with-blueprints
# Server config starts Here


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True)

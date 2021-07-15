# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   serverchan_helper.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import json
import requests


def serverchan_push(token, title, desp=""):
    """
    Serverchan推送
    :param token: Serverchan推送token
    :param title: 推送通知标题
    :param desp: 推送通知内容
    :return: serverchan API返回
    """
    if token == "":
        return
    url = f"https://sctapi.ftqq.com/{token}.send?title={title}&desp={desp}"
    response = requests.request("POST", url)

    return json.loads(response.text)

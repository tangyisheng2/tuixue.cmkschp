# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   serverchan_helper.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import json
import requests


def serverchan_push(title: str, desp=""):
    """
    Serverchan推送
    :param title: 推送通知标题
    :param desp: 推送通知内容
    :return: serverchan API返回
    """
    from main import sct_token

    url = f"https://sctapi.ftqq.com/{sct_token}.send?title={title}&desp={desp}"
    response = requests.request("POST", url)

    return json.loads(response.text)

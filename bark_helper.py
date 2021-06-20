#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :bark_helper.py
# @Time      :2021/6/20 7:27 PM
# @Author    :Eason Tang
import requests
import json


def bark_push(token: str, title: str, content):
    if token == "":
        return

    for ship in content:
        shipContent = beautify_results(ship)
        url = f"https://api.day.app/{token}"

        payload = json.dumps({
            "title": title,
            "body": shipContent
        })
        headers = {
            'Content-Type': 'application/json'
        }

        requests.request("POST", url, headers=headers, data=payload)


def beautify_results(contents):
    res = f"{contents['shipName']}在{contents['startDate']} {contents['goTime']}有："
    for seatType in contents['seatRemaining']:
        for key in seatType:
            res += f"{key}-{seatType[key]}张;"
    res = res.rstrip(";")  # 去掉末尾的分号
    return res

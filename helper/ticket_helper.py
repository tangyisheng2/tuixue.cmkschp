#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ticket_helper.py
# @Time      :2021/6/20 7:00 PM
# @Author    :Eason Tang


import requests
import json
import datetime


def request_sail_ticket(request_param, show_available_only=False):
    """
    获取剩余船票
    :param show_available_only: 只显示有船票的日期
    :param request_param: 请求参数
    :return: 格式化后的船票余量信息
    """
    url = "https://www.cmskchp.com/sailingsJson"

    payload = f"siteResJson={json.dumps(request_param)}"
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.cmskchp.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.cmskchp.com/sailings',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    }

    cnt = 0
    while cnt < 3:
        try:
            response = requests.request("POST", url, headers=headers, data=payload, timeout=3)
            result = message_process(json.loads(response.content), show_available_only)
            return result
        except requests.exceptions.Timeout:
            if cnt < 3:
                continue
            return -1


def message_process(message, show_available_only=False):
    """
    筛选原始数据
    :param show_available_only: 只显示有船票的日期
    :param message: 请求数据
    :return: 筛选后数据(Json)
    """
    res = []
    for ship_instance in message['message']:
        if show_available_only and ship_instance['totalRemainVolume'] == "0":
            break
        ticket_info = {
            "shipName": ship_instance['shipName'],
            "startDate": ship_instance['startDate'],
            "goTime": ship_instance['goTime'],
            "totalRemaining": ship_instance['totalRemainVolume'],
            "seatRemaining": [{seatType['seatTypeName']: seatType['num']}
                              for seatType in ship_instance['seatList']]
        }

        res.append(ticket_info)

    return res if res else None


def create_assist_date(datestart=None, dateend=None):
    """
    生成时间列表
    :param datestart: 开始时间
    :param dateend: 停止时间
    :return: 时间列表
    """
    # https://blog.csdn.net/joson1234567890/article/details/80946974
    # 创建日期辅助表

    if datestart is None:
        datestart = datetime.datetime.now().strftime('%Y-%m-%d')
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y-%m-%d')

    # 转为日期格式
    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    date_list = [datestart.strftime('%Y-%m-%d')]
    while datestart < dateend:
        # 日期叠加一天
        datestart += datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y-%m-%d'))
    return date_list


if __name__ == '__main__':
    ret = request_sail_ticket(request_param={
        "startSite": "SK",  # 蛇口港
        "endSite": "HKA",  # 香港机场
        "toDate": "2021-08-16"  # 乘船日期
    })
    print(ret)

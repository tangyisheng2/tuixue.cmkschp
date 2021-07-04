#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2021/6/20 7:00 PM
# @Author    :Eason Tang

from helper import request_sail_ticket, create_assist_date
from bark_helper import bark_push
import time

# ==================================
# Global Settings
# Github Action
enable_gh_action = False  # 启用GitHub Action
# Bark Push
enable_bark = False  # 启用Bark推送
bark_token = ""  # Bark推送ID
# Ticket Stuff
startSite = "SK"  # 始发站点
endSite = "HKA"  # 目标站点
startDate = "2021-08-1"  # 船票搜索日期
endDate = "2021-08-30"
show_available_only = True  # 只显示有票的日期
# ==================================

if __name__ == '__main__':
    toDate = create_assist_date(datestart=startDate, dateend=endDate)  # 船票的起止时间

    while True:
        for date in toDate:
            ret = request_sail_ticket(request_param={
                "startSite": startSite,  # 蛇口港
                "endSite": endSite,  # 香港机场
                "toDate": date  # 乘船日期
            },
                show_available_only=show_available_only)
            if ret is not None:
                print(f'{date}:{ret}')
                if enable_bark:
                    bark_push(token=bark_token, title="船票Get", content=ret)
            else:
                print(f'{date}:没有可用的船票')
        if enable_gh_action:
            break
        time.sleep(600)

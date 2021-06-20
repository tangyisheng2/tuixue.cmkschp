#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2021/6/20 7:00 PM
# @Author    :Eason Tang

from helper import request_sail_ticket, create_assist_date
from bark_helper import bark_push

# ==================================
# Global Settings
# Bark Push
enable_bark = False
bark_token = ""
# Ticket Stuff
startSite = "SK"
endSite = "HKA"
startDate = "2021-08-1"
endDate = "2021-08-18"
# ==================================

if __name__ == '__main__':
    toDate = create_assist_date(datestart=startDate, dateend=endDate)  # 船票的起止时间

    for date in toDate:
        ret = request_sail_ticket(request_param={
            "startSite": startSite,  # 蛇口港
            "endSite": endSite,  # 香港机场
            "toDate": date  # 乘船日期
        },
            show_available_only=True)
        if ret is not None:
            print(ret)
            if enable_bark:
                bark_push(token=bark_token, title="船票Get", content=ret)

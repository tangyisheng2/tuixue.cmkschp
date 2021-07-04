# 蛇口母港船票 自动爬取+推送通知

主要用于爬取蛇口母港-香港国际机场的船票，支持批量爬取以及Bark推送提醒。

注意⚠️：本项目仅供交流学习使用，请勿用于商业用途。同时，本系统只起到提醒作用，并不会自动帮您购买船票，请知悉。

# 安装

程序在Python 3.8与3.9测试通过。

安装依赖库：

```shell
pip install -r requirements.txt
```

# 使用

本程序的主要配置在`main.py`中设置。

```python
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
```

配置完成后运行`python3 main.py`自动抓取相应日期的船票。

![image](https://user-images.githubusercontent.com/16578638/124384063-47d8dd80-dd02-11eb-9cf3-f1dec9220b9c.png)


程序运行后将以Json格式输出数据。

# Bark推送(iOS Only)

安装好bark app，复制测试URL中的key至`main.py`中的`bark_token = ""`并且将`enable_bark = False`改为`True`

# Github Action定时任务

感谢@DolorHunter

在Github右上角，选择「Use this template」

![image](https://user-images.githubusercontent.com/16578638/124387285-7f4e8680-dd10-11eb-8d7e-95684aa94217.png)

选择一个炫酷的名字

![image](https://user-images.githubusercontent.com/16578638/124387328-b45ad900-dd10-11eb-85c6-6eeca13674b5.png)

在软件源创建好后，进入Action标签页，此时你应该能看见运行中的Action任务

![image](https://user-images.githubusercontent.com/16578638/124387355-d2c0d480-dd10-11eb-91e2-04b906d6680a.png)

在Jobs下面的Build中，点选Start Crawling and Barking查看软件爬取的船票信息

![image](https://user-images.githubusercontent.com/16578638/124387368-e835fe80-dd10-11eb-8309-abe5e0a13ec8.png)

任务设置为每天凌晨自动运行，如果想要修改运行频率，请到[这里](https://github.com/tangyisheng2/tuixue.cmkschp/blob/main/.github/workflows/Crawler.yml#L9)进行修改

如果想手动运行：

在Action下Workflows选择Crawler，并在右侧选择Run Workflow即可。

![image](https://user-images.githubusercontent.com/16578638/124387446-4e228600-dd11-11eb-9d0b-2b6fd50db1bb.png)



# 未来计划（不一定填坑）

- 加入Server Chan推送
- 前端网页
- 邮件推送

# Credits

感谢[tuixue.online](https://github.com/Trinkle23897/tuixue.online-visa) 的灵感。

**愿天下所有人都不用退学**

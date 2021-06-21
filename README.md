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
# Bark Push
enable_bark = False         # 启用Bark推送
bark_token = ""             # Bark推送ID
# Ticket Stuff
startSite = "SK"            # 始发站点
endSite = "HKA"             # 目标站点
startDate = "2021-08-1"     # 船票搜索日期
endDate = "2021-08-18"
show_available_only = True  # 只显示有票的日期
# ==================================
```

配置完成后运行`python3 main.py`自动抓取相应日期的船票。

![image](https://user-images.githubusercontent.com/16578638/122760727-04c44680-d2ce-11eb-85d7-296da2397c7b.png)

程序运行后将以Json格式输出数据。

# Bark推送(iOS Only)

安装好bark app，复制测试URL中的key至`main.py`中的`bark_token = ""`并且将`enable_bark = False`改为`True`

# 未来计划（不一定填坑）

- 前端网页
- 邮件推送

# Credits

感谢[tuixue.online](https://github.com/Trinkle23897/tuixue.online-visa) 的灵感。

**愿天下所有人都不用退学**

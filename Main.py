import requests
import bilibili
import re
import time
import os


# 尝试登陆
b = bilibili.Bilibili()
b.login(username=os.environ['account'], password=os.environ['password'])

# 获取 Cookie
cookie_str = ""
cookies = b.get_cookies()
for cookie in cookies:
    cookie_str += cookie + "=" + cookies[cookie] + "; "

headers_with_cookie={'User-Agent': "Mozilla/5.0 BiliDroid/6.4.0 (bbcallen@gmail.com) os/android model/M1903F11I mobi_app/android build/6040500 channel/bili innerVer/6040500 osVer/9.0.0 network/2",
                     'Cookie': cookie_str}

print("哔哩哔哩漫画开始签到 start>>>")

r = requests.post("https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn", verify=False, headers=headers_with_cookie, data={
    "platform": "android"
})

# print("响应: " + r.text)
if r.json()['code'] == 0:
    print("签到成功.")

time.sleep(2)

print("哔哩哔哩漫画获取签到信息 start>>>")
r = requests.post("https://manga.bilibili.com/twirp/activity.v1.Activity/GetClockInInfo", verify=False, headers=headers_with_cookie)

print("响应: " + r.text)

time.sleep(3)

print("哔哩哔哩银瓜子兑换硬币 start>>>")

print(b.silver_to_coin())
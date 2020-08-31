# Bilibili-Manga  漫画自动签到

### 这个程序有什么用?

可以帮助你自动登陆签到 B 站 \"哔哩哔哩漫画\" 


### 如何使用?

#### 方法一 使用 Github Actions(最简单, 推荐)

 B 站[视频教程](https://www.bilibili.com/video//).

**本项目需要设置的 Secrets:**

| 名称     | 内容          |
| -------- | ------------- |
| ACCOUNT  | 你的B站用户名 |
| PASSWORD | 你的B站密码   |

**本项目默认设置**: 每天早上 8 点打卡签到.

#### 方法二 直接运行 Python(不推荐)

1. 找任意一台安装好 Python 3.6 或以上版本的服务器
2. 在任意目录下执行 `git clone https://github.com/BlueskyClouds/Bilibili-Mangas && cd Bilibili-Mangas`
3. 使用 pip 安装依赖库, 参考命令`pip3 install requests rsa chardet`
4. 使用 Cron 每日执行 `python3 Main.py`


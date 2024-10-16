import requests

# 1. 获取单张图片
# 找到目标url
url = 'https://p1.music.126.net/07UIEegcZdOWiOvZoigpMg==/109951170046139514.jpg?imageView&quality=89'

# 构建请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# 发送请求，获取响应
# res = requests.get(url, headers=headers)

# 保存图片
# with open('网易云.jpg', 'wb') as f:
#     f.write(res.content)

# 2. 获取单手歌曲
url = 'https://m10.music.126.net/20241016171200/aeffb284e9fbc93c13ff5fde29bc54a6/yyaac/obj/wonDkMOGw6XDiTHCmMOi/3945547514/6c7d/4fb4/2def/e560cfe0e71e462bec4ef8efcdfadb5c.m4a'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
# res2 = requests.get(url, headers=headers)
# with open('网易云.mp3', 'wb') as f:
#     f.write(res2.content)

# 3. 爬取mv
# URL = 'https://api.bilibili.com/x/web-interface/card?mid=193262326&photo=1'
url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/IjAwMDYgIGEgISQgMDRiMg==/mv/308028/a7ccc18b3a5a236a612a8c6946c56a6f.mp4?wsSecret=3d347d0eaf573b27a3d515b5b31226fe&wsTime=1729071550'
url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/IjAwMDYgIGEgISQgMDRiMg==/mv/308028/a7ccc18b3a5a236a612a8c6946c56a6f.mp4?wsSecret=3d347d0eaf573b27a3d515b5b31226fe&wsTime=1729071550'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
# res3 = requests.get(url)
# with open('网易云.mp4', 'wb') as f:
#     f.write(res3.content)


# 4. 贴吧单页获取案例
url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
res4 = requests.get(url, headers=headers)
# print(res4.text)
with open('李毅.html', 'wb') as f:
    f.write(res4.content)


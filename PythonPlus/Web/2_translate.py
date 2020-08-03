"""
别试了，网易API现在收费了，爬不了了
"""
import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
text = 'mute'
head = {'Referer': 'http://fanyi.youdao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.105 Safari/537.36'}
data = {
    "type": "AUTO",
    "i": text,
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_CLICKBUTTON",
    "typoResult": "true"}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)

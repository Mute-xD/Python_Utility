"""
这个api是谷歌家的
所以
You Know
"""
import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
req = requests.get(url)
print('Status: ', req.status_code)
subIdsDict = dict()
subMissionDict = dict()
subMissionDictList = []
for subId in req.json()[:10]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(subId) + '.json'
    try:
        req = requests.get(url)
    except requests.exceptions.ProxyError:
        print('ProxyError!')
    if req.status_code is 200:
        print('.', flush=True, end='')
    else:
        print('!', flush=True, end='')
    respDict = req.json()
    subMissionDict = {'title': respDict['title'],
                      'link': 'http://news.ycombinator.com/item?id=' + str(subId),
                      'comments': respDict.get('descendants', 0)}  # 若无评论则返回0
    subMissionDictList.append(subMissionDict)
print('')
subMissionDictList = sorted(subMissionDictList, key=itemgetter('comments'), reverse=True)

for subMissionDict in subMissionDictList:
    print('--------------------------------------------------------------------------------------')
    print('Title: ', subMissionDict['title'])
    print('Discussion link :', subMissionDict['link'])
    print('Comments: ', subMissionDict['comments'])

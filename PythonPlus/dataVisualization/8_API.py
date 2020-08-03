import pygal.style
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rateLimitUrl = 'https://api.github.com/rate_limit'
rateLimit = (requests.get(rateLimitUrl)).json()
rateLimit = rateLimit['resources']['search']
print('Rate Limit', rateLimit['remaining'], '/', rateLimit['limit'])
resp = requests.get(url)
print("Status:", resp.status_code)
respDict = resp.json()
print('Total Repos: ', respDict['total_count'])

repoDict = respDict['items']
print('Repo returned: ', len(repoDict))
print('------------------------------每日精选（大误）------------------------------')
currentRepo = repoDict[0]
print('Keys: ', len(currentRepo))
print('Current repo information')
print('Name: ', currentRepo['name'])
print('Owner: ', currentRepo['owner']['login'])
print('Stars: ', currentRepo['stargazers_count'])
print('Repository: ', currentRepo['html_url'])
print('Created: ', currentRepo['created_at'])
print('Updated: ', currentRepo['updated_at'])
print('Description: ', currentRepo['description'])

repoNameList, repoStarDescription, repoLink = [], [], []
for i in range(len(repoDict)):
    repoNameList.append(str(repoDict[i]['name']))
    repoStarDescription.append({'value': int(repoDict[i]['stargazers_count']),
                                'label': str(repoDict[i]['description']),
                                'xlink': str(repoDict[i]['html_url'])})

myStyle = pygal.style.LightenStyle('#333366', base_style=pygal.style.LightColorizedStyle)
myConfig = pygal.Config()
myConfig.x_label_rotation = 45
myConfig.show_legend = False
myConfig.title_font_size = 24
myConfig.label_font_size = 14
myConfig.major_label_font_size = 18
myConfig.truncate_label = 15
myConfig.show_y_guides = False
myConfig.width = 1000

chart = pygal.Bar(config=myConfig, style=myStyle)
chart.add('Repo', repoStarDescription)
chart.x_labels = repoNameList
chart.title = 'Github上Star最多的Python项目（TOP30）'
chart.render_in_browser()
chart.render_to_file('1.svg')

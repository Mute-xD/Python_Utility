"""
json均以字符串形式存储各种格式，注意转换
pandas 太香了
TODO: 利用原生库迭代器实现
"""
import json
import math
import pygal
import pandas as pd

filePath = 'resource/btc_close_2017.json'
with open(filePath) as file:
    data = json.load(file)


def weekdayReplace(string: str):
    replace_dict = {'Monday': 'MON',
                    'Tuesday': 'TUE',
                    'Wednesday': 'WED',
                    'Thursday': 'THU',
                    'Friday': 'FRI',
                    'Saturday': 'SAT',
                    'Sunday': 'SUN'}
    for key, value in replace_dict.items():
        string = string.replace(key, value)
    return string


dateList, monthList, weekList, weekdayList, closeList = [], [], [], [], []
for dataDict in data:
    dateList.append(dataDict['date'])
    monthList.append(int(dataDict['month']))
    weekList.append(int(dataDict['week']))
    weekdayList.append(weekdayReplace(dataDict['weekday']))
    closeList.append(int(float(dataDict['close'])))

closeListLog = [math.log10(i) for i in closeList]


def Plot(x_data, x_label, title: str, x_name: str, is_render=False, improved_x=False):
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=not improved_x)
    line_chart.title = title
    line_chart.x_labels = x_label
    if improved_x:
        line_chart.x_labels_major = x_label[::20]
    line_chart.add(x_name, x_data)
    if is_render:
        line_chart.render_in_browser()


Plot(closeListLog, dateList, 'Close Price (RMB)', 'Close Price log10', False, True)

dataFrame = pd.DataFrame({'Date': dateList,
                          'Month': monthList,
                          'Week': weekList,
                          'WeekDay': weekdayList,
                          'Close': closeList})
gbMonthMean = dataFrame[['Month', 'Close']].groupby(dataFrame['Month']).mean()
gbWeekdayMean = dataFrame[['WeekDay', 'Close']].groupby(dataFrame['WeekDay']).mean()
weekdayNum = pd.DataFrame({'day': [1, 2, 3, 4, 5, 6, 7]}, index=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
gbWeekdayMean = gbWeekdayMean.join(weekdayNum).sort_values(by='day').drop('day', axis=1)
print(gbWeekdayMean.index.tolist())
Plot(gbMonthMean['Close'].tolist(), gbMonthMean['Month'].tolist(),
     'Close Price (RMB) in Month', 'Close Price', False)
Plot(gbWeekdayMean['Close'].tolist(), gbWeekdayMean.index.tolist(),
     'Close Price (RMB) in Weekday', 'Close Price', True)

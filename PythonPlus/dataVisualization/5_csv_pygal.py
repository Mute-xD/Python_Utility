import datetime
import csv
import pygal
fileName = 'resource/sitka_weather_2014.csv'
highTempList = []
dateList = []
lowTempList = []
with open(fileName) as file:
    rows = csv.reader(file)
    head = next(rows)  # 迭代器，调用一次返回值横向挪一列， 挪到最后触发异常， 可以添加第二参数规定末尾时的返回值
    for row in rows:
        highTempList.append(int(row[1]))
        lowTempList.append(int(row[3]))
        dateList.append(datetime.datetime.strptime(row[0], '%Y-%m-%d').date())
# highTempList = np.array(highTempList)
# print(highTempList)
# print(dateList)
# print(head)
linePic = pygal.Line(x_label_rotation=45, width=4000)
linePic.add('Highest Temp', highTempList)
linePic.add('Lowest Temp', lowTempList)
linePic.x_labels = dateList
# linePic.render_in_browser()
linePic.render_to_file('1.svg')

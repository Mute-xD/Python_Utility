import csv
import datetime
import matplotlib.pyplot as plt
fileName = 'resource/sitka_weather_2014.csv'
highTempList = []
dateList = []
lowTempList = []
with open(fileName) as file:
    rows = csv.reader(file)
    head = next(rows)
    for row in rows:
        highTempList.append(int(row[1]))
        lowTempList.append(int(row[3]))
        dateList.append(datetime.datetime.strptime(row[0], '%Y-%m-%d').date())

plt.plot(dateList, highTempList, c='r', alpha=0.5)
plt.plot(dateList, lowTempList, c='b', alpha=0.5)
plt.fill_between(dateList, highTempList, lowTempList, facecolor='b', alpha=0.1)
plt.show()

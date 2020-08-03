from pygalDice import Dice  # 3_pygalDice -> pygalDice
import pygal
dice1 = Dice()
dice2 = Dice(10)

resultsList = []
rollTime = 10000
for rollTimes in range(rollTime):
    result = dice1.rolling() + dice2.rolling()
    resultsList.append(result)

freqList = []
resultSum = dice1.diceSide + dice2.diceSide
for value in range(2, resultSum + 1):
    freqList.append(resultsList.count(value))

print(freqList)
hist = pygal.Bar()
hist.title = 'Result of Rolling Two Dice for ' + str(rollTime) + ' Times'
hist.x_labels = list(range(2, dice1.diceSide+dice2.diceSide+1))
hist.x_title = 'Result'
hist.y_title = 'Times'
hist.add('D'+str(dice1.diceSide)+' + '+'D'+str(dice2.diceSide), freqList)
hist.render_in_browser()
hist.render_to_file('1.svg')

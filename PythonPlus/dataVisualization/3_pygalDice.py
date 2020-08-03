"""
deploy pygal:
pip install pygal lxml cairosvg tinycss cssselect
render_to_png may not work
"""
import pygal
from random import randint


class Dice:
    def __init__(self, side=6):
        self.diceSide = side

    def rolling(self):
        return randint(1, self.diceSide)


if __name__ == '__main__':
    dice = Dice()
    resultList = []
    rollTime = 5000
    for rollTime in range(rollTime):
        result = dice.rolling()
        resultList.append(result)

    freqList = []
    for value in range(1, dice.diceSide + 1):
        freq = resultList.count(value)
        freqList.append(freq)
    print(freqList)

    hist = pygal.Bar()
    hist.title = 'Result of Rolling Dice for ' + str(rollTime + 1) + ' Times'
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = 'Result'
    hist.y_title = 'Times'
    hist.add('D6', freqList)
    hist.render_in_browser()

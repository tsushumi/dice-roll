
import random

one, two, three, four, five, six = 0, 0, 0, 0, 0, 0

for x in range(1, 1001):
    outcome = random.random()
    if outcome < 1/6:
        one = one + 1
    elif outcome < 2/6:
        two = two + 1
    elif outcome < 3/6:
        three = three + 1
    elif outcome < 4/6:
        four = four + 1
    elif outcome < 5/6:
        five = five + 1
    elif outcome < 6/6:
        six = six + 1

totalFrequency = one + two + three + four + five + six
totalPercentage = (totalFrequency / 1000 ) * 100

print('Face |   Frequency   |   Percentage')
print('-----------------------------------')
print('1        ', one, '         ', (one / 10), '%')
print('2        ', two, '         ', (two / 10), '%')
print('3        ', three, '         ', (three / 10), '%')
print('4        ', four, '         ', (four / 10), '%')
print('5        ', five, '         ', (five / 10), '%')
print('6        ', six, '         ', (six / 10), '%')
print('-----------------------------------')
print('Total:   ', totalFrequency, '        ', totalPercentage, '%')    
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def dice():
    return np.random.randint(1,7,(6,6))

def dropDice():
    return np.random.randint(1, 7, (4, 1))

if __name__ == '__main__':
    avg_max = 0
    dropLowestAvg = 0


    for i in range(100000):
        a = dropDice()
        a = np.delete(a, a.argmin())
        dropLowestAvg +=a.sum()
    print(dropLowestAvg*6 / 100000)
    for i in range(100000):
        curr_max = 0
        square = dice()+dice()+dice()

        curr_max = max(square.diagonal().sum(), curr_max)
        curr_max = max(np.flipud(square).diagonal().sum(), curr_max)

        for x in square.transpose():
            curr_max = max(x.sum(),curr_max)
        for x in square:
            curr_max = max(x.sum(), curr_max)
        avg_max += curr_max
    print(avg_max/100000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

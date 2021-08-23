"""
NOTE:
The error where all the elements change to the updated one

SOLVING:
- found out that the error is because the element in the list are lists
- problem not because of random

SOLUTION:
The program now doesn't just append the element to the list, it appends an empty 2-elemted-list, where one step further the program changes the the elements of the new list
"""

from random import randint

class Obj():

    def __init__(self) -> None:
        self.a = [[0,0]]
    
    def move(self):
        direction = randint(-1, 1)
        toChange = self.a[-1]

        if direction == 0:
            toChange[1] += 1
        else:
            toChange[0] += direction
        
        self.a.append([0,0])
        self.a[-1][0] = toChange[0]
        self.a[-1][1] = toChange[1]

o = Obj()

for i in range(21):
    o.move()

print(o.a)

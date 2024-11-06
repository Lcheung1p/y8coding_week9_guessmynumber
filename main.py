
from random import randint 


number = None
correct = randint(16,64)

while number != correct:
    print("guess my number")
    number = int(input())
    if number > correct:
        print("lower!")
    if number < correct:
        print("higher!")
    if number == correct:
        print("you won!!!!!!!")
    five_less = correct - 5
    five_more = correct + 5

    if number >= five_less and number <= five_more:
        print("almost! within 5 away")


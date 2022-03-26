
import random 
over = 0
for iterations in range(10000):
    flip_list = []
    number_of_six_streaks = 0

    for x in range(100):
        y = random.randint(0,1)
        flip_list.append(y)
    
    streak_counter = 0
    for index in range(len(flip_list)):
        if index == 0:
            pass
        elif flip_list[index] == flip_list[index-1]:
            streak_counter += 1
        
        else:
            streak_counter = 0

        if streak_counter == 5:
            number_of_six_streaks += 1

    if number_of_six_streaks:
        over += 1


print (f'The chance of 6-streaks is {over * (100/10000)} ')
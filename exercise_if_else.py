


# exercise of if else

'''
create a python program capable of greeting you with good morning good after noon and good evening. your program should use time module to get the current hour. '''


import time


current_time= time.strftime('%H:%M:%S')
print(current_time)

if int(time.strftime('%H')) >= 0 and int(time.strftime('%H')) <= 9:
    print("Good Morning")
elif int(time.strftime('%H')) > 9 and int(time.strftime('%H')) <= 4:
    print("Good afternoon")
else:
    print("Good Evening")
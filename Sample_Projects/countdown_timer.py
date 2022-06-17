import time
t = int(input("Enter desired timer "))
while t:
    min = t // 60
    sec = t % 60
    timer = '{:2d}:{:02d}'.format(min, sec)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1
print("Time over!")


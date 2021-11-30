import math

red = int(input("red ="))
green = int(input("green ="))
red_re = 0
green = 0

while(red > 0 and green > 0):
    red_d = math.ceil(red/3)
    green_d = math.ceil(green/4)
    red -= green_d
    green -= red_d
    red_re += red_d
    green_re += red_d
    red += math.ceil(red/8)
    green += math.ceil(green/6)
    hour += 1

if red == 0 and green == 0:
    print("Dran")
elif red != 0:
    print("red win")
    print("Green drones destroyed" + str(red))
    print(str(red)+"red drones remain")
else:
    print("Green")
    print(str(green)+"Green drones remain")
    print(str(green)+"Greeb drones remain")

import random
ps = random.sample(range(1,101), 1)
c = 0
y = 1
print('ไวน์ขวดที่ ',ps,(' มีพิษ'))
for e in range(1,11):
    print('คนที่ '+str(e)+' กินไวน์ขวดที่ '+str(y)+'-'+str(e)+'0 ห่างกัน 1 ซม. 00:00-09:00')
    e += 1
    y += 10

for i in range(1,11):
    t = 0
    for j in range(10):
        c += 1
        if c == int(ps[0]):
            print('คนที่',i,'ตายเวลา 0'+str(t)+':00')
            print('แสดงว่า ไวน์ ขวดที่ '+str(c)+' มีพิษ')
            break;
        t += 1
import random
n = int(input("Home :"))
g = random.sample(range(1,n+100),n)
print("money :",sum(g[::3]) )
from random import randint
n, N = 2000, 2000
points = {(randint(0, n), randint(0, n)) for i in range(N)}
while len(points) < N:
    points |= {(randint(0, n), randint(0, n))}
     
points = list(list(x) for x in points)

print(points)
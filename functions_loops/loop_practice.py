n = 0
while n <= 10:
    print('N =', n)
    n += 1
print('LOOP FINISHED')

for num in range(1, 11):
    print('Num =', num)
print('LOOP FINISHED')

for n in range(1, 4):
    for j in ['a', 'b', 'c']:
        print('n=', n, 'and j=', j)

for num in range(2, 11):
    print(num)

inter = 2
while inter <= 10:
    print(inter)
    inter += 1


def doubles(num):
    for i in range(1, 4):
        num = num * 2
        print(num)


doubles(4)

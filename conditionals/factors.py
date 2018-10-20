number = input('Enter a positive integer: ')
num = int(number)

for i in range(1, num + 1):
    if num % i == 0:
        print(f'{i} is a divisor of {num}')
   

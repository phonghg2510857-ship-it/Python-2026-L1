n = int(input('Enter a number?: '))
divisor_sum = 0
if n <= 1:
    print(f'{n} is not a perfect number')
else:
    for i in range(1, n):
        if  n % i == 0:
            divisor_sum += i
    if divisor_sum == n:
        print(f'{n} is a perfect number')
    else:
        print(f'{n} is not a perfect number')

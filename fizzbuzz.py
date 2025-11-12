for n in range(10, 30+1):
    if n % 3 == 0 or n % 5 == 0:
        print('fizz' * (n % 3 == 0) + 'buzz' * (n % 5 == 0))
    else:
        print(n)

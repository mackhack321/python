n = 1
while n <= 100:
    if n % 3 == 0 and n % 5 == 0:
        msg = 'fizzbuzz'
    elif n % 3 == 0:
        msg = 'fizz'
    elif n % 5 == 0:
        msg = 'buzz'
    else:
        msg = n
    print(msg)
    n = n + 1

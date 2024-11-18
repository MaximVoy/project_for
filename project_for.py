numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i !=1 and (i % 2 != 0 and i % 3 != 0):
        primes.append(i)
    elif i == 2 or i == 3:
        primes.append(i)
        continue
    elif i != 1 and (i % 2 == 0 or i % 3 == 0):
        not_primes.append(i)
print('numbers: ', numbers)
print('primes: ', primes)
print('not_primes: ', not_primes)



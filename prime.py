__author__ = 'Kaiming'


# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break




n = 100
L = [p for p in range(2, n) if 0 not in [p % d for d in range(2, int(p ** 0.5) + 1)]]

print(L)

n = 100
for i in range(2, n):
    flag = True
    if i == 2:
        L.append(i)
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
    if flag == True:
        L.append(i)
print(L)

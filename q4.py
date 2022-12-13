import math
def factors(number):
    return [(x, int(number / x))  for x in range(int(math.sqrt(number)))[2:] if not number % x]


x=1963
a= factors(x)
print(a[0][0])
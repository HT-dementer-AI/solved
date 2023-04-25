import decimal


def fibo(n):
    decimal.getcontext().prec = 10000

    a = decimal.Decimal(5).sqrt()
    b = ((1 + a)/2)

    a = ((b**n) - ((-b)**-n))/a

    return round(a)


n = int(input())

print(fibo(n))

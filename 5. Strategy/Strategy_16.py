def multof(nMin, nMax):
    def pfactors(n):

        total = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                total += d
                n //= d
            d += 1
        if n > 1:
            total += n
        return total
    def _sum(n):
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
            i += 1
        return total

    result = []
    for num in range(nMin, nMax + 1):
        pfs = pfactors(num)
        ds = _sum(num)
        if pfs > 0 and ds % pfs == 0:
            result.append(num)

    return result
print(multof(10, 100))
print(multof(20, 120))


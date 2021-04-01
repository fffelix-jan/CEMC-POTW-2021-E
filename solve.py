def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for i in range(10000, 100000):
    i_str = str(i)
    if i_str[2] == "0" and i_str[0] == i_str[3] and i_str[1] == i_str[4]:
        pf = prime_factors(i)
        if len(pf) == 5:
            for factor in pf:
                if factor % 2 == 0:
                    break
            else:
                print(i)

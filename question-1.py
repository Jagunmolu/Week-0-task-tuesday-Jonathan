def prime_number(prime):
    factors = [1, prime]
    if prime < 2:
        return f"{prime} is not a prime number. Negative numbers, zero and one cannot be prime numbers."
    for i in range (2, round(prime/2) + 1):
        if prime%i == 0:
            factors.append(i)
            
        factors.sort()
        
    if len(factors) > 2:
        return f"{prime} is not a prime number\n{factors}."
    else:
        return f"{prime} is a prime number."
        
        
print(prime_number(2000003))
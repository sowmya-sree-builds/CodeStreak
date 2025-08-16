# So an amstrong number is denoted like this 
# 153 = 1^3 + 5^3 + 3^3 = 153

def armstrong(n):
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s += d ** 3
        temp //= 10
    return s == n   # returns True if Armstrong, else False

# Test
print(armstrong(153))  # True
print(armstrong(123))  # False
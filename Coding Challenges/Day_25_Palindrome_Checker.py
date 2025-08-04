# Day 25: Palindrome Number Checker

n = int(input('Enter a number: '))
original = n
rev = 0
temp = abs(n)

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n < 0:
    rev = -rev

if n == rev:
    print(f'The given number {n} is a Palindrome')
else:
    print(f'Oh no! The given number {n} is not a Palindrome')

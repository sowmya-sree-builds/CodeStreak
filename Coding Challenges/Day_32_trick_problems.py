# Day 32: Program to swap the last two digits of a number

n = 12345

if n < 10:
    print("Can't swap, number has less than 2 digits")
else:
    last = n % 10
    second_last = (n // 10) % 10
    num = n // 100
    res = num * 100 + last * 10 + second_last
    print("Number after swapping last two digits:", res)

# Day 33: Program to find the second largest number in a list 
# without using sorting or built-in functions like max() or sorted()

nums = [11, 2, 3, 9, 2]
fir = sec = nums[0]

for i in nums:
    if i > fir:
        sec = fir
        fir = i
    elif i < fir and (sec == fir or i > sec):
        sec = i

print("Second largest number is:", sec)
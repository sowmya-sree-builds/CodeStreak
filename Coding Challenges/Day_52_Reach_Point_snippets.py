# def captofront(str):
#     arranged=''
#     for j in str:
#         if j.isupper():
#             arranged += j
#     for i in str:
#         if i.islower():
#             arranged +=i
#     return arranged
# print(captofront('HaPpY'))


# n = 10102
# sum=0
# reverse=0
# while n >0:
#     digit=n%10
#     reverse = reverse*10+digit
#     sum +=digit
#     n //= 10
# print(sum,reverse)


# str='wonder'
# if len(str)%2==0:
#     word=len(str)//2
#     print(str[word-1],str[word])
# else:
#     word=len(str)//2
#     print(str[word])

test=75547
temp=test
while temp>10:
    temp//=10
    first=temp
print(first)
n=test//10
sum=0
while n>10:
    d = n%10
    sum += d
    n//=10
test %= 10
sum1=first+test
print(sum1)
print(sum)
    

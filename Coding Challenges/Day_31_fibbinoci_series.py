#  to find the fibbinoci series for a range of numbers given

n = int(input('Enter a number:'))
n1 = 0
n2 = 1
# 0 1 1 2 3 5 8 13
for i in range(1,n):
    n3 = n1 + n2
    n2 = n1
    n1 = n3
    print(n3, end = ',')
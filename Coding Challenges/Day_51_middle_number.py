# Write a program to print middle character(s) in the given string or 
# number.  
# Testcase1 : Wonder  
# Output : nd  
# Explanation : The middle characters in the given word Wonder is nd.  
# Testcase1 : World  
# Output : r  
# Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
# Output : 96  
# Explanation : The middle character in the given number 6969 is 96. 

str1 = input('Enter a string: ')

if len(str1) % 2 == 0:
    word = len(str1) // 2
    print(str1[word - 1]+str1[word])
else:
    word = len(str1) // 2
    new = str1[word]
    print(new)


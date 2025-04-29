"""🧠 In this problem, you will be given the data of two arrays which contains duplicated numbers.
Now you need to remove duplicated numbers and find the median(output) of the sorted array.

Note: While finding the median, do not omit duplicates which are common in the cleaned input arrays.

Input Format:

Array 1 elements with spaces.

Array 2 elements with spaces.

Output Format:

Float value or int value depending upon the output.

Sample Input:

3112

43321

Output:

2

Explanation: Taking the input as two arrays a1: [3, 1, 1, 2) and a2: [4, 3. 3, 2, 11].

Now remove the duplicates and sort the arrays. And now find the median of the two sorted arrays"""

# Day 12 🧠 Challenge: Median from unique digits of one input

# Read input as a string of digits
digits = input().strip()

# Convert to a list of integers and remove duplicates
unique_digits = sorted(set(int(d) for d in digits))

# Calculate median
n = len(unique_digits)
if n % 2 == 1:
    median = unique_digits[n // 2]
else:
    median = (unique_digits[n // 2 - 1] + unique_digits[n // 2]) / 2

# Print median (as int if it's a whole number)
if median == int(median):
    print(int(median))
else:
    print(median)

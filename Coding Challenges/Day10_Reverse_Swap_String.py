# Day 10: Reverse Swap String

def reverse_swap_string(s):
    """
    Function to reverse a string and swap every alternate character.

    Parameters:
    s (str): The input string.

    Returns:
    str: The transformed string after reversing and swapping.
    """
    # Step 1: Reverse the string
    s = s[::-1]

    # Step 2: Convert to a list for swapping
    s = list(s)

    # Step 3: Swap every alternate character
    for i in range(0, len(s) - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]

    # Convert back to string and return
    return "".join(s)

# Example test cases
print(reverse_swap_string("hello"))   # Output: loleh
print(reverse_swap_string("abcdef"))  # Output: efdcba
print(reverse_swap_string("python"))  # Output: ytpnoh
print(reverse_swap_string("world"))   # Output: orwld

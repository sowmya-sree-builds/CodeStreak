# this code snippet is a small experiment to implement swap case functionality using just ascii values 
def custom_swapcase(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 65 <= ascii_val <= 90:   # Uppercase A-Z
            result += chr(ascii_val + 32)  # Convert to lowercase
        elif 97 <= ascii_val <= 122:  # Lowercase a-z
            result += chr(ascii_val - 32)  # Convert to uppercase
        else:
            result += ch  # Non-alphabetic characters remain same
    return result


# Example usage
text = "Hello World 123!"
print("Original:", text)
print("Swapped :", custom_swapcase(text))

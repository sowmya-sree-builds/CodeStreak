# Day 27: Find words with length less than 3

def short_words(sentence):
    words = sentence.split()
    return [word for word in words if len(word) <= 3]

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    result = short_words(text)
    print("Words with length less than 3:", result)

# Day 29: Words with exactly 2 vowels

def words_with_two_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = []
    for word in sentence.split():
        vowel_count = sum(1 for ch in word if ch in vowels)
        if vowel_count == 2:
            result.append(word)
    return result

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    words = words_with_two_vowels(sentence)
    print("Words with exactly 2 vowels:", " ".join(words))

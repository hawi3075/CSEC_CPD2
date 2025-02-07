def correct_word_case(word):
    
    uppercase_count = sum(1 for char in word if char.isupper())
    lowercase_count = len(word) - uppercase_count  

    
    if uppercase_count > lowercase_count:
        return word.upper()
    else:
        return word.lower()


word = input().strip()


print(correct_word_case(word))

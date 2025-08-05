def occurrences(text):
    text = text.lower()
    words = text.split()
    word_count = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1    
    return word_count
text = input("Enter text: ")
word_occurrences =occurrences(text)
print(word_occurrences)

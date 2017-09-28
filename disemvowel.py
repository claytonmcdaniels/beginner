def disemvowel(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    word_list = list(word)
    for letter in word:
        if letter in vowels:
            word_list.remove(letter)
        word = ''.join(word_list)
    return word
disemvowel(word)
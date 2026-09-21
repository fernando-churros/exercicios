def is_pangram(sentence, letters):
    sentence_list = []
    for letter in sentence:
        if not letter.isalpha(): continue
        sentence_list.append(letter.lower())

    sentence = ''.join(sentence_list)

    for letter in letters:
        if not letter in sentence: return False

        count = sentence_list.count(letter)
        for x in range(0, count):
            sentence_list.remove(letter)

    if len(sentence_list) != 0: return False

    return True

print(is_pangram("hello", "helo"), 'true') # return True
print(is_pangram("hello", "hel"), 'false') # return False
print(is_pangram("hello", "helow"), 'false') # return False
print(is_pangram("hello world", "helowrd"), 'true') # return True
print(is_pangram("Hello World!", "helowrd"), 'true') # return True
print(is_pangram("Hello World!", "heliowrd"), 'false') # return False
print(is_pangram("freeCodeCamp", "frcdmp"), 'false') # return False
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"), 'true') # return True

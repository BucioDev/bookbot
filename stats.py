def count_words(book):
    words = book.split()
    return len(words)


def count_char(book):
    words = book.split()
    characters = {}
    for word in words:
        lower_word = word.lower()
        chars = list(lower_word)
        for char in chars:
            lowered = char.lower()
            if lowered in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    
    return characters


def sort_on(x):
    return x['num']

def sort_letters(letters):
    dict_list = []
    for l in letters:
        dict_list.append({'char':l,'num':letters[l]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
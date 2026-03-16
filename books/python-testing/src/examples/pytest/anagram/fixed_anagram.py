def is_anagram(a_word, b_word):
    return sorted(a_word.replace(' ', '')) == sorted(b_word.replace(' ', ''))


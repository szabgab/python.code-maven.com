def is_anagram(a_word, b_word):
    return sorted(a_word) == sorted(b_word)

#return sorted(filter(lambda v: v != " ", a_word)) == sorted(filter(lambda v: v != " ", b_word))

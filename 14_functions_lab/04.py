"""
Write a function that takes minlen and
a list of words, and returns only the words
longer than minlen
"""

def min_word_length(min_word_len,*words):
    max_words = [word for word in words if len(word) > min_word_len]
    return max_words

print "Test min_word_length(5,'hi','dontgo',bye') "
print min_word_length(5,'hi','dontgo','bye')
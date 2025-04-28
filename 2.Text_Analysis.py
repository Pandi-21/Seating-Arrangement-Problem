# Problem:
# Count the frequency of each word from a text,
# ignoring common stop words like "the", "is", "at", etc.
# Allow query: find top N words starting with a given prefix.

# solution:
# - Only basic loops
# - Split text into words, clean them, remove stop words.
# - Count the word frequencies.
# - For prefix search, check words starting with prefix and get top N.

from collections import Counter

stop_words = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'for', 'with'}

def count_words(text):
    words = text.lower().split()
    clean_words = []
    for letter in words:
        letter = ''.join(c for c in letter if c.isalnum())  # Remove punctuation
        if letter and letter not in stop_words:
            clean_words.append(letter)
    return Counter(clean_words)

def words(counter, prefix, n):
    prefix = prefix.lower()
    result = []
    for word, freq in counter.items():
        if word.startswith(prefix):
            result.append((word, freq))
    result.sort(key=lambda x: -x[1])  # Sort by frequency
    return result[:n]

 
text = """
 The sequence diagram and collaboration diagram are called interaction between diagrams.
 the collaboration diagram that may be objects axis and message
"""

word_counter = count_words(text)
print(word_counter)

top_words = words(word_counter, 'fo', 3)
print(top_words)

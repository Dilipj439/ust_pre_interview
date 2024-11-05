#used collections module to get the frequency of the string
from collections import Counter

def frequency_of_string():
    line = "which is better python 2 or python 3"
    words = line.split()
    word_count = Counter(words)
    for word in sorted(word_count):
        print(f"('{word}', {word_count[word]})")



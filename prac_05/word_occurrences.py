"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

INCREMENT = 1
count = 0
words_to_count = {}
sentence = input("Text: ")
words = sentence.split()

for word in words:
    count = words_to_count.get(word, 0)
    words_to_count[word] = count + INCREMENT

words = list(words_to_count.keys())
words.sort()

maximum_length = max((len(words) for word in words))
for word in words:
    print(f"{word:{maximum_length}} : {words_to_count[word]}")

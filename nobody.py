from collections import Counter
"""'Nobody is examined to find the 3 most common words"""

words = open('nobody.txt').read().lower().split()
c = Counter(words)
print("No wonder this song was addicting." , c.most_common(3))

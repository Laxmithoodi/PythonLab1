import collections
import re
wordst = re.findall(r'\b[a-z]{3,15}\b', open("longtext.txt").read().lower())
most_common = collections.Counter(wordst).most_common(250)
print(most_common, '\n')




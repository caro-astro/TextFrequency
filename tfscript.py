from collections import Counter
from nltk.corpus import stopwords
import string

f=open("/Users/Caroline/Analysis/LML/goodthings.txt", "r+")
wordcount = Counter(f.read().split())
#for k,v in wordcount.items():
#     print k, v
print(wordcount.most_common(5))
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['\xc2\xb7', 'I', 'love', 'The', 'live', 'get', 'see', 'beautiful', 'little', 'its', 'enjoy', 'street', 'also',"it's", "I'm","Also,", 'It', 'always']

terms_stop = [term for term in fl if term not in stop]
wordcount = Counter(terms_stop)
print(wordcount.most_common(5))

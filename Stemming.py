import nltk
from nltk.stem import PorterStemmer

# متن ورودی
text = "organizes organizing organized runs running ran democracy democratic democratization"

# تقسیم متن به توکن‌ها
tokens = text.split()

# ایجاد یک شیء Stemmer
stemmer = PorterStemmer()

# انجام Stemming بر روی توکن‌ها
stemmed_tokens = [stemmer.stem(token) for token in tokens]

print(stemmed_tokens)

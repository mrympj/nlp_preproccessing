import nltk
from nltk.stem import WordNetLemmatizer

# نیاز به دانلود WordNet اگر اولین بار اجرا شود
nltk.download('wordnet')

# متن ورودی
text = "organizes organizing organized runs running ran democracy democratic democratization feet"

# تقسیم متن به توکن‌ها
tokens = text.split()

# ایجاد یک شیء Lemmatizer
lemmatizer = WordNetLemmatizer()

# انجام Lemmatization بر روی توکن‌ها
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

print(lemmatized_tokens)

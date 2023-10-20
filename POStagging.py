import nltk

# نیاز به دانلود داده‌های واژگانی اگر اولین بار اجرا شود
nltk.download('averaged_perceptron_tagger')

# متن ورودی
text = "This is an example sentence. It demonstrates POS tagging."

# تقسیم متن به کلمات (توکن‌ها)
words = nltk.word_tokenize(text)

# انجام POS tagging
pos_tags = nltk.pos_tag(words)

print(pos_tags)

import re
import inflect

abbreviations = {
    "U.S.A.": "USA",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "cause": "because",
    "could've": "could have",
    # another abbreviations
}

def normalize_token(token):
    if token in abbreviations:
        return abbreviations[token]

    normalized_token = token.lower()

    normalized_token = re.sub(r'[^a-z]+', '', normalized_token)

    p = inflect.engine()
    if normalized_token.isdigit():
        normalized_token = p.number_to_words(int(normalized_token))

    return normalized_token

text = "U.S.A. and USA; 200$ and two hundred dollars. aren't we happy?"

tokens = re.findall(r'\S+', text)

normalized_tokens = [normalize_token(token) for token in tokens]

print(normalized_tokens)

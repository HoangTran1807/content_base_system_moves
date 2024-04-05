import re
from underthesea import word_tokenize

with open('./desc.html', 'r', encoding='utf-8') as file:
    content = file.read()
    result = re.sub('<[^>]*>', '', content)

with open("./vietnamese-stopwords.txt", encoding='utf-8') as f:
    stopwords = f.readlines()
stopwords = [x.strip().replace(" ", "_") for x in stopwords]
print(f"Tổng số lượng từ dừng: {len(stopwords)}")

# Tách từ
words = word_tokenize(result, format="text")

# Loại bỏ stopword
filtered_words = [word for word in words.split() if word not in stopwords]

# Ghép lại thành chuỗi
result = ' '.join(filtered_words)

print(result)






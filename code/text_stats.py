import string

def count_word_frequency(file_path):
    """读取文本文件，统计单词词频，忽略大小写、标点符号"""
    word_count = {}
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().lower()
    # 删除所有标点
    trans = str.maketrans('', '', string.punctuation)
    content = content.translate(trans)
    words = content.split()
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1
    return word_count

if __name__ == "__main__":
    freq = count_word_frequency("code/sample.txt")
    print("====单词词频统计结果====")
    for word, num in sorted(freq.items()):
        print(f"{word}: {num}")

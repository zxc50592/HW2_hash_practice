def count_unique_words(filename):
    # 創建一個空的字典來存儲每個單字的出現次數
    word_count = {}

    # 打開文件並讀取
    with open(filename, 'r') as file:
        # 逐行讀取
        for line in file:
            # 去除每行的換行符號，然後使用空格分割單字
            words = line.strip().split()
            # 進行計數
            for word in words:
                # 使用字典的Hash來計算每個單字的數量
                word_count[word] = word_count.get(word, 0) + 1

    # 計算總共有多少個不重複的英文單字
    unique_words_count = len(word_count)

    return word_count

def main():
    filename = "hw2_data.txt"
    word_count = count_unique_words(filename)

    print("總共有 %d 個不重複的英文單字。" % len(word_count))
    print("每個英文單字出現的次數為：")
    
    # 列出單字以及其數量，並加上編號
    i = 1
    for word, count in word_count.items():
        print("%d.%s: %d" % (i, word, count))
        i += 1

if __name__ == "__main__":
    main()


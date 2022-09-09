def reverseWords(input):
    inputWords = input.split(" ")  # 通过空格将字符串分隔，把各个单词分隔为列表
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    input = "I like cat"
    rw = reverseWords(input)
    print(rw)



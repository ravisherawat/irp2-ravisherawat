def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


if __name__ == "__main__":
    sentence = input()
    print(reverse_words(sentence))

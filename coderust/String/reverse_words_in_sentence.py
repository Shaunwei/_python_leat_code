def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


def rev_words(words):
    def rec_r(word, index):
        if index == len(word) - 1:
            return word[-1]
        return rec_r(word, index+1) + word[index]
    return rec_r(words, 0)


if __name__ == '__main__':
    s = 'Quick brown fox jumped over the lazy dog.'
    print reverse_words(s)

    print rev_words(s)

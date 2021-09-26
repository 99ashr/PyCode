def reverse_words_order_and_swap_cases(sentence):

    # Write your code here
    # s = sentence[::-1]
    # print(s)
    # print(sentence.swapcase())
    sentence = sentence.swapcase()
    s = sentence.split()
    new_str = []
    for i in s[::-1]:
        new_str.append(i)
    # print(new_str)
    str1 = " "
    return(str1.join(new_str))
    # print(ns)


if __name__ == '__main__':
    print(reverse_words_order_and_swap_cases("aWESOME is cODING"))

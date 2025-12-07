def reverse_word(sentence):
    arr= sentence.split(" ")
    reversed_arr= arr[::-1]
    print(reversed_arr)

reverse_word("Hello World")


class Node:
    def __init__(self, data):
        data= self.data
        self.next= None
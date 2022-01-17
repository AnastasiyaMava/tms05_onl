sentence = " the quick brown fox jumps over the lazy dog"
list_numb = [len(i) for i in sentence.split() if i != 'the']
print(list_numb)
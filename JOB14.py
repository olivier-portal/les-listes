def my_long_word(n, s):
    list = [word for word in s.split() if len(word) > n]
    my_string = ' '.join(map(str, list))
    return my_string

    
new_sentence = my_long_word(3, 'La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance')

print(new_sentence)
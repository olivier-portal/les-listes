def my_long_word(number, string):
    list = [char for char in string]
    list_of_words = ''.join(char if char != ' ' else ' ' for char in string).split()
    list_of_words_length = 0
    # for _ in list_of_words:
    #     list_of_words_length += 1
    # for i in range(list_of_words_length):
    #     for j in range(list_of_words_length - 1):
    #         if j <= number:
    #             list_of_words.pop(j)
    return list_of_words

    
new_sentence = my_long_word(3, 'La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance')

print(new_sentence)


# def convert_in_string():
#     string = "Hello World"
#     list = [char for char in string]
#     words = ''.join(char if char != ' ' else ' ' for char in string).split()
#     print(words)


    #         if i != ' ':
    #             new_index = list[j] + list[j + 1]
    #         return list
    
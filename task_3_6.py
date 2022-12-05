"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().

"""


def int_func(arg_word):
    return arg_word.capitalize()


def capitalize_string(in_string):
    arg_string = in_string.split()
    for element in range(len(arg_string)):
        arg_string[element] = int_func(arg_string[element])
    return ' '.join(arg_string)


input_word = input("Введите слово: ")
print(int_func(input_word))

input_words = input("Введите строку слов, разделенных пробелом: ")
print(capitalize_string(input_words))

from global_var import alphabet_upper


def vigenere_encrypt(source_file_way, result_file_way, key_word):
    # Эта функция шифрует текст шифром Вижинера
    # Функция переводит весь текст в верхний регистр
    # source_file_way файл с текстом
    # result_file_way файл куда будет записан заштфрованный текст
    # key_word ключ
    result = ""
    source_file = open(source_file_way, "r")

    new_text = ""
    # Переводим весь текст в верхний регистр
    for line in source_file.readlines():
        for i in line.upper():
            if i in alphabet_upper:
                new_text += i

    # Ключ тоже должен быть в верхнем регистре
    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    for i in range(len(new_text)):
        result += alphabet_upper[alphabet_upper.find(new_text[i]) + alphabet_upper.find(key_word[i % len(key_word)])]

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()


def vigenere_encrypt_int():
    # функция для отрисвки в консоль
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_encrypt(source_file_way, result_file_way, key_word)


def vigenere_decrypt(source_file_way, result_file_way, key_word):
   # Эта функция расшифровывает текст
    result = ""
    source_file = open(source_file_way, "r")

    new_text = ""
    for line in source_file.readlines():
        for i in line.upper():
            if i in alphabet_upper:
                new_text += i

    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    for i in range(len(new_text)):
        result += alphabet_upper[alphabet_upper.find(new_text[i]) - alphabet_upper.find(key_word[i % len(key_word)])]

    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()


def vigenere_decrypt_int():
    # функция для отрисовки в консоль
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_decrypt(source_file_way, result_file_way, key_word)

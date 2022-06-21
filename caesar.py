from global_var import alphabet_lower
from global_var import alphabet_upper

def encrypt_caes_line(line, shift):
    #эта функция шифрует одну строку шифром цезаря
    # line строка
    # shift сдвиг
    res = ""
    for let in line:
        find_res = alphabet_lower.find(let)
        if find_res != -1:
            find_res += shift
            find_res %= len(alphabet_upper)
            res += alphabet_lower[find_res]
        else:
            find_res = alphabet_upper.find(let)
            if find_res != -1:
                find_res += shift
                find_res %= len(alphabet_upper)
                res += alphabet_upper[find_res]
            else:
                res += let
    return res


def caesar_encrypt(source_file_way, result_file_way, shift):
    # эта функция шифрует весть текст из файла source_file_way в файл result_file_way с двигом shift
    result = ""
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += encrypt_caes_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    result_file.close()


def caesar_encrypt_int():
    # функция для красивой отрисовки в консоль
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_encrypt(source_file_way, result_file_way, shift)


def decrypt_caes_line(line, shift):
    #эта функция расшифровывает одну строку шифром цезаря
    # line строка
    # shift сдвиг
    # дешифрованная строка

    result = ""
    for let in line:
        find_res = alphabet_lower.find(let)
        if find_res != -1:
            find_res -= shift
            find_res %= len(alphabet_upper)
            result += alphabet_lower[find_res]
        else:
            find_res = alphabet_upper.find(let)
            if find_res != -1:
                find_res -= shift
                find_res %= len(alphabet_upper)
                result += alphabet_upper[find_res]
            else:
                result += let
    return result


def caesar_decrypt(source_file_way, result_file_way, shift):
    # эта функция дешифрует весть текст из файла source_file_way в файл result_file_way с двигом shift
    result = ""
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += decrypt_caes_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)


def caesar_decrypt_int():
    # функция для красивой отрисовки в консоль
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_auto_crack(source_file_way, result_file_way):
    # эта функция взламывает шифр цезаря с помощью частотного анализа
    # source_file_way файл с шифрованным текстом
    # result_file_way файл для результата
    source_file = open(source_file_way, "r")

    # Подсчет количества букв
    counter = {}
    let_sum = 0
    for let in alphabet_lower:
        counter[let] = 0
    for line in source_file.readlines():
        for let in line.lower():
            if let in counter.keys():
                counter[let] += 1
                let_sum += 1

    counter = (list(counter.items()))
    counter.sort(key=lambda i: i[1], reverse=True)
    counter = list(map(lambda x: [x[0], x[1] / let_sum], counter))
    shift = alphabet_lower.find(counter[0][0]) - alphabet_lower.find("e")
    if shift < 0:
        shift = len(alphabet_upper) + shift

    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_auto_crack_int():
    # функция для красивой отрисовки в консоль
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter file you want to save result to name: ")
    caesar_auto_crack(source_file_way, result_file_way)

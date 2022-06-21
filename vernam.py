from global_var import alphabet_upper
import random



def vernam_encrypt(source_file_way, result_file_way, result_key_file_way, seed):
    # Эта функция шифрует текст шифром Вернама.
    result = ""
    result_key = ""
    source_file = open(source_file_way, "r")

    random.seed(seed)

    for line in source_file:
        new_line = ""

        for i in line.upper():
            if i in alphabet_upper:
                new_line += i
        line = new_line

        tmp = ""
        for i in range(len(line)):
            tmp += alphabet_upper[random.randint(0, 25)]
        keyword = tmp

        for let, klet in zip(line, keyword):
            found_let = alphabet_upper.find(let)
            found_key_let = alphabet_upper.find(klet)
            result += alphabet_upper[(found_let + found_key_let) % len(alphabet_upper)]

        result_key += keyword

    source_file = open(result_file_way, "w")
    source_file.write(result)
    source_file.close()
    result_key_file = open(result_key_file_way, "w")
    result_key_file.write(result_key)
    result_key_file.close()


def vernam_encrypt_int():
    # функция для отрисовки в консоль
    source_file_way = input("Enter file you want encrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    new_key_file_way = input("Enter file with key name or absolute way: ")
    seed = input("Enter seed to generate random key: ")
    vernam_encrypt(source_file_way, result_file_way, new_key_file_way, seed)


def vernam_decrypt(source_file_way, result_file_way, key_file_way):
    # Эта функция расшифровывает текст
    result = ""
    source_file = open(source_file_way, "r")
    key_file = open(key_file_way, "r")


    for let, klet in zip(source_file.read(), key_file.read()):
        found_let = alphabet_upper.find(let)
        found_key_let = alphabet_upper.find(klet)
        result += alphabet_upper[(found_let - found_key_let) % len(alphabet_upper)]


    result_file = open(result_file_way, "w")
    result_file.write(result)
    source_file.close()
    result_file.close()
    key_file.close()


def vernam_decrypt_int():
    # функция для отрисовки в консоль
    source_file_way = input("Enter file you want decrypt name or absolute way: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_file_way = input("Enter the name of the file with key: ")
    vernam_decrypt(source_file_way, result_file_way, key_file_way)

import numpy as np
from PIL import Image
import random



def picture_encrypt(source_picture_way, source_text_file_way, result_picture_way, seed):
    # Эта функция шифрует текст в случайные пиксели картинки

    # загрузка файлов и инициализация некоторых переменных
    used_pixel_list = []

    source_text_file = open(source_text_file_way, "r")
    source_img = Image.open(source_picture_way)
    source_img.load()
    source_array = np.array(source_img)
    source_width, source_height = source_img.size

    random.seed(seed)
    current_pixel = random.randint(0, source_height * source_width)

    # основной цикл в котором шифруется текст
    for line in source_text_file.readlines():
        for let in line:
            while current_pixel in used_pixel_list:
                current_pixel = random.randint(0, source_height * source_width)
            pixel_line = current_pixel // source_width
            pixel_collumn = current_pixel % source_width
            let = ord(let)

            let_r = (let & 0b11100000) >> 5
            let_g = (let & 0b00011100) >> 2
            let_b = let & 0b00000011
            source_array[pixel_line][pixel_collumn][0] = (source_array[pixel_line][pixel_collumn][
                                                              0] & 0b11111000) + let_r
            source_array[pixel_line][pixel_collumn][1] = (source_array[pixel_line][pixel_collumn][
                                                              1] & 0b11111000) + let_g
            source_array[pixel_line][pixel_collumn][2] = (source_array[pixel_line][pixel_collumn][
                                                              2] & 0b11111100) + let_b
            used_pixel_list.append(current_pixel)

    # зашифровываем 0 чтобы обозначить конец последовательности
    while current_pixel in used_pixel_list:
        current_pixel = random.randint(0, source_height * source_width)
    pixel_line = current_pixel // source_width
    pixel_collumn = current_pixel % source_width
    source_array[pixel_line][pixel_collumn][0] = (source_array[pixel_line][pixel_collumn][0] & 0b11111000)
    source_array[pixel_line][pixel_collumn][1] = (source_array[pixel_line][pixel_collumn][1] & 0b11111000)
    source_array[pixel_line][pixel_collumn][2] = (source_array[pixel_line][pixel_collumn][2] & 0b11111100)

    # сохранение результата
    res = Image.fromarray(source_array, "RGB")
    res.save(result_picture_way)
    source_text_file.close()


def picture_encrypt_int():
    # функция для отрисовки в консоль
    source_picture_way = input("Enter name of picture you want to encrypt in: ")
    source_text_way = input("Enter file you want to encrypt name: ")
    result_picture_name = input("Enter the name of the file you want to save the result to (without extension): ")
    seed = input("Enter seed: ")
    picture_encrypt(source_picture_way, source_text_way, result_picture_name + ".bmp", seed)


def picture_decrypt_letter(pixel):
    # Эта функция извлекает символы из картинки
    let_r = (pixel[0] & 0b00000111) << 5
    let_g = (pixel[1] & 0b00000111) << 2
    let_b = pixel[2] & 0b00000011
    let = let_r + let_g + let_b
    return let


def picture_decrypt(source_picture_way, result_text_file_way, seed):
    # Эта функция расшифровывает текст

    # загрузка файлов и инициализация некоторых переменных
    used_pixel_list = []

    result_file = open(result_text_file_way, "w")
    source_img = Image.open(source_picture_way)
    source_img.load()
    source_array = np.array(source_img)

    source_width, source_height = source_img.size

    random.seed(seed)
    result = ""
    # расшифровываем по пикселю, пока не найдем 0
    while True:
        current_pixel = random.randint(0, source_height * source_width)
        while current_pixel in used_pixel_list:
            current_pixel = random.randint(0, source_height * source_width)
        pixel_line = current_pixel // source_width
        pixel_collumn = current_pixel % source_width
        tmp = picture_decrypt_letter(source_array[pixel_line][pixel_collumn])

        if tmp == 0:
            break
        else:
            result += chr(tmp)

    result_file.write(result)
    result_file.close()


def picture_decrypt_int():
    # функция для отрисовки в консоль
    source_picture_way = input("Enter name of picture you want to decrypt: ")
    result_text_file_way = input("Enter the name of the file you want to save the result to: ")
    seed = input("Enter seed: ")
    picture_decrypt(source_picture_way, result_text_file_way, seed)

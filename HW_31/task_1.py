"""
1. Написать функцию, которая генерируют в директории `directory`
`number_of_files` файлов.
Содержимое файлов должно быть случайным, состоять из
больших/маленьких латинских букв, цифр и символов пунктуации.
Файл должен содержать случайное число символов в
диапазоне от `size/2` до `size` символов.

def file_generator(directory, number_of_files, size)
Осторожно: file_generator('files', 200, 1000_000) ~150 Mb

2. Написать функцию (обычную, однопоточную), которая возвращает
число букв `letter_to_find` во всех файлах директории `directory`

def letter_counter_in_one_thread(directory, letter_to_find)

3. Написать функцию, которая возвращает число букв `letter_to_find`
во всех файлах директории `directory`
Функция должна разбить файлы в директории на `number_of_threads`
групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
4. Написать клиентский код, который создает файлы, подсчитывает количество
букв функцией в одном потоке и в нескольких потоках, и выводит время
выполнения функций.

NOTE1: Директорию считаем "плоской" - вложенных директорий нет.
NOTE2: Можно реализовать и вариант на процессах, и сравнить время выполнения.
"""
import concurrent.futures
import os
import random
import string
import time


def generate_random_content(size):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(size))


"""
1. Написать функцию, которая генерируют в директории `directory`
`number_of_files` файлов.
Содержимое файлов должно быть случайным, состоять из
больших/маленьких латинских букв, цифр и символов пунктуации.
Файл должен содержать случайное число символов в
диапазоне от `size/2` до `size` символов.

def file_generator(directory, number_of_files, size)
Осторожно: file_generator('files', 200, 1000_000) ~150 Mb
"""


def file_generator(directory, number_of_files, size):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        file_name = os.path.join(directory, f"file_{i + 1}.txt")
        random_size = random.randint(size // 2, size)
        content = generate_random_content(random_size)

        with open(file_name, 'w') as file:
            file.write(content)


def count_letter_in_files(files_path, letter_to_find):
    with open(files_path, 'r') as file:
        text = file.read()
    return text.count(letter_to_find)


"""
2. Написать функцию (обычную, однопоточную), которая возвращает
число букв `letter_to_find` во всех файлах директории `directory`

def letter_counter_in_one_thread(directory, letter_to_find)
"""


def letter_counter_in_one_thread(directory, letter_to_find):
    total_count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            total_count += count_letter_in_files((os.path.join(directory, filename)), letter_to_find)
    return total_count


"""
3. Написать функцию, которая возвращает число букв `letter_to_find`
во всех файлах директории `directory`
Функция должна разбить файлы в директории на `number_of_threads`
групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
"""


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    count = 0
    files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]
    file_groups = [files[i::number_of_threads] for i in range(number_of_threads)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for filenames in file_groups:
            for file in filenames:
                futures.append(executor.submit(count_letter_in_files, os.path.join(directory, file), letter_to_find))
        for future in concurrent.futures.as_completed(futures):
            count += future.result()
    return count


"""
4. Написать клиентский код, который создает файлы, подсчитывает количество
букв функцией в одном потоке и в нескольких потоках, и выводит время
выполнения функций.
"""

target_directory = "directory"
num_files_to_generate = 20
file_size = 100
letter_to_find = 'A'
threads = 3

start_time = time.time()
file_generator(target_directory, num_files_to_generate, file_size)
end_time = time.time()
print(f"Files generator {end_time - start_time} seconds")
start_time = time.time()
count_letter_one_thread = letter_counter_in_one_thread(target_directory, letter_to_find)
end_time = time.time()
print(
    f"{count_letter_one_thread} letter were found 1 times in {end_time - start_time} seconds")
start_time = time.time()
count_letter_n_threads = letter_counter_in_n_threads(target_directory, letter_to_find, threads)
end_time = time.time()
print(f"{count_letter_n_threads} letter were found {threads} times in {end_time - start_time} seconds")

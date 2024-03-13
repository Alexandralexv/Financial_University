import os # функции для взаимодействия с операционной системой
import shutil # операции над файлами и директориями

def create_folder(folder_name): # новая папка
    try:
        os.mkdir(folder_name) # новая папка с именем
        print(f"Папка '{folder_name}' успешно создана.")
    except FileExistsError: # обрабатывает исключение FileExistsError, возникающее, если папка с таким именем уже существует
        print(f"Папка '{folder_name}' уже существует.")

def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        print(f"Папка '{folder_name}' успешно удалена.")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не найдена.")
    except OSError:
        print(f"Невозможно удалить '{folder_name}'. Папка не пуста.")

def move_to_folder(folder_name): # переместить в папку
    try:
        os.chdir(folder_name)
        print(f"Перешли в папку '{folder_name}'. Текущая директория: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не найдена.")

def create_file(file_name): 
    try:
        with open(file_name, 'w') as file:
            print(f"Файл '{file_name}' успешно создан.")
    except FileExistsError:
        print(f"Файл '{file_name}' уже существует.")

def write_to_file(file_name, text): 
    try:
        with open(file_name, 'a') as file:
            file.write(text + '\n')
            print(f"Текст успешно записан в файл '{file_name}'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

def view_file(file_name): 
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Содержимое файла '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

def delete_file(file_name): 
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

def copy_file(source, destination): 
    try:
        shutil.copy2(source, destination)
        print(f"Файл '{source}' успешно скопирован в '{destination}'.")
    except FileNotFoundError:
        print(f"Файл '{source}' не найден.")

def move_file(source, destination): 
    try:
        shutil.move(source, destination)
        print(f"Файл '{source}' успешно перемещен в '{destination}'.")
    except FileNotFoundError:
        print(f"Файл '{source}' не найден.")

def rename_file(old_name, new_name): 
    try:
        os.rename(old_name, new_name)
        print(f"Файл '{old_name}' успешно переименован в '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл '{old_name}' не найден.")

# Создаем папку
create_folder("example_folder")

# Переходим в созданную папку
move_to_folder("example_folder")

# Создаем файл и записываем в него текст
create_file("example.txt")
write_to_file("example.txt", "Пример текста в файле")

# Просматриваем содержимое файла
view_file("example.txt")

# Копируем файл в другую папку
copy_file("example.txt", "../backup_folder")

# Переименовываем файл
rename_file("example.txt", "renamed_example.txt")

# Удаляем файл
delete_file("renamed_example.txt")

# Выходим на уровень вверх
move_to_folder("..")

# Удаляем созданную папку
delete_folder("example_folder")

# Удаляем файл
delete_file("backup_folder")
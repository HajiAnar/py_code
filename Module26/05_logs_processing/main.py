import os


def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

            # Путь до файла с логами


input_file_path = os.path.join('data', 'work_logs.txt')

# Путь до файла, в который будут записаны строки с ошибками
output_file_path = os.path.join('data', 'output.txt')

# Проверка наличия файлов перед началом работы с ними
if not os.path.exists(input_file_path):
    print(f"Файл {input_file_path} не найден.")
elif not os.path.exists(output_file_path):
    print(f"Файл {output_file_path} не найден.")
else:
    with open(output_file_path, 'w') as output:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
    print("Файл успешно обработан.")
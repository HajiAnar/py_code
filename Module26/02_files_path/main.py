import os




def gen_files_path(target_dir = None, directory = os.path.abspath(os.sep)):
    """Функция для нахождения каталога, указанного пользователем и генерирования пути всех встреченных файлов
    target_dir - директория, заданная пользователем
    directory - абсолютный путь
    """
    for root,  dirs, files in os.walk(directory):
        if target_dir and target_dir in dirs:
            print(f'Found! {root}, {os.sep}, {target_dir}')
            return
        for file_name in files:
            yield os.path.join(root,file_name)

for file in gen_files_path('test'):
    print(file)


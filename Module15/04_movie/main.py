films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']


n = int(input("Сколько фильмов выбрать? "))
your_films = []
for i in range(n):
    print("Ваш текущий топ фильмов:", your_films)
    film_name = input("Имя фильма: ")
    if film_name in films:
        your_films.append(film_name)
    else:
        print('Ошибка: фильма', film_name, 'у нас нет :(')


print("Ваш текущий топ фильмов:", your_films)

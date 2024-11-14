import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, username, password):
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == username and user.password == hash_password:
                self.current_user = user
                print('Успешный вход')
                return
            else:
                print('Неверный логин или пароль!')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print('Пользователь с таким именем уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        print(f'Пользователь {nickname} успешно зарегестрирован')

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print('Вы вышли из аккаунта.')
        else:
            print('Вы не вошли в систему.')

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                continue

    def get_videos(self, search_word):
        result = []
        search_word = search_word.lower()
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video)
                return result

    def watch_video(self, title):
        if self.current_user is None:
            print('Вы не вошли не в систему ')
            return

        found_video = next((video for video in self.videos if video.title == title), None)
        if found_video is None:
            print('Ксожалению, видео не найдено')
            return
        if found_video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет')
            return

        print(f'''видео '{title}''')
        while found_video.time_now < found_video.duration:
            print(f'Секунда: {found_video.time_now}')
            found_video.time_now += 1
            sleep(1)

        found_video.time_now = 0
        print('Конец видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

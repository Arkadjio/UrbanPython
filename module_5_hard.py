import hashlib
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return f"Пользователь {nickname} успешно вошел."
        return "Неверный логин или пароль."

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        print("Регистрация прошла успешно!")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(video.title == existing_video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        results = [video.title for video in self.videos if search_word in video.title.lower()]
        return results

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        found_video = next((video for video in self.videos if video.title == title), None)

        if not found_video:
            print("Видео не найдено.")
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Воспроизведение видео
        print(f"Воспроизведение видео '{found_video.title}'...")
        for second in range(found_video.time_now + 1, found_video.duration + 1):
            print(second)
            sleep(1)

        found_video.time_now = 0
        print("Конец видео")


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

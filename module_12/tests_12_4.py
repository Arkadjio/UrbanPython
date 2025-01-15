import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Параметр <Name> может быть только строкой')

        self.distance = 0

        if speed > 0:
            self.speed = speed
        else:
            raise ValueError('Значение параметра < speed > не может быть отрицательным ')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    try:
        def test_walk(self):
            runner_test_walk = Runner('Lera', -1)
            for i in range(10):
                runner_test_walk.walk()
            self.assertEqual(runner_test_walk.distance, 50)
        logging.info('"test_walk" выполнен успешно')
    except ValueError:
        logging.warning('"Неверная скорость для Runner".')

    try:
        def test_run(self):
            runner_test_run = Runner(0)
            for i in range(10):
                runner_test_run.run()
            self.assertEqual(runner_test_run.distance, 100)
        logging.info('"test_run" выполнен успешно')
    except TypeError:
        logging.warning('"Неверный тип данных для объекта Runner".')

    def test_challenge(self):
        walk_2 = Runner('Lera')
        run_2 = Runner('Artemiy')
        for i in range(10):
            walk_2.walk()
            run_2.run()
        self.assertNotEqual(run_2.distance, walk_2.distance)
        logging.info(' челендж успешно пройден')


if __name__ == '__main__':
    unittest.main()

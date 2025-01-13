from module_13 import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        participants = {'Усейн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {k: rt.Runner(name=k, speed=v) for k, v in participants.items()}

    def test_Usain_Nick(self):
        tour_1 = rt.Tournament(90, self.runners['Усейн'], self.runners['Ник'])
        all_results = tour_1.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_Andrey_Nick(self):
        tour_2 = rt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tour_2.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_all_vs(self):
        tour_3 = rt.Tournament(90, self.runners['Усейн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour_3.start()

        self.assertTrue(all_results[3], self.runners['Ник'])

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.keys():
            print(f'{key}: {value}')


if __name__ == '__main__':
    unittest.main()

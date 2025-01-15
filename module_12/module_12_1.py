from module_12 import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_test_walk = runner.Runner('Lera')
        for i in range(10):
            runner_test_walk.walk()
        self.assertEqual(runner_test_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_test_run = runner.Runner('Artemiy')
        for i in range(10):
            runner_test_run.run()
        self.assertEqual(runner_test_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk_2 = runner.Runner('Lera')
        run_2 = runner.Runner('Artemiy')
        for i in range(10):
            walk_2.walk()
            run_2.run()
        self.assertNotEqual(run_2.distance, walk_2.distance)


if __name__ == '__main__':
    unittest.main()

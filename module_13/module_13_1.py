from module_13 import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_test_walk = runner.Runner(input('Enter name- '))
        for i in range(10):
            runner_test_walk.walk()
        self.assertEqual(runner_test_walk.distance, 50)

    def test_run(self):
        runner_test_run = runner.Runner(input('Enter name- '))
        for i in range(10):
            runner_test_run.run()
        self.assertEqual(runner_test_run.distance, 100)

    def test_challenge(self):
        walk_2 = runner.Runner(input('Enter name- '))
        run_2 = runner.Runner(input('Enter name- '))
        for i in range(10):
            walk_2.walk()
            run_2.run()
        self.assertNotEqual(run_2.distance, walk_2.distance)


if __name__ == '__main__':
    unittest.main()

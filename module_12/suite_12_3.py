import unittest
import module_12_2 as m2
import module_12_1 as m1

runnerTS = unittest.TestSuite()

runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(m1.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(m2.TournamentTest))
runner_suite = unittest.TextTestRunner(verbosity=2)
runner_suite.run(runnerTS)

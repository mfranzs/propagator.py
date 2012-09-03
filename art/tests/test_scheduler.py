import unittest

from art import scheduler
from art.art import Cell, Propagator
from art.primitives import *

class TestCaseWithScheduler(unittest.TestCase):
    def setUp(self):
        scheduler.initialize()

class SchedulerTestCase(TestCaseWithScheduler):
    def test_new_scheduler_has_no_alerted_propagators(self):
        self.assertEqual(len(scheduler.alerted_propagators), 0)
        self.assertEqual(len(scheduler.propagators_ever_alerted), 0)


if __name__ == '__main__':
        unittest.main()
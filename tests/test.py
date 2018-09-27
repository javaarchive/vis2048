# noinspection PyUnresolvedReferences
import unittest

from tests.game_test import GameTest
from tests.mat_test import MutSqMatTest
from tests.vec2_test import Vec2Test


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(Vec2Test())
    suite.addTest(MutSqMatTest())
    suite.addTest(GameTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(create_suite())

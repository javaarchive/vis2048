import unittest

from vis2048.game import Game
from vis2048.vec2 import Vec2


class GameTest(unittest.TestCase):
    def test_init(self):
        game = Game(4, 2, 2048)

        self.assertEqual(0, game.score)
        self.assertEqual(2, game.min_tile)
        self.assertEqual(2048, game.max_tile)
        self.assertEqual(4, game.width)
        self.assertEqual([None] * 4 ** 2, game.mat._items)

    def test_stuck(self):
        game = Game(4, 2, 2048)

        self.assertFalse(game.stuck())

        game.mat._items = [
            2, 4, 8, 16,
            32, 64, 128, 256,
            512, 1024, 2048, 2,
            4, 8, 16, 32
        ]

        self.assertTrue(game.stuck())

        game.mat[Vec2(1, 1)] = 4

        self.assertFalse(game.stuck())

    def test_won(self):
        game = Game(4, 2, 2048)

        self.assertFalse(game.won())

        game.mat._items = [
            2, 4, 8, 16,
            32, 64, 128, 256,
            512, 1024, 1024, 2,
            4, 8, 16, 32
        ]

        game.left()

        self.assertTrue(game.won())

    def test_full(self):
        game = Game(4, 2, 2048)

        self.assertFalse(game.full())

        game.mat._items = [
            2, 2, 8, 16,
            32, 64, 128, 256,
            512, 1024, 1024, 2,
            4, 4, 16, 32
        ]

        self.assertTrue(game.full())

        game.left()

        self.assertFalse(game.full())

    def test_place_two_working(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 8, 16,
            32, None, 128, 256,
            512, 1024, None, 2,
            4, 4, 16, 32
        ]

        game.place_two()

        first_gap = game.mat[Vec2(1, 1)]
        second_gap = game.mat[Vec2(2, 2)]

        self.assertIn(2, (first_gap, second_gap))

    def test_place_two_full(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 8, 16,
            32, 4, 128, 256,
            512, 1024, 2, 2,
            4, 4, 16, 32
        ]

        self.assertRaises(ValueError, game.place_two)

    def test_score(self):
        game = Game(4, 2, 2048)

        self.assertEqual(0, game.score)

        game.mat._items = [
            2, 2, 8, 16,
            32, 64, 128, 256,
            512, 1024, 1024, 2,
            4, 4, 16, 32
        ]

        game.left()

        self.assertEqual(4 + 2048 + 8, game.score)

    def test_move_left_merge(self):
        game = Game(4, 2, 2048)

        line = [2, 2, 2, 2]
        game._move_left(line)

        self.assertEqual([4, 4, None, None], line)

    def test_move_left_gap(self):
        game = Game(4, 2, 2048)

        line = [2, 4, None, 4]
        game._move_left(line)

        self.assertEqual([2, 8, None, None], line)

    def test_move_left_shift(self):
        game = Game(4, 2, 2048)

        line = [2, 2, 4, 2]
        game._move_left(line)

        self.assertEqual([4, 4, 2, None], line)

    def test_left(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 2, 2,
            2, 2, 4, 2,
            4, 8, 4, 4,
            16, None, 16, 16
        ]

        game.left()

        self.assertEqual([
            4, 4, None, None,
            4, 4, 2, None,
            4, 8, 8, None,
            32, 16, None, None
        ], game.mat._items)

    def test_right(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 2, 2,
            2, 2, 4, 2,
            4, 8, 4, 4,
            16, None, 16, 16
        ]

        game.right()

        self.assertEqual([
            None, None, 4, 4,
            None, 4, 4, 2,
            None, 4, 8, 8,
            None, None, 16, 32
        ], game.mat._items)

    def test_up(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 2, 2,
            2, 2, 4, 2,
            4, 8, 4, 4,
            16, None, 16, 16
        ]

        game.up()

        self.assertEqual([
            4, 4, 2, 4,
            4, 8, 8, 4,
            16, None, 16, 16,
            None, None, None, None
        ], game.mat._items)

    def test_down(self):
        game = Game(4, 2, 2048)

        game.mat._items = [
            2, 2, 2, 2,
            2, 2, 4, 2,
            4, 8, 4, 4,
            16, None, 16, 16
        ]

        game.down()

        self.assertEqual([
            None, None, None, None,
            4, None, 2, 4,
            4, 4, 8, 4,
            16, 8, 16, 16
        ], game.mat._items)

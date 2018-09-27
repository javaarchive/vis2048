import unittest

from vis2048.vec2 import Vec2


class Vec2Test(unittest.TestCase):
    def test_init(self):
        vec = Vec2(12, -3)

        self.assertEqual(12, vec.x)
        self.assertEqual(-3, vec.y)

    def test_str(self):
        vec = Vec2(-11, 3)

        self.assertEqual('(-11, 3)', str(vec))

    def test_eq(self):
        vec_1 = Vec2(11, 9)
        vec_2 = Vec2(11, 9)

        self.assertEqual(vec_1, vec_2)

    def test_eq_not(self):
        vec_1 = Vec2(11, 9)
        vec_2 = Vec2(12, 9)

        self.assertNotEqual(vec_1, vec_2)

    def test_hash(self):
        vec_1 = Vec2(678, 32)
        vec_2 = Vec2(678, 32)
        vec_3 = Vec2(677, 31)

        hash_vec_1 = hash(vec_1)
        hash_vec_2 = hash(vec_2)
        hash_vec_3 = hash(vec_3)

        self.assertEqual(hash_vec_1, hash_vec_2)
        self.assertNotEqual(hash_vec_1, hash_vec_3)
        self.assertNotEqual(hash_vec_2, hash_vec_3)

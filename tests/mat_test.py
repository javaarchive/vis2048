import unittest

from vis2048.mat import MutSqMat
from vis2048.vec2 import Vec2


class MutSqMatTest(unittest.TestCase):
    def test_init(self):
        mat = MutSqMat(4)

        self.assertEqual(mat.width, 4)

    def test_init_items(self):
        mat = MutSqMat(4, [1 for _ in range(4 * 4)])

        self.assertEqual(4, mat.width)
        self.assertEqual([1 for _ in range(4 * 4)], mat._items)

    def test_rotate_0(self):
        mat = MutSqMat(4)
        mat[Vec2(1, 1)] = 16

        mat.rotate(0)

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(1, 1)] = 16

        self.assertEqual(mat_ref, mat)

    def test_rotate_1(self):
        mat = MutSqMat(4)
        mat[Vec2(1, 1)] = 16

        mat.rotate(1)

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(1, 2)] = 16

        self.assertEqual(mat_ref, mat)

    def test_rotate_2(self):
        mat = MutSqMat(4)
        mat[Vec2(1, 1)] = 16

        mat.rotate(2)

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(2, 2)] = 16

        self.assertEqual(mat_ref, mat)

    def test_rotate_3(self):
        mat = MutSqMat(4)
        mat[Vec2(1, 1)] = 16

        mat.rotate(3)

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(2, 1)] = 16

        self.assertEqual(mat_ref, mat)

    def test_set_get(self):
        mat = MutSqMat(4)
        mat[Vec2(1, 1)] = 8
        mat[Vec2(2, 3)] = 2

        self.assertEqual(8, mat[Vec2(1, 1)])
        self.assertEqual(2, mat[Vec2(2, 3)])

    def test_set_get_row(self):
        mat = MutSqMat(4)
        mat.set_row(0, [8, 32, 64, 64])
        mat.set_row(1, [2, 4, 8, 16])
        mat.set_row(2, [4, 2, 2, 128])

        self.assertEqual([2, 4, 8, 16], mat.get_row(1))

    def test_copy(self):
        mat = MutSqMat(4)
        mat.set_row(0, [16, None, 8, 4])
        mat.set_row(2, [2, 2, None, None])

        mat_copy = mat.copy()

        self.assertEquals(mat, mat_copy)
        self.assertFalse(mat_copy is mat)

    def test_contains(self):
        mat = MutSqMat(4)

        self.assertNotIn(64, mat)

        mat[Vec2(0, 2)] = 64

        self.assertIn(64, mat)

    def test_eq(self):
        mat = MutSqMat(4)
        mat[Vec2(3, 3)] = 4
        mat[Vec2(1, 1)] = 2

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(3, 3)] = 4
        mat_ref[Vec2(1, 1)] = 2

        self.assertEquals(mat_ref, mat)

    def test_eq_not(self):
        mat = MutSqMat(4)
        mat[Vec2(3, 3)] = 2
        mat[Vec2(1, 1)] = 4

        mat_ref = MutSqMat(4)
        mat_ref[Vec2(3, 3)] = 4
        mat_ref[Vec2(1, 1)] = 2

        self.assertNotEqual(mat_ref, mat)

    def test_hash(self):
        mat = MutSqMat(4)
        mat[Vec2(2, 3)] = 32

        mat_ref = mat.copy()

        mat_other = MutSqMat(4)
        mat_other[Vec2(1, 0)] = 2

        hash_mat = hash(mat)
        hash_mat_ref = hash(mat_ref)
        hash_mat_other = hash(mat_other)

        self.assertEquals(hash_mat_ref, hash_mat)
        self.assertNotEqual(hash_mat_other, hash_mat)

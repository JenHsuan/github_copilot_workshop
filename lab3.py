import unittest
from lab2 import game

class TestGame(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(game('剪刀', '剪刀'), '平手')
        self.assertEqual(game('石頭', '石頭'), '平手')
        self.assertEqual(game('布', '布'), '平手')
        self.assertEqual(game('蜥蜴', '蜥蜴'), '平手')
        self.assertEqual(game('史波克', '史波克'), '平手')

    def test_lose(self):
        self.assertEqual(game('剪刀', '石頭'), '你輸了')
        self.assertEqual(game('石頭', '布'), '你輸了')
        self.assertEqual(game('布', '剪刀'), '你輸了')
        self.assertEqual(game('蜥蜴', '剪刀'), '你輸了')
        self.assertEqual(game('史波克', '蜥蜴'), '你輸了')

    def test_win(self):
        self.assertEqual(game('剪刀', '蜥蜴'), '你贏了')
        self.assertEqual(game('石頭', '剪刀'), '你贏了')
        self.assertEqual(game('布', '石頭'), '你贏了')
        self.assertEqual(game('蜥蜴', '布'), '你贏了')
        self.assertEqual(game('史波克', '剪刀'), '你贏了')

if __name__ == '__main__':
    unittest.main()
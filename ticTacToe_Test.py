import unittest
from Game import Game, GameOver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.g = Game()
        self.board =   [['BLANK', 'BLANK', 'BLANK'],
                        ['BLANK', 'BLANK', 'BLANK'],
                        ['BLANK', 'BLANK', 'BLANK']]

    def test_game001(self):
        g = Game()
        self.assertIsInstance(g, Game)

    def test_game_size(self):
        w = self.g.__width__
        h = self.g.__height__
        self.assertEqual((w,h), (3,3))

    def test_default_player1(self):
        self.assertEqual('O', self.g.player1)

    def test_default_player2(self):
        self.assertEqual('X', self.g.player2)

    def test_custom_player1(self):
        g = Game(player1='X')
        self.assertEqual('X', g.player1)

    def test_custom_player2(self):
        g = Game(player1='X')
        self.assertEqual('O', g.player2)

    def test_board1(self):
        self.assertEqual(self.board, self.g.board)

    def test_initial_valid_moves(self):
        self.assertEqual(self.g.__height__ * self.g.__width__, len(self.g.get_valid_moves()))

    def test_if_valid_move01(self):
        self.assertTrue(self.g.is_valid_move(1,1))

    def test_if_valid_move02(self):
        self.assertFalse(self.g.is_valid_move(3,3))

    def test_if_valid_move03(self):
        self.assertFalse(self.g.is_valid_move(-1,0))

    def test_if_valid_move04(self):
        self.g.board = [['BLANK', 'BLANK', 'BLANK'],
                        ['BLANK', 'O', 'BLANK'],
                        ['BLANK', 'BLANK', 'BLANK']]

        self.assertEqual(self.g.__height__ * self.g.__width__-1, len(self.g.get_valid_moves()))


    def test_if_valid_move05(self):
        self.g.board = [['BLANK', 'BLANK', 'BLANK'],
                        ['BLANK', 'O', 'BLANK'],
                        ['BLANK', 'BLANK', 'BLANK']]
        self.assertFalse(self.g.is_valid_move(1, 1))

    def test_if_valid_move06(self):
        self.g.board = [['O', 'O', 'O'],
                        ['O', 'O', 'O'],
                        ['BLANK', 'O', 'O']]
        self.assertEqual(self.g.__height__ * self.g.__width__-8, len(self.g.get_valid_moves()))

    def test_make_move01(self):
        self.g.make_move(1,1)
        board = [['BLANK', 'BLANK', 'BLANK'],
                 ['BLANK', 'O', 'BLANK'],
                 ['BLANK', 'BLANK', 'BLANK']]
        self.assertEqual(board, self.g.board)

    def test_make_move02(self):
        self.g.make_move(1,1)

        self.assertEqual('X', self.g.current_player)


    def test_make_move02(self):
        self.g.make_move(1,1)

        self.assertEqual('X', self.g.current_player)

    def test_goal_reached01(self):
        self.g.board = [['O', 'BLANK', 'BLANK'],
                        ['BLANK', 'O', 'BLANK'],
                        ['BLANK', 'BLANK', 'BLANK']]

        self.assertFalse(self.g.is_goal_reached())

    def test_goal_reached02(self):
        g = Game()
        g.move_record['O'] = [(0,0), (1,1), (2,2)]
        try:
            self.assertTrue(g.is_goal_reached())
        except GameOver as go:
            pass

    def test_game01(self):
        self.g.make_move(1,1)
        self.g.make_move(0,0)
        board = [['X', 'BLANK', 'BLANK'],
                 ['BLANK', 'O', 'BLANK'],
                 ['BLANK', 'BLANK', 'BLANK']]
        self.assertEqual(self.g.board, board)

    def test_game02(self):
        self.g.make_move(1, 1) # 'O'
        self.g.make_move(0, 0) # 'X'
        self.g.make_move(1,0)  # 'O'
        self.g.make_move(1,2)  # 'X'
        self.g.make_move(2,0)  # 'O'
        self.g.make_move(0,2)  # 'X'
        self.g.make_move(2,2)  # 'O'
        board = [['X', 'BLANK', 'X'],
                 ['O', 'O', 'X'],
                 ['O', 'BLANK', 'O']]
        self.assertEqual(self.g.board, board)

if __name__ == '__main__':
    unittest.main()

import unittest
import poker

class TestPoker(unittest.TestCase):

    def setUp(self):
        self.hands_patterns = [
            ['4H', '3H', '2H', '5H', '6H'], # straight flush
            ['2H', "3H", '4H', '5H', '6D'], # straight
            ['2H', "3H", '5H', '6H', '7H'], # flush
            ['2H', "3H", '6S', '5H', '7D'], # high card
            ['2H', "2D", '2S', '2C', '7D'], # four card
            ['3D', '3H', '3S', '5H', '6H'], # three card
            ['3D', '3H', '3S', '6S', '6H'], # full house
            ['5H', '5S', '4H', '3H', '9H'], # one pair
            ['5H', '5S', '3S', '3H', '9H'], # two pair
            ['4H', '3H', '2H', '5H', 'AH'], # straight flush
            ['9H', "TH", 'JH', 'QH', 'KD'], # straight
        ]

    @unittest.SkipTest
    def test_is_high_card(self):
        label = True
        hands = ['2H', '4H', '5C', '9S', 'AS']
        self.assertEqual(poker.is_high_card(hands), label)

    def test_is_straight_flush(self):
        label_patterns = [
            True, False, False, False, False, False, False, False, False, True, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_straight_flush(hands), label)

    def test_is_flush(self):
        label_patterns = [
            True, False, True, False, False, False, False, False, False, True, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_flush(hands), label)


    def test_is_straight(self):
        label_patterns = [
            True, True, False, False, False, False, False, False, False, True, True
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_straight(hands), label)

    def test_is_four_card(self):
        label_patterns = [
            False, False, False, False, True, False, False, False, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_four_card(hands), label)

    def test_is_three_card(self):
        label_patterns = [
            False, False, False, False, False, True, False, False, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_three_card(hands), label)

    def test_is_full_house(self):
        label_patterns = [
            False, False, False, False, False, False, True, False, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_full_house(hands), label)
    
    def test_is_one_pair(self):
        label_patterns = [
            False, False, False, False, False, False, False, True, False, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_one_pair(hands), label)

    def test_is_two_pair(self):
        label_patterns = [
            False, False, False, False, False, False, False, False, True, False, False
        ]
        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.is_two_pair(hands), label)

    def test_judge_hands(self):
        label_patterns = [8, 4, 5, 0, 7, 3, 6, 1, 2, 8, 4]

        for hands, label in zip(self.hands_patterns, label_patterns):
            with self.subTest(hands=hands, label=label):
                self.assertEqual(poker.judge_hands(hands), label)

    def test_str2num(self):
        test = 'A'
        self.assertEqual(poker.str2num(test), 1)
        test = 'T'
        self.assertEqual(poker.str2num(test), 10)
        test = 'J'
        self.assertEqual(poker.str2num(test), 11)
        test = 'Q'
        self.assertEqual(poker.str2num(test), 12)
        test = 'K'
        self.assertEqual(poker.str2num(test), 13)
    
    def test_fuck(self):
        player1 = ['2H', '4H', '5C', '9S', 'AS']
        player2 = ['2H', '4H', '2C', '9S', 'AS']

        self.assertEqual(poker.fuck(player1, player2), "PLAYER2 WIN!!")

        

if __name__ == '__main__':
    unittest.main()
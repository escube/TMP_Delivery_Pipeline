__author__ = 'Mago Castozzo'

import unittest

from questions.the_question import Questioner

class QuestionerTestCase(unittest.TestCase):
    def test_default_question_set(self):
        questioner = Questioner()
        self.assertEqual(questioner.message, 'Ma lo sai chi?')

if __name__ == '__main__':
    unittest.main()
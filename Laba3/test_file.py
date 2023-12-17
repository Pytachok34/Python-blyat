import unittest
from stats import text_stat

def main():
    unittest.main()

if __name__ == "__main__":
    main()
    

class MyTestCase(unittest.TestCase):

    def test_empty_content(self):
        self.assertEqual(text_stat(""), ("empty", 0, 0))

    def test_text_without_words(self):
        self.assertEqual(text_stat(" ;.   . % #"), ("no words", 0, 11))

    def test_new_line_and_tab(self):
        self.assertEqual(text_stat("3   hi \n  3"), ("3", 3, 11))

    #def test_regular(self):
        #self.assertEqual(text_stat("_"), ("empty", 0, 0))

    def test_correct_statistic(self):
        self.assertEqual(text_stat("hi,.;\n"
                                    "3      3\n"
                                    "hallo hi\n"
                                    "hallo hallo\n"
                                    "allo 3		123\n"
                                    "."), ("3", 10, 49))

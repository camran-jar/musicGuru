import unittest
from server import songSearch

class TestSongSearch(unittest.TestCase):

    def test_song_search_1950(self):
        result = songSearch(1950)
        expected = "In 1950 the number 3 song was Teardrops From My Eyes - Ruth Brown"
        self.assertEqual(result, expected)

    def test_song_search_2009(self):
        result = songSearch(2009)
        expected = "In 2009 the number 10 song was Boom Boom Pow - The Black Eyed Peas"
        self.assertEqual(result, expected)

    # Add more test cases to cover different scenarios

if __name__ == '__main__':
    unittest.main()

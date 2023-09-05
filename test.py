import unittest
from server import songSearch

class TestSongSearch(unittest.TestCase):

    def test_song_search_1950(self):
       data = songSearch(1950, test=True)
       print(data[0])
       print(data[1].split('.')[0])
       self.assertEqual(str(data[0]), data[1].split('.')[0])
    
    def test_song_search_2000(self):
       data = songSearch(2000, test=True)
       print(data[0])
       print(data[1].split('.')[0])
       self.assertEqual(str(data[0]), data[1].split('.')[0])   

    def test_song_search_1989(self):
       data = songSearch(1989, test=True)
       print(data[0])
       print(data[1].split('.')[0])
       self.assertEqual(str(data[0]), data[1].split('.')[0])

    def test_song_search_1992(self):
       data = songSearch(1992, test=True)
       print(data[0])
       print(data[1].split('.')[0])
       self.assertEqual(str(data[0]), data[1].split('.')[0])
    

if __name__ == '__main__':
    unittest.main()

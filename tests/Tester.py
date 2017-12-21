import unittest
from src.Channel import Channel
from src.Following import Following
from src.User import User

class MyTestCase(unittest.TestCase):
    def setUp(self):
        channels = [Channel("c1"), Channel("c2"), Channel("c3")]
        users = [User("u1"), User("u2"), User("u3"), User("u4")]
        followings = [Following("u1", "c1"), Following("u3", "c3"), Following("u2", "c2"),
                      Following("u4", "c2")]


    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

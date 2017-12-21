import unittest
from src.Channel import Channel
from src.Following import Following
from src.utils import *


class UtilsTester(unittest.TestCase):
    def test_get_least_used_number(self):
        phone_numbers = ["123", "456"]
        channels = [Channel("c1", "123"), Channel("c2", "123"), Channel("c3", "456")]
        least_used_number = get_least_used_number(phone_numbers, channels)
        self.assertEqual(least_used_number, "456", "Got least used number")

    def test_least_impacted_channel(self):
        channels = [Channel("c1", "123", 1), Channel("c2", "123", 2), Channel("c3", "456", 3)]
        channel = least_impacted_channel(channels)
        self.assertEqual(channel.channel_uid, "c1")

    def test_is_collision_true(self):
        channels = [Channel("c1", "123"), Channel("c2"), Channel("c3", "123")]
        followers = [Following("u1", "c1"), Following("u3", "c3"), Following("u2", "c1"), Following("u2", "c2"),
                     Following("u4", "c2")]
        collision = is_collision("123", "c2", channels, followers)
        self.assertEqual(collision, True)

    def test_is_collision_false(self):
        channels = [Channel("c1", "123"), Channel("c2"), Channel("c3", "123")]
        followers = [Following("u1", "c1"), Following("u3", "c3"), Following("u2", "c2"),
                     Following("u4", "c2")]
        collision = is_collision("123", "c2", channels, followers)
        self.assertEqual(collision, False)


if __name__ == '__main__':
    unittest.main()

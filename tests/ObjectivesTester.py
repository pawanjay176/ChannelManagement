import unittest

from src.Channel import Channel
from src.Following import Following
from src.User import User


class ObjectivesTester(unittest.TestCase):
    def test_assign_number_to_channel(self):
        c1 = Channel("c1")
        phone_numbers = list()
        channels = [c1]
        followings = [Following("u1", "c1")]
        self.assertIsNone(c1.phone_number)
        c1.assign_phone_number(phone_numbers, channels, followings)
        self.assertIsNotNone(c1.phone_number)

    def test_broadcast(self):
        c1 = Channel("c1")
        phone_numbers = list()
        channels = [c1]
        followings = [Following("u1", "c1")]
        self.assertIsNone(c1.phone_number)
        c1.broadcast(phone_numbers, channels, followings)
        self.assertIsNotNone(c1.phone_number)

    def test_minimum_phone_numbers_used(self):
        c1 = Channel("c1")
        c2 = Channel("c2")
        phone_numbers = list()
        channels = [c1, c2]
        followings = [Following("u1", "c1"), Following("u2", "c2")]
        phone_numbers = c1.broadcast(phone_numbers, channels, followings)
        self.assertEqual(len(phone_numbers), 1)
        phone_numbers = c2.broadcast(phone_numbers, channels, followings)
        self.assertEqual(len(phone_numbers), 1)

    def test_collision_handled(self):
        c1 = Channel("c1")
        c2 = Channel("c2")
        phone_numbers = list()
        channels = [c1, c2]
        followings = [Following("u1", "c1"), Following("u2", "c2"), Following("u2", "c1")]
        phone_numbers = c1.broadcast(phone_numbers, channels, followings)
        self.assertEqual(len(phone_numbers), 1)
        phone_numbers = c2.broadcast(phone_numbers, channels, followings)
        self.assertEqual(len(phone_numbers), 2)

    def test_follow_channel_without_collision(self):
        c1 = Channel("c1")
        c2 = Channel("c2")
        u2 = User("u2")
        phone_numbers = list()
        channels = [c1, c2]
        followings = [Following("u1", "c1")]
        phone_numbers = c1.broadcast(phone_numbers, channels, followings)
        phone_numbers = c2.broadcast(phone_numbers, channels, followings)

        u2.follow_channel("c2", channels, phone_numbers, followings)
        self.assertEqual(c1.phone_number, c2.phone_number)

    def test_follow_channel_with_collision(self):
        c1 = Channel("c1")
        c2 = Channel("c2")
        u2 = User("u2")
        phone_numbers = list()
        channels = [c1, c2]
        followings = [Following("u1", "c1")]
        phone_numbers = c1.broadcast(phone_numbers, channels, followings)
        phone_numbers = c2.broadcast(phone_numbers, channels, followings)

        followings, phone_numbers = u2.follow_channel("c2", channels, phone_numbers, followings)
        u2.follow_channel("c1", channels, phone_numbers, followings)
        self.assertNotEqual(c1.phone_number, c2.phone_number)


if __name__ == '__main__':
    unittest.main()

from src.Following import Following
from src.User import User

from src.Channel import Channel

channels = [Channel("c1"), Channel("c2"), Channel("c3")]
users = [User("u1"), User("u2"), User("u3"), User("u4")]
followings = [Following("u1", "c1"), Following("u3", "c3"), Following("u2", "c2"),
              Following("u4", "c2")]
c1 = channels[0]
c2 = channels[1]
c3 = channels[2]

u1 = users[0]
u2 = users[1]
u3 = users[2]
u4 = users[3]

phone_numbers = list()

phone_numbers = c1.broadcast(phone_numbers, channels, followings)
phone_numbers = c3.broadcast(phone_numbers, channels, followings)
phone_numbers = c1.broadcast(phone_numbers, channels, followings)
phone_numbers = c2.broadcast(phone_numbers, channels, followings)
phone_numbers = c2.broadcast(phone_numbers, channels, followings)
phone_numbers = c2.broadcast(phone_numbers, channels, followings)
followings, phone_numbers = u2.follow_channel(c1.channel_uid, channels, phone_numbers, followings)
# followings, phone_numbers = u2.follow_channel(c3.channel_uid, channels, phone_numbers, followings)

c4 = Channel("c4")
channels.append(c4)
phone_numbers = c4.broadcast(phone_numbers, channels, followings)
phone_numbers = c4.broadcast(phone_numbers, channels, followings)

followings, phone_numbers = u1.follow_channel(c4.channel_uid, channels, phone_numbers, followings)
followings, phone_numbers = u3.follow_channel(c4.channel_uid, channels, phone_numbers, followings)

c5 = Channel("c5")
channels.append(c5)


u5 = User("u5")
users.append(u5)
followings, phone_numbers = u5.follow_channel(c5.channel_uid, channels, phone_numbers, followings)
phone_numbers = c5.broadcast(phone_numbers, channels, followings)

print(followings)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

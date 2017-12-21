from src.Following import Following
from src import utils


class User:
    def __init__(self, uid=None, name=None):
        self.uid = uid
        self.name = name

    def __repr__(self):
        return self.uid + " " + str(self.name)

    # need to work only for channels followed by same user!!!!
    def follow_channel(self, channel_uid, channel_list, phone_numbers, followers):
        # check if user is already following the channel
        if channel_uid in [i.channel_uid for i in followers if i.user_uid == self.uid]:
            return
        # if not add to followers list
        followers.append(Following(self.uid, channel_uid))

        # get all of current user's channels
        user_channels_uid = [i.channel_uid for i in followers if i.user_uid == self.uid]
        user_channels = [i for i in channel_list if i.channel_uid in user_channels_uid]
        # check if there is a collision while following and handle

        curr_channel = [channel for channel in channel_list if channel.channel_uid == channel_uid][0]
        if curr_channel.phone_number is not None:
            if utils.is_collision(curr_channel.phone_number, channel_uid, channel_list, followers):
                # check least impacted channel among all of current user's channels
                channel_to_change = utils.least_impacted_channel(user_channels)
                phone_numbers = channel_to_change.assign_phone_number(phone_numbers, channel_list, followers)
        return followers, phone_numbers

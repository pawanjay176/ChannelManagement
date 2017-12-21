from operator import attrgetter


def get_least_used_number(phone_number_list, channel_list):
    channels_with_number = [channel for channel in channel_list if channel.phone_number in phone_number_list]
    least_used_number = None
    counts = [channel.phone_number for channel in channels_with_number]
    if len(channels_with_number) > 0:
        phone_number_count = {number: counts.count(number) for number in
                              counts}
        least_used_number = min(phone_number_count, key=phone_number_count.get)
    return least_used_number


# check if assigning phone_number to channel with uid==channel_uid results in a collision
def is_collision(phone_number, channel_uid, channel_list, followers):
    if phone_number is None:
        return False
    channels_with_number = [channel for channel in channel_list if channel.phone_number == phone_number]
    # users following channel_uid
    curr_users = [i.user_uid for i in followers if(i.channel_uid == channel_uid)]
    for user in curr_users:
        # find all channels that user follows
        user_channels = [i.channel_uid for i in followers if i.user_uid == user and i.channel_uid != channel_uid]
        for channel in user_channels:
            if channel in [i.channel_uid for i in channels_with_number]:
                return True
    return False


def least_impacted_channel(channel_list):
    return min(channel_list, key=attrgetter('broadcast_count'))


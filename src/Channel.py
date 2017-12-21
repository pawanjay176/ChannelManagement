import random
import string
from src import utils
import copy

class Channel:
    def __init__(self, channel_uid=None, phone_number=None, broadcast_count=0):
        self.channel_uid = channel_uid
        self.phone_number = phone_number
        self.broadcast_count = broadcast_count

    def __repr__(self):
        return self.channel_uid+" "+str(self.phone_number)+" "+str(self.broadcast_count)

    """
    Assign least used phone_number to current channel
    If all phone_numbers result in a collision, generate a new one
    """
    def assign_phone_number(self, phone_numbers, channel_list, followers):
        # Get the least used phone_number from phone_numbers list
        number_to_assign = utils.get_least_used_number(phone_number_list=phone_numbers,
                                                       channel_list=channel_list)
        new_phone_numbers = copy.deepcopy(phone_numbers)
        phone_numbers = [i for i in phone_numbers if i != number_to_assign]

        # Keep updating number_to_assign till there is no collision
        while utils.is_collision(number_to_assign, self.channel_uid, channel_list, followers):
            number_to_assign = utils.get_least_used_number(phone_number_list=phone_numbers,
                                                           channel_list=channel_list)
            phone_numbers = [i for i in phone_numbers if i != number_to_assign]

        # If existing phone_number couldn't be used, generate a new one and set it as channel phone_number
        # Not handled duplicate numbers!
        if number_to_assign is None:
            number_to_assign = ''.join(random.choice(string.digits) for i in range(3))
        self.phone_number = number_to_assign

        if number_to_assign not in new_phone_numbers:
            new_phone_numbers.append(number_to_assign)

        return new_phone_numbers

    """
    Placeholder for increasing broadcast_count of channel
    Assigns a phone number if channel doesn't have one and returns list of used phone_numbers
    """
    def broadcast(self, phone_numbers, channel_list, followers):
        if self.phone_number is None:
            phone_numbers = self.assign_phone_number(phone_numbers, channel_list, followers)
        self.broadcast_count += 1
        return phone_numbers


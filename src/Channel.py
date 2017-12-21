import random
import string

from src import utils


class Channel:
    def __init__(self, channel_uid=None, phone_number=None):
        self.channel_uid = channel_uid
        self.phone_number = phone_number
        self.broadcast_count = 0

    def __repr__(self):
        return self.channel_uid+" "+str(self.phone_number)+" "+str(self.broadcast_count)

    def assign_phone_number(self, phone_numbers, channel_list, followers):
        number_to_assign = utils.get_least_used_number(phone_number_list=phone_numbers,
                                                       channel_list=channel_list)
        phone_numbers = [i for i in phone_numbers if i != number_to_assign]
        while utils.is_collision(number_to_assign, self.channel_uid, channel_list, followers):
            number_to_assign = utils.get_least_used_number(phone_number_list=phone_numbers,
                                                           channel_list=channel_list)
            phone_numbers = [i for i in phone_numbers if i != number_to_assign]

        if number_to_assign is None:
            number_to_assign = ''.join(random.choice(string.digits) for i in range(3))
        self.phone_number = number_to_assign

        if number_to_assign not in phone_numbers:
            phone_numbers.append(number_to_assign)
        return phone_numbers

    def broadcast(self, phone_numbers, channel_list, followers):
        if self.phone_number is None:
            phone_numbers = self.assign_phone_number(phone_numbers, channel_list, followers)
        self.broadcast_count += 1
        return phone_numbers


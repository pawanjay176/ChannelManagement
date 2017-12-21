class Following:
    def __init__(self, user_uid, channel_uid):
        self.user_uid = user_uid
        self.channel_uid = channel_uid

    def __repr__(self):
        return self.channel_uid + " " + self.user_uid

    def get_channel_uid(self):
        return self.channel_uid

    def get_user_uid(self):
        return self.user_uid

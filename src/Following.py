class Following:
    def __init__(self, user_uid, channel_uid):
        self.user_uid = user_uid
        self.channel_uid = channel_uid

    def __repr__(self):
        return str(self.channel_uid) + " " + str(self.user_uid)

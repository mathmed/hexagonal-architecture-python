
class UserNotFoundError(Exception):

    def __init__(self, message='User not found'):
        self.message = message
        super().__init__(self.message)

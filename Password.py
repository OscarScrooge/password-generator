import random


class Password():

    def __init__(self, length):
        self.members = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&/()=?¡"
        self.length = length


    def newPassword(self):
        password_generated = ""

        for i in range(self.length):
            random_member = random.randint(0, len(self.members) - 1)
            password_generated += self.members[random_member]

        return password_generated

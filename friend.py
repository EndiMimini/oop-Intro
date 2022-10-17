
class Friend:
    def __init__(self):
        self.friends = []
        self.friendsNumber = 0
    
    def addFriend(self, user):
        self.friends.append(user)
        self.friendsNumber += 1
        print('Friend Added', user.firstName , user.lastName)
        print('Total number of friends: ' + str(self.friendsNumber))
        return self


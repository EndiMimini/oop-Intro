from friend import Friend

class User:
    userType = 'Human'
    gender = 'Female'
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.friends = Friend()

    #methods 
    # when we pass in self => instance method
    # when we pass in cls => class method
    # static 

    def introduce_yourself(self):
        print('My name is ' + self.firstName + ' ' + self.lastName + ' and at the moment I have ' + str(self.friends.friendsNumber) + ' friends')
    
    @classmethod
    def displayType(cls):
        print(cls.userType)
        print(cls.gender)
        return cls
    
    def addFriend(self, user):
        self.friends.addFriend(user)
        return self


irida = User('Irida', 'Rapi')

blerta = User('Blerta', 'Kola')


irida.introduce_yourself()
irida.displayType()

blerta.introduce_yourself()
blerta.displayType()
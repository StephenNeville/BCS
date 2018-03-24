+# Object-oriented programming
# source: wikipedia


class Human(object):
    def __init__(self, name, friend=None):
        self.name = name
        self.friend = friend
    def say_name(self):
        print("My name is "+self.name)
    def say_goodnight(self):
        if self.friend is None:
            print("Good night nobody.")
        else:
            print("Good night "+self.friend.name)

#create a new human object named stephen
stephen = Human("Stephen")
#create a human object named joe with stephen as a friend
joe = Human("Joe", stephen)

stephen.say_name() #shows 'My name is Stephen'
stephen.say_goodnight() #shows 'Good night nobody.'
joe.say_name() # shows 'My name is Joe'
joe.say_goodnight() #shows 'Good night Stephen'

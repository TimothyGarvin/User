class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print(f'\n===============')
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("Already Enrolled!")
        else:
            self.gold_card_points = 200
            self.is_rewards_member = True
    
    def spend_points(self,amount):
        if self.gold_card_points < amount:
            print("Insufficient Funds!")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)

Adam = User("Adam", "Sapple", "asap@gmail.com", 37,)
Trent = User("Trent", "Reznor", "Fromnothingent@gmail.com.", 57)
Liz = User("Liz", "Snyder", "lizsnyder@yahoo.com", 66)

Adam.spend_points(50)

Trent.enroll()
Trent.spend_points(80)

Adam.display_info()
Trent.display_info()
Liz.display_info()

Trent.enroll()

Liz.spend_points(40)
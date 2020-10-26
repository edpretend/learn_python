class Employee():    
    def __init__(self, first_name, last_name, money):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money

    def give_raise(self, money_plus = 5000):
        self.money += money_plus

from random import randint

class Die():
    def __init__(self, message='y'):
        self.message = message
        self.type_list = []
        self.time_list = []

    def roll_one_time(self, one_sides=6):
        """同一类型的一次roll"""
        return randint(1, one_sides)

    def roll_one_type(self, one_type_sides, time):
        """同一类型的多次roll"""
        sum_roll = 0
        i = 1
        #循环体实现同类型相加
        while True:
            if i >= 1 and i <= int(time):
                sum_roll += self.roll_one_time(one_type_sides)
                i += 1
                continue
            break
        return sum_roll

    def roll_some_types(self, num_types):
        """手动录入"""
        #num_types = input("Please input number of types: ")
        #循环体生成类型列表types
        i = 1
        while True:
            if i >= 1 and i <= int(num_types):
                this_type = input("Please input this type, what's num side: ")
                this_time = input("Please input this time of this type, what's time: ")
                self.type_list.append(int(this_type))
                self.time_list.append(int(this_time))
                i += 1
                continue
            break
        #开始roll并求和
        sum_roll = 0
        for j in range(1, len(self.type_list) + 1):
            sum_roll += self.roll_one_type(self.type_list[j-1], self.time_list[j-1])
        return sum_roll

    def auto_roll_some_types(self, type_list=[], time_list=[]):
        """导入列表自动生成"""
        sum_roll = 0
        self.type_list = type_list
        self.time_list = time_list
        for j in range(1, len(self.type_list) + 1):
            sum_roll += self.roll_one_type(self.type_list[j-1], self.time_list[j-1])
        return sum_roll

    def auto_last_roll(self):
        """使用记录过的上一次的参数，继续roll"""
        sum_roll = 0
        for j in range(1, len(self.type_list) + 1):
            sum_roll += self.roll_one_type(self.type_list[j-1], self.time_list[j-1])
        return sum_roll


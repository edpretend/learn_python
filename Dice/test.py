from die import Die

die = Die('new')
type_list = [2, 3, 5]
time_list = [100000, 100000, 100000]
#num_types = input("Please input number of types: ")
one_roll = die.auto_roll_some_types(type_list, time_list)
print(one_roll)
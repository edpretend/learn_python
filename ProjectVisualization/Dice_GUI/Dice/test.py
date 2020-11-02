from class_die import Die

die = Die('new')
type_list = [2, 3, 5]
time_list = [1000, 1000, 1000]
#num_types = input("Please input number of types: ")
one_roll = die.auto_roll_some_types(type_list, time_list)
print(one_roll)

last_roll = die.auto_last_roll()
print(last_roll)
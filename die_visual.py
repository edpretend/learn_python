from die import Die

die_num = input("Please input number of dice to roll: ")

#while True:
#    x = input('Input an integer: ')
#    if x.isdigit():
#        break
#    else:
#        print('Please input an *integer*')




while True:
    if question1 == 'Y' or question1 == 'y':
        num_sides = input("Please input num sides of dices: ")
        break
    elif question1 == 'N' or question1 == 'n':
        num_sides = []
        for d_num in range(1, int(die_num)+1):
            print("Please input num sides of dice" + str(d_num) + ".")
            num_side = input("Num sides of this dice: ")
            num_sides.append(num_side)
        break
    else:
        continue

roll_number = input("Tell me the roll number: ")
for r_num in range(1, int(roll_number)+1):
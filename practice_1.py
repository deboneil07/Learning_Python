def greatest_no_in_a_list():
    num_holder = []

    num_input = input('enter the numbers! or press q to quit! ')

    while num_input.lower() != 'q':
    
        num_keep = int(num_input)
        num_holder.append(num_keep)

        num_input = input("enter the number or press q to quit! ")

    num_holder.sort()
    print(num_holder)
    print(f'the  greatest number in the list is {num_holder[-1]} ')
    
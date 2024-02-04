locker_code = ['_', '_', '_', '_', '_']

for _ in range(5):
    input_number = input("Enter a 2-digit number: ")
    position = int(input_number[0]) - 1
    digit = input_number[1]
    locker_code[position] = digit

# main
print(''.join(locker_code))

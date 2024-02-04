start_number = int(input())
current_number = start_number

while current_number >= 0:
    print(current_number)
    current_number -= 1 + (start_number - current_number)

num_pupils = int(input())
group_sizes = [5, 4, 3]

largest_group_size = 0
for size in group_sizes:
    if num_pupils % size == 0 and size > largest_group_size:
        largest_group_size = size

num_groups = num_pupils // largest_group_size

# main
print("{}x{}".format(num_groups, largest_group_size))

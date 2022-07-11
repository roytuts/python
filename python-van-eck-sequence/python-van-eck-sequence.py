num_dict = {}
next_num = 0
sequence = ''

for i in range(100):
    if next_num in num_dict:
        distance = i - num_dict[next_num]
    else:
        distance = 0

    num_dict[next_num] = i
    sequence += "%d, " % next_num
    next_num = distance

print(sequence)

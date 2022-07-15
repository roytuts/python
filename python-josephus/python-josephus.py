def josephus(num_people, rem_pos):
    temp_pos = rem_pos - 1
    people = []
    
    for i in range(num_people):
        people.append(i+1)
    
    iteration = num_people - 1
    
    while iteration > 0:
        people.pop(temp_pos)
        temp_pos += rem_pos - 1
        if(temp_pos > len(people) - 1):
            temp_pos = temp_pos % len(people)
        iteration = iteration - 1
    
    return people[0]

print('Winner is %d' % josephus(5, 3))
print('Winner is %d' % josephus(10, 3))
print('Winner is %d' % josephus(5, 2))
print('Winner is %d' % josephus(7, 3))

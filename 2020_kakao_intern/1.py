numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

l_pos, r_pos = [4,1], [4,3]
result = ''

for number in numbers:
    x = ((number-1) // 3) + 1
    y = ((number-1) % 3) + 1
    
    if number in [1,4,7]:
        l_pos = [x, y]
        result += 'L'
    elif number in [3,6,9]:
        r_pos = [x, y]
        result += 'R'
    else:
        l_distance = abs(l_pos[0] - x)+abs(l_pos[1] - y)
        r_distance = abs(r_pos[0] - x)+abs(r_pos[1] - y)
        if l_distance > r_distance:
            r_pos = [x, y]
            result += 'R'
        elif l_distance < r_distance:
            l_pos = [x, y]
            result += 'L'
        else:
            if hand == 'right':
                r_pos = [x, y]
                result += 'R'
            else:
                l_pos = [x, y]
                result += 'L'
    
    print(result)
    print(l_pos, r_pos)
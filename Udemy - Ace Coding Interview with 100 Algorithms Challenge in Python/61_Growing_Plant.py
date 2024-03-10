"""
"""

def find_height(up_speed, down_speed, target_level, initial_height=0):
    current_height = initial_height
    num_days = 0

    while current_height < target_level:
        num_days += 1
        current_height += up_speed

        if current_height >= target_level:
            break

        current_height -= down_speed 

    return num_days
    

    


if __name__ == "__main__":
    up_speed = 4
    down_speed = 3
    target_level = 20
    initial_height = 0
    res = find_height(up_speed, down_speed, target_level, initial_height)

    print(res)
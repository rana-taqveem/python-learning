def turn_left():
    print('turn_left')

def move():
    print('move')

def at_goal():
    return True

def front_is_clear():
    return True

def right_is_clear():
    return True

def wall_in_front():
    return True


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
move_count = 0
trun_right_count = 0
turn_left_count = 0
   
while not at_goal():
    if front_is_clear():
        move()
        move_count = move_count + 1
    if right_is_clear():
        turn_right()
        trun_right_count = trun_right_count + 1
    
    if move_count == 4 and trun_right_count == 4 and turn_left_count == 0:
        turn_left()
        move_count = 0
        trun_right_count = 0
        turn_left_count = 0
        
    
    if wall_in_front():
        turn_left()
        turn_left_count = turn_left_count + 1


        

        
        
  




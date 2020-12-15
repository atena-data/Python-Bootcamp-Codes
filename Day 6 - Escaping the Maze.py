#follow this link to load the maze [maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

#create a function to turn right in the maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
    
#code to direct robot to the goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
        if right_is_clear() and not at_goal():
            turn_right()
            move()
    elif wall_in_front():
        turn_left()

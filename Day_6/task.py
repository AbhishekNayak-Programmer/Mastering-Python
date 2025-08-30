# Functions 
def greet() :
    print("Hello World")

greet()


# Alone Reeborg Robot
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# Square Command
# def turn_around() :
#     turn_left()
#     turn_left()
    
# def turn_right() :
#     turn_left()
#     turn_left()
#     turn_left()
    

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()


# The Hurdle Loop
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# count = 0
    
# while count < 6 :
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#     count += 1

# Random Win Hurdle
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal() :
#     jump()


# Hurdle 3 
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal() :
#     if wall_in_front() :
#         jump()
#     else :
#         move()
 

# Hurdle 4
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#  def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right() :
#         move()
        
#     turn_right()
#     move()
#     turn_right()
    
#     while not wall_in_front() :
#         move()
        
#     turn_left()

# while not at_goal() :
#     if wall_in_front() :
#         jump()
#     else :
#         move()
 

# Maze
# Link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear() :
#     move()
# turn_left()

# while not at_goal() :
#      if right_is_clear() :
#          turn_right()
#          move()
#      elif front_is_clear() :
#         move()
#      else :
#         turn_left()
      
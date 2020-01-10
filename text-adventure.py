# TextBased Adventure Game
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

# multi-dimensional array: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
#
# 6 rooms:
#
# [0,2][1,2]
# [0,1][1,1]
# [0,0][1,0]
#

h, w = 3, 2;

rooms = [[0 for y in range(h)] for x in range(w)]

rooms[0][0] = "You are in the kitchen. There are doors to the North and East."
rooms[0][1] = "You are in the living room. There are doors to the North, South, and East."
rooms[0][2] = "You are in the dungeon suite. There are doors to the South and East."
rooms[1][0] = "You are in the bathroom. There are doors to the North and West."
rooms[1][1] = "You are in the garage. There are doors to the North, South, and West."
rooms[1][2] = "You are on the porch. There are doors to the South and West."

# start at 0,0
locationX = 0
locationY = 0

# Dictionary
directionLookup = {
    "n": (0,1), # tuples
    "s": (0,-1),
    "e": (1,0),
    "w": (-1,0)
}

print("Commands: n (North), e (East), s (South), w (West)")

while True:
    print(rooms[locationX][locationY])
    
    command = input()
    
    if command == 'quit':
        break    
    
    if not command in directionLookup:
        print("Huh?")
    else:
        newLocationX = locationX + directionLookup.get(command)[0]
        newLocationY = locationY + directionLookup.get(command)[1]
        
        if newLocationX < 0 or newLocationX >= w or newLocationY < 0 or newLocationY >= h:
            print("There is a wall there. You cannot go in that direction.")
        else:
            locationX = newLocationX
            locationY = newLocationY
    
   



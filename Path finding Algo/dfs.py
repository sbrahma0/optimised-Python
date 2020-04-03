# https://realpython.com/beginners-guide-python-turtle/  -  This is the fundamental of the turtle graphics library
# It is recommended to use the deque library from collection module since its time complexity for append and pop from both
# side is O(n).
import turtle
grid = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+           +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++ +++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]
# You can get more grid configuration from the frid file.
# This is the function to generate the maze
def maze_making(grid, t, res = 1.5):
    t.hideturtle()
    s.setup(1300/res,700/res)
    t.shape("square")
    t.shapesize(1/res,1/res)
    t.color('white')
    t.penup()

    walls = []
    path = []

    rows = len(grid) # This is the number of rows
    col = len(grid[0]) # This is the number of column

    for r in range(rows):
        for c in range(col):
            x,y = (-600 + c*24)/res ,(300 - r*24)/res # these are to be considered as a single point at the center of the turtle
            char = grid[r][c]
            if char == '+': # These are the walls
                walls.append((c,r))
                t.goto(x,y)
                t.color("black")
                t.stamp()
                t.speed(0)
            else:
                path.append((c,r))
    return walls, path

def stamp(x,y,t,colour,res = 1.5):
    X, Y = (-600 + x * 24) / res, (300 - y * 24) / res
    t.goto(X, Y)
    t.color(colour)
    t.stamp()
    t.speed(0)
# Breadth First search
def bfs(start_x, start_y, end_x, end_y, path, res,t):
    frontier = []
    visited = set()
    back_track = {}
    back_track[start_x,start_y] = start_x,start_y
    frontier.append((start_x,start_y))

    while len(frontier)>0:
        #print(frontier)
        x,y = frontier.pop()  # This is the main difference of DFS from BFS, in BFS we used queu(First in First out)
                              # But in DFS we use stack(Last in First out)
                              # In DFS and BFS some adjustments can be done by changing the order of discovering the neighbours
                              # But for comparison i have kept both as same.
        #print(x,y)
        if (x,y-1) in path and (x,y-1) not in visited: # Check for the down cell
            stamp(x,y-1,t,'green', res)
            visited.add((x,y-1))
            back_track[x,y-1] = x,y
            frontier.append((x,y-1))
            if (x,y-1) == (end_x,end_y):
                return back_track

        if (x, y + 1) in path and (x, y + 1) not in visited:  # Check for the upper cell
            stamp(x, y + 1,t, 'green',res)
            visited.add((x, y + 1))
            back_track[x, y + 1] = x, y
            frontier.append((x, y + 1))
            if (x, y + 1) == (end_x, end_y):
                return back_track

        if (x-1, y) in path and (x-1, y) not in visited:  # Check for the left cell
            stamp(x-1, y, t,'green', res)
            visited.add((x-1, y))
            back_track[x-1, y] = x, y
            frontier.append((x-1, y))
            if (x-1, y) == (end_x, end_y):
                return back_track

        if (x+1, y) in path and (x+1, y) not in visited:  # Check for the right cell
            stamp(x+1, y, t,'green', res)
            visited.add((x+1, y))
            back_track[x+1, y] = x, y
            frontier.append((x+1, y))
            if (x+1, y) == (end_x, end_y):
                return back_track
        #print (visited)
        #print('*******')
        #print (back_track)

def path_tracking(end_x, end_y, start_x, start_y, t, bt):

    while (end_x,end_y) != (start_x,start_y):
        stamp(end_x, end_y, t, 'yellow', 1.5)
        (end_x, end_y) = bt[end_x,end_y]

s = turtle.Screen()
t = turtle.Turtle()
res = 1.5
w,p = maze_making(grid, t, res)
start_x = input("Enter the start x point - ")
start_y = input("Enter the start y point - ")
end_x = input("Enter the start x point - ")
end_y = input("Enter the start y point - ")

if (start_x,start_y) in w or (end_x ,end_y) in w:
    print("In obstacle")
else:
    x, y = (-600 + start_x * 24) / res, (300 - start_y * 24) / res
    t.goto(x,y)
    t.color("red")
    t.stamp()
    t.speed(0)

    x, y = (-600 + end_x * 24) / res, (300 - end_y * 24) / res
    t.goto(x,y)
    t.color("blue")
    t.stamp()
    t.speed(0)

    bt = bfs(start_x,start_y,end_x,end_y,p, res,t)
    path_tracking(end_x,end_y,start_x,start_y, t,bt)
s.exitonclick()

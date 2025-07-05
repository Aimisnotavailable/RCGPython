import turtle

# Maze parameters
maze_size = 10
cell_size = 30

# Maze definition (8x8 inner maze, surrounded by walls)
inner_maze = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0]
]

# Add outer walls
maze = [[1]*maze_size]
for row in inner_maze:
    maze.append([1] + row + [1])
maze.append([1]*maze_size)

goal_pos = (maze_size - 2, maze_size - 2)  # bottom-right inside the wall

def draw_maze(maze, cell_size):
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.hideturtle()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            screen_x = x * cell_size - (maze_size // 2) * cell_size
            screen_y = (maze_size // 2) * cell_size - y * cell_size
            if cell == 1:
                drawer.penup()
                drawer.goto(screen_x, screen_y)
                drawer.pendown()
                drawer.fillcolor("black")
                drawer.begin_fill()
                for _ in range(4):
                    drawer.forward(cell_size)
                    drawer.right(90)
                drawer.end_fill()
            elif (x, y) == goal_pos:
                drawer.penup()
                drawer.goto(screen_x, screen_y)
                drawer.pendown()
                drawer.fillcolor("green")
                drawer.begin_fill()
                for _ in range(4):
                    drawer.forward(cell_size)
                    drawer.right(90)
                drawer.end_fill()
            else:
                # Draw white background for open cells to make walls clear
                drawer.penup()
                drawer.goto(screen_x, screen_y)
                drawer.pendown()
                drawer.fillcolor("white")
                drawer.begin_fill()
                for _ in range(4):
                    drawer.forward(cell_size)
                    drawer.right(90)
                drawer.end_fill()
    drawer.penup()

# Draw the maze
draw_maze(maze, cell_size)

# Player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.shapesize(stretch_wid=cell_size/20*0.7, stretch_len=cell_size/20*0.7)  # scale turtle
player.penup()
start_x = 1 * cell_size - (maze_size // 2) * cell_size + cell_size / 2

start_y = (maze_size // 2) * cell_size - 1 * cell_size - cell_size / 2
player.goto(start_x, start_y)
player.setheading(0)

# Player position in maze grid
player_pos = [1, 1]

def can_move(nx, ny):
    return 0 <= nx < maze_size and 0 <= ny < maze_size and maze[ny][nx] == 0

def move_left():
    x, y = player_pos
    nx, ny = x - 1, y
    if can_move(nx, ny):
        screen_x = nx * cell_size - (maze_size // 2) * cell_size + cell_size / 2
        screen_y = (maze_size // 2) * cell_size - ny * cell_size - cell_size / 2
        player.goto(screen_x, screen_y)
        player_pos[0], player_pos[1] = nx, ny
        if (nx, ny) == goal_pos:
            print("Congratulations! You reached the goal!")
            turtle.done()
            exit()
    else:
        print("Can't move there!")

def move_right():
    x, y = player_pos
    nx, ny = x + 1, y
    if can_move(nx, ny):
        screen_x = nx * cell_size - (maze_size // 2) * cell_size + cell_size / 2
        screen_y = (maze_size // 2) * cell_size - ny * cell_size - cell_size / 2
        player.goto(screen_x, screen_y)
        player_pos[0], player_pos[1] = nx, ny
        if (nx, ny) == goal_pos:
            print("Congratulations! You reached the goal!")
            turtle.done()
            exit()
    else:
        print("Can't move there!")

def move_up():
    x, y = player_pos
    nx, ny = x, y - 1
    if can_move(nx, ny):
        screen_x = nx * cell_size - (maze_size // 2) * cell_size + cell_size / 2
        screen_y = (maze_size // 2) * cell_size - ny * cell_size - cell_size / 2
        player.goto(screen_x, screen_y)
        player_pos[0], player_pos[1] = nx, ny
        if (nx, ny) == goal_pos:
            print("Congratulations! You reached the goal!")
            turtle.done()
            exit()
    else:
        print("Can't move there!")

def move_down():
    x, y = player_pos
    nx, ny = x, y + 1
    if can_move(nx, ny):
        screen_x = nx * cell_size - (maze_size // 2) * cell_size + cell_size / 2
        screen_y = (maze_size // 2) * cell_size - ny * cell_size - cell_size / 2
        player.goto(screen_x, screen_y)
        player_pos[0], player_pos[1] = nx, ny
        if (nx, ny) == goal_pos:
            print("Congratulations! You reached the goal!")
            turtle.done()
            exit()
    else:
        print("Can't move there!")

while True:
    cmd = input("Enter direction (left/right/up/down) or 'quit': ")
    if cmd is None or cmd.lower() == 'quit':
        break
    if cmd.lower() == 'left':
        move_left()
    elif cmd.lower() == 'right':
        move_right()
    elif cmd.lower() == 'up':
        move_up()
    elif cmd.lower() == 'down':
        move_down()
    else:
        print("Invalid direction.")

turtle.done()
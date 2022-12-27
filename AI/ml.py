import random
import curses

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)

# Define the dimensions of the screen
width = screen.getmaxyx()[1]
height = screen.getmaxyx()[0]

# Define the initial position of the snake
snake = [(height // 2, width // 2)]

# Define the initial direction of the snake
direction = (0, 1)

# Define the initial position of the food
food = (random.randint(0, height - 1), random.randint(0, width - 1))

# Initialize the score
score = 0

# Main game loop
while True:
    # Clear the screen
    screen.clear()
    
    # Draw the snake
    for y, x in snake:
        screen.addstr(y, x, '#')
    
    # Draw the food
    screen.addstr(food[0], food[1], '*')
    
    # Update the snake position
    snake.insert(0, (snake[0][0] + direction[0], snake[0][1] + direction[1]))
    snake.pop()
    
    # Check if the snake has collided with the food
    if snake[0] == food:
        # Update the score and generate a new piece of food
        score += 1
        food = (random.randint(0, height - 1), random.randint(0, width - 1))
    else:
        # Remove the tail of the snake
        snake.pop()
    
    # Check if the snake has collided with a wall
    if snake[0][0] == 0 or snake[0][0] == height - 1 or snake[0][1] == 0 or snake[0][1] == width - 1:
        break
    
    # Check if the snake has collided with itself
    if snake[0] in snake[1:]:
        break
    
    # Update the screen
    screen.refresh()
    curses.napms(100)
    
    # Check for user input
    key = screen.getch()
    if key == ord('w'):
        direction = (-1, 0)
    elif key == ord('a'):
        direction = (0, -1)
    elif key == ord('s'):
        direction = (1, 0)
    elif key == ord('d'):
        direction = (0, 1)

# End the game
curses.endwin()
print(f'Game over! Your score is {score}')

#Dependencies
from tkinter import *
import random

WIDTH = 800
HEIGHT = 800
REFRESH_RATE = 120
SPACE_SIZE = 40
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
APPLE_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
SCORE = 0
DIRECTION = "down"


class Snake():
  
  def __init__(self):
    self.body_size = BODY_PARTS
    self.coords = []
    self.squares = []
    
    for i in range(0, self.body_size):
      self.coords.append([0, 0])
      
    for x, y in self.coords:
      square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE)
      self.squares.append(square)
    
    
class Apple():
  
  def __init__(self):
    
    x = random.randint(0, WIDTH / SPACE_SIZE - 1) * SPACE_SIZE
    y = random.randint(0, HEIGHT / SPACE_SIZE - 1) * SPACE_SIZE
    
    self.coords = [x, y]
    
    canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=APPLE_COLOR, tag="apple")
    
  
def next_turn(snake, apple):
  
  x, y = snake.coords[0]
  
  if DIRECTION == "left":
    x -= SPACE_SIZE
  elif DIRECTION == "right":
    x += SPACE_SIZE
  elif DIRECTION == "up":
    y -= SPACE_SIZE
  elif DIRECTION == "down":
    y += SPACE_SIZE
    
  snake.coords.insert(0, (x, y))
  square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
  snake.squares.insert(0, square)
  
  if x == apple.coords[0] and y == apple.coords[1]:
    global SCORE
    SCORE += 1
    scoreLabel.config(text=f"Score: {SCORE}")
    canvas.delete("apple")
    apple = Apple()
  else:
    del snake.coords[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
    
  if check_collision(snake):
    game_over()
  else:  
    window.after(REFRESH_RATE, next_turn, snake, apple)
  
  
def change_direction(new_direction):

  global DIRECTION
  
  if new_direction == "left":
    if DIRECTION != "right":
      DIRECTION = new_direction
  elif new_direction == "right":
    if DIRECTION != "left":
      DIRECTION = new_direction
  elif new_direction == "up":
    if DIRECTION != "down":
      DIRECTION = new_direction
  elif new_direction == "down":
    if DIRECTION != "up":
      DIRECTION = new_direction
  
  
def check_collision(snake):
  
  x, y = snake.coords[0]
  
  if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
    return True
  
  for body_part in snake.coords[1:]:
    if x == body_part[0] and y == body_part[1]:
      return True


def game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("consolas", 40), text="GAME OVER", fill="#FF0000")



#Window Config
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

#Score Label
scoreLabel = Label(window, text = f"Score: {SCORE}", font=("consolas", 40))
scoreLabel.pack()

#Game Board
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

#Reposition Window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width / 2 - WIDTH / 2)
y = int(screen_height / 2 - HEIGHT / 2)
window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

#Instanciate Classes
snake = Snake()
apple = Apple()

next_turn(snake, apple)


window.mainloop()
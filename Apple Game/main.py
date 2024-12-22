import pgzrun
import random

WIDTH = 400
HEIGHT = 400

basket = Actor('basket', center=(200, 350))
apple = Actor('apple', center=(random.randint(50, 350), 0))
score = 0

def draw():
    screen.clear()
    basket.draw()
    apple.draw()
    screen.draw.text(f"Score: {score}", (10, 10), color="white")

def update():
    global score
    apple.y += 4
    if apple.colliderect(basket):
        score += 1
        apple.x = random.randint(50, 350)
        apple.y = 0
    if apple.y > HEIGHT:
        apple.x = random.randint(50, 350)
        apple.y = 0
    if keyboard.left:
        basket.x -= 10
    if keyboard.right:
        basket.x += 10

pgzrun.go()

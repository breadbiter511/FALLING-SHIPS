import pygame
import pgzrun
import random

pygame.init()
WIDTH = 1000
HEIGHT = 500

shooter = Actor("person.png")
bullet = Actor("bullet.png")
ship = Actor("ship.png")
shooter.pos = (500,480)
ships = []
ship_count = 0
game_over = False
fire_ball = False
def create_ship():
    num = 0
    for i in range(8):
        temp = Actor("ship.png")
        ships.append(temp)
        ships[i].pos = (125 * num + 33,50)
        num = num + 1 

create_ship()

def draw():
    global ships
    screen.blit("background",(0,0))
    shooter.draw()
    for i in ships:
        i.draw()
        i.y = i.y + random.randint(0,3)-0.8
    if fire_ball == True:
        bullet.y = bullet.y - 10
    if game_over == True:
        screen.clear()
        screen.fill("red")
        screen.draw.text("YOU LOSE",(500,250),fontsize = 150)
    if ship_count == 8:
        screen.clear()
        screen.fill("green")
        screen.draw.text("YOU WIN",(500,250),fontsize = 200)

def update():
    global ship_count,ships,game_over
    if keyboard.left:
        shooter.x = shooter.x - 10
    if keyboard.right:
        shooter.x = shooter.x + 10
    if keyboard[keys.SPACE]:
        fire()

def fire():
    global fire_ball
    fire_ball = True
    bullet.pos = (shooter.x,(shooter.y-5))
    
    
pgzrun.go()
# 2023182003 김서진
from pico2d import *

import game_world
from grass import Grass
from boy import Boy
from ball import Ball


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass(40)
    game_world.add_object(grass, 0)

    grass = Grass(20)
    game_world.add_object(grass, 2)



def add_object(o, depth):
    game_world.add_object(o, depth)

def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.03)
# finalization code
close_canvas()

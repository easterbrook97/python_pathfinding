import pygame
from queue import PriorityQueue


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# goes back through came_from and turns nodes inside purple
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def greedy_search(draw, grid, start, end):
    pass

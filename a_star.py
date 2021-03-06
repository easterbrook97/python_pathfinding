import pygame
from queue import PriorityQueue

# manhatten distance to estimate distance from current node to end node
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

def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    # move through each node in the open set
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)


        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        #  creates a temp g_score for each neighbour of a given node
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            #  if the temp g score is less than current g score it is updated
            #  also assigns the node which came before the neighbour
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                #  if the neighbour is not in open_set add to open set
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()
        # once all neighbours have been explored close the current node
        if current != start:
            current.make_closed()
    return False
